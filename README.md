# AI Code Assistant

An intelligent code completion and assistance tool built with Streamlit, OpenAI, and Python.

## Features

- User authentication (login, signup, password reset)
- Code editor with syntax highlighting
- AI-powered code suggestions
- Real-time code quality rating
- Interactive coding assistant chatbot
- Resource recommendations
- Code execution and output display

## Prerequisites

- Python 3.8 or higher
- MySQL Server
- OpenAI API key

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd ai-code-assistant
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up the database:

   - Create a MySQL database named `code_assistant`
   - Update the `.env` file with your database credentials

5. Create a `.env` file:

```bash
cp .env.template .env
```

Edit the `.env` file with your credentials:

- Database configuration
- OpenAI API key

## Running the Application

1. Start the MySQL server if it's not running

2. Run the application:

```bash
streamlit run app.py
```

3. Open your browser and navigate to `http://localhost:8501`

## Usage

1. Create an account or login with existing credentials
2. Navigate to the Code Editor
3. Start writing Python code
4. Use the various features:
   - Get AI suggestions for code completion
   - Run your code
   - Chat with the AI assistant
   - Get resource recommendations
   - View code quality ratings

## Security Notes

- Passwords are securely hashed using bcrypt
- API keys and sensitive information are stored in environment variables
- Code execution is done in a safe environment

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
