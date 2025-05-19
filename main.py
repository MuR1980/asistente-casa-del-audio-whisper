
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

@app.route("/transcribe", methods=["POST"])
def transcribe():
    audio_file = request.files["audio"]
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file.stream  # ✅ solución correcta
    )
    return jsonify({ "transcript": transcript.text })

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            { "role": "system", "content": "Sos un asistente de ventas de Casa del Audio." },
            { "role": "user", "content": user_message }
        ]
    )
    reply = response.choices[0].message.content
    return jsonify({ "reply": reply })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
