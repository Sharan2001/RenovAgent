from fastapi import FastAPI, UploadFile, File
from conversation import ConversationManager
from agents.bob import BobAgent
from agents.alice import AliceAgent
from services.stt import audioText
from services.tts import speakText
from fastapi.staticfiles import StaticFiles
import base64
from fastapi.responses import JSONResponse

app = FastAPI()

manager = ConversationManager()
bob = BobAgent()
alice = AliceAgent()

## Non streaming endpoint - for testing and simplicity in frontend integration. 
@app.post("/voice")
async def voice_endpoint(file: UploadFile = File(...)):

    transcript = audioText(file.file)

    reply_text = manager.handle_input(transcript, bob, alice)

    audio_bytes = speakText(reply_text, manager.active_agent)

    audio_base64 = base64.b64encode(audio_bytes).decode("utf-8") # Convert bytes to base64 string for browser audio

    print("\nUser:", transcript)
    print("Agent:", manager.active_agent)
    print("Response:", reply_text)
    print("-----------------------------------------------------")

    return JSONResponse({
        "transcript": transcript,
        "response": reply_text,
        "agent": manager.active_agent,
        "audio": audio_base64
    })

app.mount("/", StaticFiles(directory="static", html=True), name="static")
