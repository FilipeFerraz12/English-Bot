from google.cloud import speech
import os
from pydub import AudioSegment
from dotenv import load_dotenv
load_dotenv()


def transcribe_audio(audio_file):
    client = speech.SpeechClient()
    audio = AudioSegment.from_file(audio_file)
    audio.export("temp.wav", format="wav")

    with open("temp.wav", "rb") as f:
        byte_data = f.read()

    audio = speech.RecognitionAudio(content=byte_data)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US"
    )

    response = client.recognize(config=config, audio=audio)
    transcription = ""
    for result in response.results:
        transcription += result.alternatives[0].transcript

    return transcription
