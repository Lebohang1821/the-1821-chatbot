# 1821 Chatbot

The 1821 Chatbot is an AI-powered coding assistant built using Streamlit and the Gemini API. It helps with debugging, code documentation, and solution design.

## Features

- 🐍 Python Expert
- 🐞 Debugging Assistant
- 📝 Code Documentation
- 💡 Solution Design

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/the-1821-chatbot.git
    ```
2. Navigate to the project directory:
    ```bash
    cd the-1821-chatbot
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Set the API key in your environment:
```bash
export GEMINI_API_KEY="your-api-key-here"
```

For better security, use a `.env` file and load it with `python-dotenv`:
1. Create a `.env` file in the project directory:
    ```plaintext
    GEMINI_API_KEY=your-api-key-here
    ```
2. Install `python-dotenv`:
    ```bash
    pip install python-dotenv
    ```
3. Load the environment variables in your `main.py`:
    ```python
    from dotenv import load_dotenv
    load_dotenv()
    ```

## Usage

Run the Streamlit app on `localhost:3000`:
```bash
streamlit run main.py --server.port 3000
```

## Credits

Built with [Joshua1821](https://joshua-chikasha.me/)