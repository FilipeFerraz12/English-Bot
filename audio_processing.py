from google.cloud import speech
import os
from pydub import AudioSegment
from dotenv import load_dotenv
load_dotenv()

def transcribe_audio(audio_file):
    client = speech.SpeechClient()

    # Converte para .wav com codificação adequada
    audio = AudioSegment.from_file(audio_file)
    audio = audio.set_channels(1).set_frame_rate(16000)
    audio.export("temp.wav", format="wav")

    # Lê o áudio convertido
    with open("temp.wav", "rb") as f:
        byte_data = f.read()

    audio = speech.RecognitionAudio(content=byte_data)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US"
    )

    try:
        response = client.recognize(config=config, audio=audio)
        transcription = ""
        for result in response.results:
            transcription += result.alternatives[0].transcript
        return transcription or "Sorry, I couldn't understand the audio."
    except Exception as e:
        print("Erro no Google Speech:", e)
        return "Sorry, there was an error transcribing the audio."
