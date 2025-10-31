# Groq Chatbot

This is a simple chatbot application that uses the Groq API and is built with Flask. It uses ngrok to create a public URL for the chatbot.

## Prerequisites

*   Python 3.6+
*   pip

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Chatbot

1.  **Run the Flask application:**
    ```bash
    python app.py
    ```

2.  When you run the application, you will see an ngrok URL printed in the console. It will look something like this:
    ```
     * ngrok tunnel "https://<unique-id>.ngrok.io" -> "http://127.0.0.1:5000"
    ```

3.  Open this URL in your web browser to interact with the chatbot.

## How it Works

This application uses:
*   **Flask** as the web framework.
*   **Groq** for the AI chat model.
*   **ngrok** to create a secure, public URL to the Flask application running on your local machine.
*   **Marked.js** to render the chatbot's Markdown responses in the browser.
