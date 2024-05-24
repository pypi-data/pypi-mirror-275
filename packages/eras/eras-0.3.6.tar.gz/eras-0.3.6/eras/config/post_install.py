import os
import sys
import subprocess

def alias_exists(alias_name):
    home = os.path.expanduser("~")
    shell_config_files = [".bashrc", ".zshrc", ".bash_profile"]

    for config_file in shell_config_files:
        config_path = os.path.join(home, config_file)
        if os.path.exists(config_path):
            with open(config_path, "r") as file:
                if alias_name in file.read():
                    return True
    return False

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
                    if var_name in file.read():
                        return True
        return False

# def refresh_windows_environment_variables():
#     # Refresh user environment variables
#     user_vars = os.popen('powershell -Command "[System.Environment]::GetEnvironmentVariables(\'User\')"').read()
#     for line in user_vars.splitlines():
#         if '=' in line:
#             key, value = line.split('=', 1)
#             os.environ[key.strip()] = value.strip()
#
#     # Refresh system environment variables
#     system_vars = os.popen('powershell -Command "[System.Environment]::GetEnvironmentVariables(\'Machine\')"').read()
#     for line in system_vars.splitlines():
#         if '=' in line:
#             key, value = line.split('=', 1)
#             os.environ[key.strip()] = value.strip()

def add_env_var_to_shell(env_var_command):
    if os.name == 'nt':  # Windows
        print('setting windows shell env var')
        var_name, var_value = env_var_command.split('=', 1)
        os.system(f'setx {var_name} {var_value}')
        # Set the environment variable persistently using setx
        # subprocess.run(['setx', var_name, var_value], check=True)

    else:  # Unix-based systems
        home = os.path.expanduser("~")
        shell_config_files = [".bashrc", ".zshrc", ".bash_profile"]

        for config_file in shell_config_files:
            config_path = os.path.join(home, config_file)
            if os.path.exists(config_path):
                with open(config_path, "a") as file:
                    file.write(f"\nexport {env_var_command}\n")

def ensure():
    if not env_var_exists("ERAS_OPENAI_KEY"):
        openai_key = input("Please enter your OpenAI API key (ERAS_OPENAI_KEY): ").strip()
        if not openai_key:
            print("Error: OpenAI API key cannot be empty.")
            sys.exit(1)
        env_var_command = f"ERAS_OPENAI_KEY={openai_key}"
        os.environ['ERAS_OPENAI_KEY'] = openai_key
        add_env_var_to_shell(env_var_command)
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
            raise ValueError("Unsupported shell type")

def reload_profile(profile_file):
    if os.name != 'nt':  # Unix-based systems
        shell = os.environ.get('SHELL', '')
        if 'zsh' in shell:
            subprocess.run(['zsh', '-c', f'source {profile_file}'], check=True)
        elif 'bash' in shell:
            subprocess.run(['bash', '-c', f'source {profile_file}'], check=True)
        else:
            print(f"Please manually source your profile file: {profile_file}")
    else:
        print("Please restart your Command Prompt or PowerShell session to apply the changes.")

if __name__ == "__main__":
    ensure()
