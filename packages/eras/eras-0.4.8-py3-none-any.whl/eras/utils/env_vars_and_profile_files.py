import os
import sys
import subprocess
import re

def env_var_exists(var_name):
    if os.name == 'nt':  # Windows
        return os.getenv(var_name) is not None
    else:  # Unix-based systems
        home = os.path.expanduser("~")
        shell_config_files = [".bashrc", ".zshrc", ".bash_profile"]

        for config_file in shell_config_files:
            config_path = os.path.join(home, config_file)
            if os.path.exists(config_path):
                with open(config_path, "r") as file:
                    # print(file.read())
                    # print(f'{var_name} is in file? : {var_name in file.read()}')
                    if var_name in file.read():
                        # print(file.read())
                        # print(f'{var_name} is in {file.read()} {config_path}')
                        return True
        return False

def set_env_var(env_var_name, value):
    env_var_command = f"{env_var_name}={value}"
    print(f"setting env var: {env_var_command}")
    os.environ[env_var_name] = value
    set_env_var_to_shell(env_var_command)

def set_env_var_to_shell(env_var_command):
    if os.name == 'nt':  # Windows
        print('setting windows shell env var')
        var_name, var_value = env_var_command.split('=', 1)
        os.system(f'setx {var_name} {var_value}')

    else:  # Unix-based systems
        home = os.path.expanduser("~")
        shell_config_files = [".bashrc", ".zshrc", ".bash_profile"]
        var_name, var_value = env_var_command.split('=', 1)
        export_command = f"export {env_var_command}"

        for config_file in shell_config_files:
            config_path = os.path.join(home, config_file)
            if os.path.exists(config_path):
                with open(config_path, "r") as file:
                    lines = file.readlines()

                with open(config_path, "w") as file:
                    var_found = False
                    for line in lines:
                        if re.match(f"^export {var_name}=", line):
                            file.write(f"{export_command}\n")
                            var_found = True
                        else:
                            file.write(line)
                    if not var_found:
                        file.write(f"\n{export_command}\n")

def ensure():
    if not env_var_exists("ERAS_OPENAI_KEY"):
        openai_key = input("Please enter your OpenAI API key (ERAS_OPENAI_KEY): ").strip()
        if not openai_key:
            print("Error: OpenAI API key cannot be empty.")
            sys.exit(1)
        env_var_command = f"ERAS_OPENAI_KEY={openai_key}"
        os.environ['ERAS_OPENAI_KEY'] = openai_key
        set_env_var_to_shell(env_var_command)
        print("Environment variable 'ERAS_OPENAI_KEY' added to environment.")

        if os.name != 'nt':  # Unix-based systems
            reload_profile(get_profile_file())
        else:
            print('======= PLEASE CLOSE THIS TERMINAL WINDOW AND OPEN A NEW ONE =========')

def get_profile_file():
    if os.name == 'nt':  # Windows
        return None  # No equivalent profile file
    else:  # Unix-based systems
        shell = os.environ.get('SHELL', '')
        if 'zsh' in shell:
            return os.path.expanduser('~/.zshrc')
        elif 'bash' in shell:
            bash_profile = os.path.expanduser('~/.bash_profile')
            if os.path.exists(bash_profile):
                return bash_profile
            else:
                return os.path.expanduser('~/.bashrc')
        else:
            print("Unsupported shell type.  Close this terminal windows and open a new one.")

def reload_profile(profile_file):
    if os.name != 'nt':  # Unix-based systems
        shell = os.environ.get('SHELL', '')
        if 'zsh' in shell:
            os.execvp('zsh', ['zsh', '-c', f'source {profile_file} && exec zsh'])
        elif 'bash' in shell:
            os.execvp('bash', ['bash', '-c', f'source {profile_file} && exec bash'])
        else:
            print(f"Please manually source your profile file: {profile_file}")
    else:
        print("Please restart your Command Prompt or PowerShell session to apply the changes.")

if __name__ == "__main__":
    ensure()
