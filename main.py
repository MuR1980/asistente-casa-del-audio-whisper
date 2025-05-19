
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

@app.route("/transcribe", methods=["POST"])
def transcribe():
    audio = request.files["audio"]
    transcript = openai.Audio.transcribe("whisper-1", audio)
    return jsonify({ "transcript": transcript["text"] })

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            { "role": "system", "content": "Sos un asistente de ventas de Casa del Audio." },
            { "role": "user", "content": user_message }
        ]
    )
    reply = completion.choices[0].message["content"]
    return jsonify({ "reply": reply })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
