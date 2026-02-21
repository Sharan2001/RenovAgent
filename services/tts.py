from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OpenAI"))

def speakText(text,agentName):
    if agentName == "Bob":
        voice = "onyx"
    elif agentName == "Alice":        
        voice = "shimmer"
    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice=voice,
        input=text
    )

    return response.content