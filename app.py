
import os
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

@app.route("/")
def home():
    return "JARVIS AI is online, Sir!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    if not message.strip():
        return jsonify({"reply": "Please give me a command, Sir."}), 400

    try:
        response = client.responses.create(
            model="gpt-5.5",
            instructions=(
                "You are JARVIS, a sophisticated personal AI "
                "assistant. Address the user respectfully as Sir. "
                "Be intelligent, helpful and concise."
            ),
            input=message
        )

        return jsonify({"reply": response.output_text})

    except Exception:
        return jsonify({
            "reply": "I am having trouble connecting to my AI brain, Sir."
        }), 500

if __name__ == "__main__":
    app.run()
