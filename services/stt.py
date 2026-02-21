from openai import OpenAI
import os
import tempfile
from dotenv import load_dotenv
    
load_dotenv()
client = OpenAI(api_key=os.getenv("OpenAI"))

def audioText(file):
    # Save uploaded file to a temporary .webm file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as tmp:
        tmp.write(file.read())
        tmp_path = tmp.name

    # Reopen in binary mode for OpenAI
    with open(tmp_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

    return transcript.text