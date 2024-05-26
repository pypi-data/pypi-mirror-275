import os
import platform
from eras.models.constants import OPENAI_MODEL_DEFAULT, ERAS_MODEL_ENV_VAR_NAME, ERAS_OPENAI_KEY_ENV_VAR_NAME, ERAS_BASE_URL_ENV_VAR_NAME

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    def get_eras_open_ai_key(self):
        return os.getenv(ERAS_OPENAI_KEY_ENV_VAR_NAME)

    def get_eras_base_url(self):
        base_url = os.getenv(ERAS_BASE_URL_ENV_VAR_NAME)
        if base_url == "":
            return None
        return os.getenv(ERAS_BASE_URL_ENV_VAR_NAME)

    def get_model_name(self):
        return os.getenv(ERAS_MODEL_ENV_VAR_NAME, OPENAI_MODEL_DEFAULT)

    def get_user_operating_system(self):
        # return "System: Mac , macOS: Monterey, osVersion: 12.4"
        os_name = platform.system()
        os_version = platform.version()
        os_release = platform.release()

        if os_name == 'Windows':
            return f"{os_name} {os_release}"
        elif os_name == 'Darwin':
            mac_version, _, _ = platform.mac_ver()
            return f"macOS {mac_version}"
        elif os_name == 'Linux':
            try:
                # Try to get more detailed distribution info
                distro_info = platform.linux_distribution()
                if distro_info[0] and distro_info[1]:
                    return f"{distro_info[0]} {distro_info[1]}"
                else:
                    return f"Linux {os_release}"
            except AttributeError:
                # platform.linux_distribution() is removed in Python 3.8 and later
                return f"Linux {os_release}"
        else:
            return f"{os_name} {os_version}"


config = Config()
