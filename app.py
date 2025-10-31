
from flask import Flask, render_template, request, jsonify
from groq import Groq
from pyngrok import ngrok

app = Flask(__name__)

# Hardcoded Groq API key
groq_api_key = "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"

client = Groq(
    api_key=groq_api_key,
)

# Hardcoded ngrok authtoken
ngrok_authtoken = "2yDwhspkLWqMo2txVlyTj8ksAhR_7oxCzRQf9q26nusFo1zPY"
ngrok.set_auth_token(ngrok_authtoken)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": user_message,
        }
    ],
    model="llama3-8b-8192",
    )

    bot_response = chat_completion.choices[0].message.content
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    public_url = ngrok.connect(5000)
    print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:5000\"".format(public_url))
    app.run()
