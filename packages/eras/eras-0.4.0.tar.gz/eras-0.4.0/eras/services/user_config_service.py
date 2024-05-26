from InquirerPy import prompt
from InquirerPy.base.control import Choice
import os
import sys
from eras.utils.env_vars_and_profile_files import env_var_exists, reload_profile, get_profile_file, set_env_var
from eras.models.constants import ERAS_OPENAI_KEY_ENV_VAR_NAME, ERAS_HAS_RUN_INITIAL_CONFIG_VAR_NAME, ERAS_MODEL_ENV_VAR_NAME, ERAS_BASE_URL_ENV_VAR_NAME
from eras.config.config import config

class UserConfigService:
    # def __init__(self):
    #     print('init')

    def ensure_needed_configs_are_set(self):
        if not env_var_exists(ERAS_HAS_RUN_INITIAL_CONFIG_VAR_NAME):
            print('WELCOME TO ERAS!!')
            self.prompt_for_all_configs(should_reload_profile=False)
            set_env_var(ERAS_HAS_RUN_INITIAL_CONFIG_VAR_NAME, "true")
            self.reload_prof()

    def prompt_for_all_configs(self, should_reload_profile=True):
        openai_key_value = config.get_eras_open_ai_key() if config.get_eras_open_ai_key() is not None else ""
        model_name_value = config.get_model_name() if config.get_model_name() is not None else ""
        base_url_value = config.get_eras_base_url() if config.get_eras_base_url() is not None else ""
        # print(f"base_url is {base_url_value}")

        openai_key_question = {"type": "input", "message": "OpenAI key (or local llama key). Cannot be blank! :", "name": "openai_key_value", "default": openai_key_value}
        model_name_question = {"type": "input", "message": "Enter which model to use. e.g. Llama-3 or https://platform.openai.com/docs/models/gpt-4o :", "name": "model_name_value", "default": model_name_value}
        base_url_question = {"type": "input", "message": "(Optional) Enter alternative base url (defaults to openai). (llama.cpp is http://127.0.0.1:8080) :  ", "name": "base_url_value", "default": base_url_value}

        questions = [
            openai_key_question,
            model_name_question,
            base_url_question
        ]

        result = prompt(questions)
        new_base_url_value = result["base_url_value"]
        new_model_name_value = result["model_name_value"]
        new_openai_key_value = result["openai_key_value"]

        set_env_var(ERAS_OPENAI_KEY_ENV_VAR_NAME, new_openai_key_value)
        set_env_var(ERAS_MODEL_ENV_VAR_NAME, new_model_name_value)
        set_env_var(ERAS_BASE_URL_ENV_VAR_NAME, new_base_url_value)
        # if new_base_url_value is not "":
        #     set_env_var(ERAS_BASE_URL_ENV_VAR_NAME, new_base_url_value)
        if should_reload_profile:
            self.reload_prof()

    def reload_prof(self):
        """NOTE: Reloading profile will immediately stop execution"""
        if os.name != 'nt':  # Unix-based systems
            print('reloading profile')
            reload_profile(get_profile_file())
        else:
            print('======= PLEASE CLOSE THIS TERMINAL WINDOW AND OPEN A NEW ONE =========')
