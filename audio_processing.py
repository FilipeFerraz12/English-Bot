from google.cloud import speech
from pydub import AudioSegment
import os
from dotenv import load_dotenv

load_dotenv()

def transcribe_audio(audio_file_path: str) -> str:
    """
    Transcreve um arquivo de áudio usando Google Cloud Speech-to-Text.
    Recebe o caminho do arquivo de áudio (pode ser .ogg, .mp3 etc).
    Retorna a transcrição em texto.
    """
    # Inicializa cliente do Google Speech
    client = speech.SpeechClient()

    # Converte o arquivo para WAV PCM LINEAR16, que o Google espera
    audio_segment = AudioSegment.from_file(audio_file_path)
    temp_wav_path = "temp.wav"
    audio_segment.export(temp_wav_path, format="wav")

    # Lê bytes do áudio convertido
    with open(temp_wav_path, "rb") as audio_file:
        content = audio_file.read()

    # Prepara o áudio para o reconhecimento
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=audio_segment.frame_rate,  # Melhor informar o sample rate original
        language_code="en-US",
        enable_automatic_punctuation=True,  # Opcional, para pontuação automática
    )

    # Chama a API de reconhecimento
    response = client.recognize(config=config, audio=audio)

    # Concatena resultados de transcrição
    transcription = " ".join([result.alternatives[0].transcript for result in response.results])

    # Remove arquivo temporário
    if os.path.exists(temp_wav_path):
        os.remove(temp_wav_path)

    return transcription
