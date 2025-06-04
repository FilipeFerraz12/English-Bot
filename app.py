from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from openai_utils import correct_english_text
from audio_processing import transcribe_audio
import os
import requests

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get("Body")
    media_url = request.form.get("MediaUrl0")
    resp = MessagingResponse()
    msg = resp.message()

    if media_url:
        r = requests.get(media_url)
        with open("audio.ogg", "wb") as f:
            f.write(r.content)
        transcription = transcribe_audio("audio.ogg")
        feedback = correct_english_text(transcription)
        msg.body(f"You said: {transcription}\n\nFeedback:\n{feedback}")
    else:
        feedback = correct_english_text(incoming_msg)
        msg.body(feedback)

    return str(resp)

@app.route("/", methods=["GET"])
def index():
    return "English Bot is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
