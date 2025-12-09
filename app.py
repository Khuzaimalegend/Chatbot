
import os
from flask import Flask, render_template, request, jsonify
from groq import Groq
from pyngrok import ngrok

app = Flask(__name__)

# --- Load API Keys from Environment Variables ---
groq_api_key = os.environ.get("GROQ_API_KEY")
ngrok_authtoken = os.environ.get("NGROK_AUTHTOKEN")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY environment variable not set. Get one from https://console.groq.com/keys")

client = Groq(api_key=groq_api_key)

if ngrok_authtoken:
    ngrok.set_auth_token(ngrok_authtoken)
# ---------------------------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": user_message}
        ],
        model="mixtral-8x7b-32768",
    )

    bot_response = chat_completion.choices[0].message.content
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    # Disconnect any existing ngrok tunnels to prevent session conflicts
    try:
        ngrok.kill()
    except Exception as e:
        print(f"No existing ngrok processes to kill or an error occurred: {e}")

    # Connect to ngrok and create a public URL
    if ngrok_authtoken:
        try:
            public_url = ngrok.connect(5000)
            print(f" * ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:5000\"")
            app.run()
        except Exception as e:
            print(f"Error starting ngrok tunnel: {e}")
            print("ngrok tunnel failed. Running on localhost only.")
            app.run(port=5000)
    else:
        print("NGROK_AUTHTOKEN not set. Running on localhost only.")
        app.run(port=5000)
