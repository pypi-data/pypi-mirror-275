import time
import uuid
from typing import List, Tuple, Set, Dict

from eras.factories.function_details_factory import FunctionDetailsFactory
from eras.models.conversation import Conversation
from eras.services.llm_callable_functions.user_details import UserDetails

system_prompt = "You are a helpful assistant that answers questions accurately, without making up facts."
model = "gpt-3.5-turbo"


# Agent which:
# - provides an inference function which accepts a question to send to chatgpt and responds with the answer.
# - maintains a conversation, which is a collection of messages that have been sent to and received from chatgpt.
# - determines if chatgpt has requested that a local function has been called.
# - executes the local function and sends the result to chatgpt (via conversation messages)
class OpenAILLMFunctionsAgent:
    def __init__(self, openai_client):
        # print('init')
        self.callable_function_service = UserDetails()
        self.tools = [] + self.callable_function_service.get_tools()
        self.openai_client = openai_client

    def inference(self, question=None, conversation=None, start_time_seconds=None):
        # print('------- inference ------------')
        # start a new conversation if needed, which tracks all messages to and from chatgpt
        conversation = self.ensure_conversation_exists(conversation)

        # measure how long it takes to complete
        start_time_seconds = start_time_seconds if start_time_seconds is not None else time.time()

        # initial call will have a user question, but some calls will be to pass local function results back to chatgpt.
        conversation.add_user_question_to_messages_if_applicable(question)

        # get all messages in the conversation history to pass to chatgpt
        messages = conversation.get_messages_in_chatgpt_format()
        # print(f"sending messages: {messages}")

        # call chatgpt
        # response = self.openai_client.ChatCompletion.create(model=model, messages=messages, tools=self.tools)
        response = self.openai_client.chat.completions.create(
            model=model,
            messages=messages,
            tools=self.tools,
            stream=False, # Whether to stream the response or return the full response at once
            # max_tokens=8000,  # The maximum number of tokens to generate in the completion
            # temperature=0.5,  # The temperature of the model, controlling the randomness of the output
            # top_p=1.0,  # The nucleus sampling parameter, controlling the diversity of the output
            # n=1,  # The number of completions to generate
            # # stop=None,  # A list of stop sequences to stop the completion at
            # stop=None,
            # presence_penalty=0.0,  # The penalty for generating tokens that appear in the prompt
            # frequency_penalty=0.0,  # The penalty for generating tokens that appear frequently in the prompt
            # logit_bias={},  # A dictionary of token IDs and associated biases to apply to the logits
        )
        # print(response)

        # add the response to our conversation.  we may need to pass it back to chatgpt if a function is called.
        conversation.add_chatgpt_response_to_messages(response)

        # call local functions
        # the results of all called functions will be stored in metadata.content
        functions_details = self.call_appropriate_function_based_on_llm_response(response)
        # add response of local functions to messages and recursively call chatgpt again so the response is passed.
        if functions_details is not None:
            conversation.add_functions_details_as_messages_in_conversation(functions_details)
            # print('recursively calling inference to pass back the results of the functions called')
            return self.inference(question=None, conversation=conversation, start_time_seconds=start_time_seconds)

        # return the answer as text
        return self.handle_chatgpt_completed_response(response, conversation, start_time_seconds)

    # If chatgpt response with 'stop', print out the answer and return it.
    def handle_chatgpt_completed_response(self, response, conversation, start_time_seconds):
        if self.get_finish_reason_from_chatgpt_response(response) == 'stop':
            last_message = conversation.get_last_message()
            # print(f"chatgpt response: \n {last_message.message_text}")
            # print(f"answer received in {time.time() - start_time_seconds} seconds.")
            return last_message.message_text

    # Help determine if chatgpt has completed "stop"
    def get_finish_reason_from_chatgpt_response(self, response):
        choices = response.choices # response['choices']
        choice = choices[0]
        finish_reason = choice.finish_reason # choice['finish_reason']
        return finish_reason

    def ensure_conversation_exists(self, conversation: Conversation):
        if conversation is None:
            conversation = Conversation(conversation_id=str(uuid.uuid4()), system_prompt=system_prompt)
        return conversation

    # Evaluates the chatgpt response and determines if a local function should be called.
    # If so, finds the appropriate service to call and stores the result of the function call in the function_details.
    def call_appropriate_function_based_on_llm_response(self, response):
        # determine if chatgpt is asking to call any local functions
        # functions = get_function_calls_details_from_llm_response(llm_response)
        functions = FunctionDetailsFactory.create_function_details_from_chatgpt_response(response)
        if functions is None:
            return None

        # call each local function chatgpt has asked to call.
        # store the result of the function into function_details.function_result
        for function_details in functions:
            function_name = function_details.function_name
            arguments = function_details.arguments

            if self.callable_function_service.does_function_exist(function_name):
                # print(f'calling function: {function_name}')
                function_result = self.callable_function_service.call_function(function_name=function_name, arguments=arguments)
                function_details.function_result = function_result

        return functions
