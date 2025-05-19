
# Asistente Casa del Audio - Demo con Voz (Whisper + GPT)

Este proyecto es una demo funcional de un asistente virtual que permite grabar voz desde el navegador (incluido iPhone), transcribir con la API de Whisper de OpenAI y responder usando GPT-3.5 Turbo.

---

## 🚀 Funcionalidades

- 🎙 Grabación de voz compatible con iOS, Android y escritorio
- 🧠 Transcripción por inteligencia artificial (OpenAI Whisper)
- 🤖 Chat asistente con respuestas habladas (Text-to-Speech)
- 📱 Interfaz responsive con branding de Casa del Audio

---

## 📦 Archivos incluidos

- `index.html`: Interfaz web del asistente
- `main.py`: Servidor Flask que maneja transcripción y chat
- `requirements.txt`: Dependencias necesarias

---

## 🔧 Cómo desplegar en Render.com

1. Subí este proyecto a un repositorio (GitHub o GitLab)
2. Ingresá a [https://render.com](https://render.com)
3. Creá un **Web Service** y completá:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`

4. Agregá tu variable de entorno en Render:

```
Name: OPENAI_API_KEY
Value: sk-... (tu clave de OpenAI)
```

---

## 🌐 Cómo usar

1. Abrí la URL generada por Render
2. Tocá el botón “🎙 Grabar voz”
3. Hablá tu consulta → se transcribe automáticamente
4. El asistente responde en texto y voz

---

## 💡 Créditos

Desarrollado con IA para presentación de Casa del Audio
