
import re

from eras.agents.simple_llm import SimpleLLM
from eras.config.config import config
from eras.services.shell_command_service import ShellCommandService
import openai

from eras.services.user_config_service import UserConfigService
import httpx

class UserCommandService:
    def __init__(self):
        self.openai_client = openai.OpenAI(
            base_url=config.get_eras_base_url(),
            api_key=config.get_eras_open_ai_key()
        )
        self.shell_command_service = ShellCommandService(self.openai_client)
        self.simple_llm = SimpleLLM(self.openai_client)
        self.user_config_service = UserConfigService()

    def handle_request(self, user_input: str):
        if user_input.startswith("/help"):
            self.handle_help_request(user_input)
        elif user_input.startswith("/chat"):
            self.handle_chat_request(user_input)
        elif user_input.startswith("/config"):
            self.handle_config_request(user_input)
        else:
            self.handle_shell_nli_request(user_input)

    def handle_help_request(self, user_input):
        self.user_config_service.print_eras_logo()
        self.user_config_service.show_commands()

    def handle_chat_request(self, user_input):
        match = re.match(r'^/chat\s+(.*)', user_input)
        prompt = match.group(1) if match else None

        def handle_text_received(text):
            print(text, end="")

        def handle_response_complete():
            print()

        self.simple_llm.stream_inference(prompt, handle_text_received, handle_response_complete)


    def handle_shell_nli_request(self, user_input):
        self.shell_command_service.handle_prompt(user_input)

    def handle_config_request(self, user_input):
        self.user_config_service.prompt_for_all_configs()

