# Groq Chatbot

This is a simple chatbot application that uses the Groq API and is built with Flask.

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

## Configuration

You need to have a Groq API key to use this application.

1.  Get your API key from the [Groq console](https://console.groq.com/keys).

2.  Set the API key as an environment variable. You can do this by creating a `.env` file in the root of the project with the following content:
    ```
    GROQ_API_KEY=your-groq-api-key
    ```
    The application will automatically load this environment variable.

## Running Locally

1.  **Set the Groq API key:**
    Make sure you have set your `GROQ_API_KEY` environment variable as described in the "Configuration" section.

2.  **Run the Flask application:**
    ```bash
    export FLASK_APP=app.py
    flask run
    ```
    Alternatively, you can run:
    ```bash
    python app.py
    ```

3.  Open your web browser and go to `http://127.0.0.1:5000` to see the chatbot in action.

## Deployment

To make your chatbot accessible online, you can deploy it to a cloud platform like Heroku, Render, or any other platform that supports Python/WSGI applications.

The general steps for deployment are:

1.  **Create a `gunicorn` dependency:** Add `gunicorn` to your `requirements.txt` file. Gunicorn is a production-ready WSGI server.
2.  **Create a `Procfile`:** This file tells the deployment platform how to run your application. It should contain a line like this:
    ```
    web: gunicorn app:app
    ```
3.  **Connect your GitHub repository to the deployment platform:** Most platforms have an option to connect your GitHub account and deploy directly from a repository.
4.  **Set the `GROQ_API_KEY` environment variable** in the platform's settings.

This will make your chatbot live on the internet. Note that GitHub itself does not host and run Python applications directly; it only stores the code. You need a separate hosting service to run the chatbot.
