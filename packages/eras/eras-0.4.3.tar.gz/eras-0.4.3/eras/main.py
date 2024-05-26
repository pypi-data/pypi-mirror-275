import argparse
import sys
import os
from dotenv import load_dotenv
load_dotenv()

from eras.services.user_command_service import UserCommandService
from eras.services.user_config_service import UserConfigService

# from eras.services.user_command_service import UserCommandService
def main():
    # print("main")
    user_config_service = UserConfigService()
    user_config_service.ensure_needed_configs_are_set()

    parser = argparse.ArgumentParser(description="AI Natural Language Interface for running shell commands")
    parser.add_argument('question', nargs='+', help='question or instruction to turn into a shell command')
    args = parser.parse_args()
    user_input = ' '.join(args.question)
    user_command_service = UserCommandService()
    user_command_service.handle_request(user_input)


if __name__ == "__main__":
    main()
