# Shell-AI: let AI write your shell commands

[![PyPI version](https://badge.fury.io/py/shell-ai.svg)](https://pypi.org/project/shell-ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Forks](https://img.shields.io/github/forks/ricklamers/shell-ai)](https://github.com/ricklamers/shell-ai/network)
[![Stars](https://img.shields.io/github/stars/ricklamers/shell-ai)](https://github.com/ricklamers/shell-ai/stargazers)


Shell-AI (`shai`) is a CLI utility that brings the power of natural language understanding to your command line. Simply input what you want to do in natural language, and `shai` will suggest single-line commands that achieve your intent. Under the hood, Shell-AI leverages the [LangChain](https://github.com/langchain-ai/langchain) for LLM use and builds on the excellent [InquirerPy](https://github.com/kazhala/InquirerPy) for the interactive CLI.

![demo-shell-ai](https://github.com/ricklamers/shell-ai/assets/1309307/b4057165-5c23-46d4-b68e-00915b738dc3)

## Installation

You can install Shell-AI directly from PyPI using pip:

```bash
pip install shell-ai
```

Note that on Linux, Python 3.10 or later is required.

After installation, you can invoke the utility using the `shai` command.

## Usage

To use Shell-AI, open your terminal and type:

```bash
shai run terraform dry run thingy
```

Shell-AI will then suggest 3 commands to fulfill your request:
- `terraform plan`
- `terraform plan -input=false`
- `terraform plan`

## Features

- **Natural Language Input**: Describe what you want to do in plain English (or other supported languages).
- **Command Suggestions**: Get single-line command suggestions that accomplish what you asked for.
- **Cross-Platform**: Works on Linux, macOS, and Windows.
- **Azure Compatibility**: Shell-AI now supports Azure OpenAI deployments.

## Configuration
### Environment Variables

1. **`OPENAI_API_KEY`**: Required. Set this environment variable to your OpenAI API key. You can find it on your [OpenAI Dashboard](https://beta.openai.com/account/api-keys).

### Optional Variables

1. **`OPENAI_MODEL`**: Defaults to `gpt-3.5-turbo`. You can set it to another OpenAI model if desired.
2. **`OPENAI_MAX_TOKENS`**: Defaults to `None`. You can set the maximum number of tokens that can be generated in the chat completion.
3. **`SHAI_SUGGESTION_COUNT`**: Defaults to 3. You can set it to specify the number of suggestions to generate.
4. **`OPENAI_API_BASE`**: Defaults to `https://api.openai.com/v1`. You can set it to specify the proxy or service emulator.
5. **`OPENAI_ORGANIZATION`**: OpenAI Organization ID
6. **`OPENAI_PROXY`**: OpenAI proxy
7. **`OPENAI_API_TYPE`**: Set to "azure" if you are using Azure deployments.
8. **`AZURE_DEPLOYMENT_NAME`**: Your Azure deployment name (required if using Azure).
9. **`AZURE_API_BASE`**: Your Azure API base (required if using Azure).
10. **`CTX`**: Allow the assistant to keep the console outputs as context allowing the LLM to produce more precise outputs. ***IMPORTANT***: the outputs will be sent to OpenAI through their API, be careful if any sensitive data. Default to false.

You can also enable context mode in command line with `--ctx` flag:

```bash
shai --ctx [request]
```

### Configuration File

Alternatively, you can store these variables in a JSON configuration file:

- For Linux/macOS: Create a file called `config.json` under `~/.config/shell-ai/` and secure it with `chmod 600 ~/.config/shell-ai/config.json`.
- For Windows: Create a file called `config.json` under `%APPDATA%\shell-ai\`

Example `config.json`:

```json
{
  "OPENAI_API_KEY": "your_openai_api_key_here",
  "OPENAI_MODEL": "gpt-3.5-turbo",
  "SHAI_SUGGESTION_COUNT": "3",
  "CTX": true
}
```

The application will read from this file if it exists, overriding any existing environment variables.

Run the application after setting these configurations.


## Contributing

This implementation can be made much smarter! Contribute your ideas as Pull Requests and make AI Shell better for everyone.

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

Shell-AI is licensed under the MIT License. See [LICENSE](LICENSE) for details.
