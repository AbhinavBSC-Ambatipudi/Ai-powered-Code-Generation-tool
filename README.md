# AI-powered Code Generation Tool

A Python tool that uses OpenAI's GPT models and LangChain to generate code solutions based on natural language prompts.

## Overview

This project demonstrates the integration of OpenAI's language models with LangChain's agent framework to create an AI assistant capable of writing Python code. The tool takes natural language instructions and uses a Python REPL (Read-Eval-Print Loop) to write, test, and refine the code in real time.

## Features

- Natural language to code translation
- Uses OpenAI's GPT-4o-mini model for code generation
- Interactive Python REPL for code execution
- Verbose output showing the AI's reasoning process
- Support for various programming problems

## Prerequisites

- Python 3.6+
- OpenAI API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ai-powered-code-generation-tool.git
   cd ai-powered-code-generation-tool
   ```

2. Install the required packages:
   ```
   pip install langchain openai langchain_experimental
   ```

3. Make sure you're using the compatible version of OpenAI:
   ```
   pip install openai==0.28
   ```

## Usage

1. Replace the OpenAI API key in the code with your own key:
   ```python
   os.environ["OPENAI_API_KEY"] = 'your-api-key-here'
   ```

2. Run the script:
   ```
   python main.py
   ```

3. Modify the agent.invoke() call with your own programming problem:
   ```python
   response = agent.invoke("Your programming problem here")
   ```

## Example

The current example in the code generates a Python program to print the Fibonacci series using a recursive method.

## Configuration

You can customize the following parameters:
- `temperature`: Controls randomness in the model's output (0 = deterministic)
- `model_name`: The OpenAI model to use
- `max_tokens`: Maximum number of tokens in the response

```python
llm=OpenAI(temperature=0, model_name="gpt-4o-mini", max_tokens=1000)
```

## Advanced Usage

The tool supports various types of coding tasks including:
- Algorithm implementation
- Data structure operations
- Mathematical problems
- Simple application development

## Security Note

- Never commit your API keys to version control
- Consider using environment variables or a secure configuration manager

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain) for the agent framework
- [OpenAI](https://openai.com/) for the language models
