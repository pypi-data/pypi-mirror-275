# ERAS
Easily Runnable AI Shell allows you to run shell commands using natural language.   

No more having to leave the terminal to look up how to run a command!

Eras works on Windows, Mac, and Linux!

Eras works with OpenAI, or any model exposed via an OpenAI spec compliant server, such as Llama.cpp server!

# Demo
[Eras Demo](https://youtu.be/T7KRDwi5HDo)

[![Video Thumbnail](https://img.youtube.com/vi/T7KRDwi5HDo/0.jpg)](https://youtu.be/T7KRDwi5HDo)

# Install

## Mac & Linux
```
pip install eras
```

If you get an error about externally-managed-environment it's because you have python installed via homebrew, and need to use pipx instead:

pipx
``` 
brew install pipx
pipx ensurepath
pipx install eras
```
With pipx you may need to open a new terminal window or source .zshrc a couple of times.

## Windows
```
pip install eras
```

You will be prompted for various configuration settings.  Once set, close your terminal window and open up a new one.
# Use
The first use of Eras will prompt you to enter various configs. See the Config Examples section below.

The first use will also prompt you to allow accessibility features for Terminal.app, which is required to allow Eras to populate
the terminal with the shell command.

![img.png](https://i.imgur.com/y3OLDuG.png)


When you ask Eras a question, it will use AI to create a shell command, then populate your next terminal line with the command, so all you have to do is review and press enter.

## Usage Examples
```
% eras list all files in the current directory

ERAS will then populate the next terminal line with the command:
% ls

All you have to do is confirm and hit enter!

...
% eras create a new file named jason.txt with contents "hello world"
% echo "hello world" > jason.txt
...

```
### Chat Examples
```
% eras /chat What is the capital of France 
% Paris is the capital of France

Note: if you want to use ? or other special terminal chars you should surround your question in quotes
% eras /chat "What is the capital of France?"
% Paris is the capital of France
```

### Config Examples
On the first run of eras, you will be prompted to enter config values, which are saved as env vars.

To run the config again, you can run `eras /config`

An API key must be provided when using OpenAI or Llama.cpp (can be anything unless you explicitly set one in Llama.cpp)

#### OpenAI
For OpenAI you must provide:
- API Key - Grab an OpenAI key from [here](https://platform.openai.com/api-keys)
- Model name - (defaults to gpt-4) Find any valid one [here](https://platform.openai.com/docs/models)

#### Alternative OpenAI Server (e.g. Llama.cpp server)
You will be prompted to enter the alternative base url. e.g. `http://127.0.0.1:8080`

## Llama.cpp Setup Instructions
Find the server setup instructions at: https://github.com/ggerganov/llama.cpp

##### NVIDIA GPU Instructions
If you are running a NVIDIA GPU, you will want to build the llama server with CUDA enabled, as outlined [here](https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#cuda)

I followed [these instructions](https://medium.com/@michaelhumor/how-to-build-llama-cpp-on-windows-with-nvidia-gpu-226a28069a76):

- Download Visual Studio and install CMake tools
  - Go to https://visualstudio.microsoft.com/downloads/ and download “Visual Studio 2022 (Community)”
- Open VisualStudioSetup.exe to install Visual Studio
- Select Desktop development with C++ to install CMake tools

- Download a gguf model:
  - e.g. https://huggingface.co/MaziyarPanahi/Llama-3-8B-Instruct-32k-v0.1-GGUF/blob/main/Llama-3-8B-Instruct-32k-v0.1.Q4_K_M.gguf

Run these commands in Developer Command Prompt (search Windows and it'll come up)

```
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
mkdir build
cd build
cmake .. -DLLAMA_CUDA=ON
cmake --build . --config Release
```

Start the Llama server:
``` 
.\bin\Release\server.exe -m C:\shared-drive\llm_models\Llama-3-8B-Instruct-32k-v0.1.Q4_K_M.gguf -ngl 9999 --host 0.0.0.0 --ctx-size 32000
```
# Upcoming functionality

## Llama 3 support
Llama.cpp provides an API similar to OpenAI, so pointing eras at http://127.0.0.1:8080 works as expected.  

I just need to prompt for the base_url preference and use it.

