
import os
from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

# Replace with your Groq API key
groq_api_key = os.environ.get("GROQ_API_KEY")


client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


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
    app.run(debug=True)
