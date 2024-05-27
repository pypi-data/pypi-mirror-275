# Repartee

Repartee is a command-line interface (CLI) tool designed to interface with multiple AI APIs to handle various functionalities, including sending prompts and receiving responses from AI models. It tracks spending based on token usage and offers a flexible configuration system.

## Core Functionality
- Interface with multiple AI APIs (GPT-4o, GPT-4-turbo, GPT-3.5-turbo from OpenAI, Claude 3, Gemini 1.5, Perplexity).
- Securely store API keys in environment variables.
- Configure API parameters such as max tokens and temperature.
- Support YAML configuration files for settings.
- Command-line argument parsing for API selection and prompt input.
- Output formatting options (standard output, file, REPL).
- Interactive REPL prompt.
- Input from files and shell command piping.
- Advanced features like error handling, retry mechanisms, and spending tracking.

## Project Structure
```
repartee/
│
├── repartee/
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   ├── api_clients/
│   │   ├── __init__.py
│   │   ├── openai_api.py
│   │   ├── claude3.py
│   │   ├── gemini15.py
│   │   └── perplexity.py
│   ├── prompt_handler.py
│   ├── output_formatter.py
│   ├── repl.py
│   ├── spending_tracker.py
│   └── utils.py
│
├── tests/
│   ├── __init__.py
│   ├── test_cli.py
│   ├── test_config.py
│   ├── test_api_clients.py
│   ├── test_prompt_handler.py
│   ├── test_output_formatter.py
│   ├── test_repl.py
│   └── test_spending_tracker.py
│
├── .gitignore
├── README.md
├── setup.py
└── requirements.txt
```

## Key Components

1. **cli.py**: Handles command-line argument parsing and routes the inputs to the appropriate API client.
2. **config.py**: Manages loading and accessing configuration settings from YAML files.
3. **api_clients/openai_api.py**: Contains functions to interact with OpenAI's GPT models, including checking API key availability and making API requests.
4. **output_formatter.py**: Formats the AI responses into markdown format suitable for Obsidian, with specific callout blocks for system and user messages.
5. **spending_tracker.py**: Tracks token usage and calculates spending based on the model's token cost.
6. **repl.py**: Provides an interactive Read-Eval-Print Loop (REPL) for live prompt-response sessions.

## Roadmap

- [x] Set up the initial project structure
- [x] Implement CLI argument parsing
- [x] Implement configuration management
- [x] Implement OpenAI API client
- [ ] Implement Claude 3 API client
- [ ] Implement Gemini 1.5 API client
- [ ] Implement Perplexity API client
- [x] Implement basic output formatting
- [ ] Implement spending tracker
- [ ] Implement REPL interface
- [ ] Write tests for CLI
- [ ] Write tests for configuration management
- [ ] Write tests for API clients
- [ ] Write tests for prompt handler
- [ ] Write tests for output formatter
- [ ] Write tests for REPL
- [ ] Write tests for spending tracker
