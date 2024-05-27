import os
import platform
from eras.models.constants import OPENAI_MODEL_DEFAULT, ERAS_MODEL_ENV_VAR_NAME, ERAS_OPENAI_KEY_ENV_VAR_NAME, ERAS_BASE_URL_ENV_VAR_NAME
import uuid
class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    def get_google_analytics_measurement_id(self):
        return 'G-E13DKQSHRK'

    def get_google_analytics_secret(self):
        return 'F2UoThnPR2qKCisNZi20bQ'

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

    def get_system_identifier(self):
        try:
            # Get the operating system details
            os_name = platform.system()  # e.g., 'Windows', 'Linux', 'Darwin'
            os_version = platform.version()  # e.g., '10.0.19042', '#59-Ubuntu SMP Wed Oct 10 14:51:03 UTC 2018'

            # Get a hardware-based UUID
            # uuid.getnode() can sometimes return a random value if it cannot access the hardware address
            node = uuid.getnode()
            if (node >> 40) % 2:
                hw_uuid = str(uuid.uuid4())  # Random UUID if getnode() is not reliable
            else:
                hw_uuid = hex(node)  # Hardware-based UUID

            # Get the current user
            user = os.getlogin()  # e.g., 'johndoe'

            # Combine all parts to form a unique identifier
            system_id = f"{os_name}-{os_version}-{hw_uuid}-{user}"

            return system_id

        except Exception as e:
            # Handle exceptions gracefully
            return f"Unknown"

config = Config()
