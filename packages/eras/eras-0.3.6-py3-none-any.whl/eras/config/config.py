import os
import platform

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    def get_open_ai_key(self):
        return os.getenv('OPEN_AI_KEY')

    def get_eras_open_ai_key(self):
        return os.getenv('ERAS_OPENAI_KEY')

    def get_eras_base_url(self):
        return os.getenv('ERAS_BASE_URL')

    def get_model_name(self):
        return "gpt-3.5-turbo"

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
