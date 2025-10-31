# AI Chatbot with Groq & Flask

This is a modern, AI-powered chatbot application built with Flask and the Groq API. It features a sleek, animated UI and is designed to be run securely.

## Features
- **Modern UI:** A beautiful dark theme with gradients, animations, and a "typing" indicator.
- **AI-Powered:** Uses the powerful `mixtral-8x7b-32768` model from Groq for intelligent responses.
- **Secure:** Loads API keys from environment variables to protect your sensitive credentials.
- **Accessible:** Uses `ngrok` to create a temporary public URL, making it easy to test and share.

## 1. Important Security Configuration

To run this application, you must provide two secret keys as **environment variables**. Hardcoding keys is a major security risk, as it can expose them publicly.

You will need:
- A **Groq API Key**: Get one from the [Groq Console](https://console.groq.com/keys).
- An **ngrok Authtoken**: Get one from the [ngrok Dashboard](https://dashboard.ngrok.com/get-started/your-authtoken).

### How to Set Environment Variables

**On macOS/Linux:**
Open your terminal and run these commands before starting the app:
```bash
export GROQ_API_KEY="your_groq_api_key_here"
export NGROK_AUTHTOKEN="your_ngrok_authtoken_here"
```

**On Windows:**
Use these commands in Command Prompt:
```cmd
set GROQ_API_KEY="your_groq_api_key_here"
set NGROK_AUTHTOKEN="your_ngrok_authtoken_here"
```

## 2. Installation & Running the Chatbot

Once your environment variables are set, you can run the chatbot.

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\\Scripts\\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python app.py
    ```
    If your keys are set correctly, the app will start and print a public `ngrok` URL. Open this URL in your browser to use the chatbot.
