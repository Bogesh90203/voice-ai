import io
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from gtts import gTTS
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextData(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "Backend is running"}


@app.post("/generate")
def generate_voice(data: TextData):
    if not data.text or not data.text.strip():
        return {"message": "No text provided", "status": "error"}

    buf = io.BytesIO()
    tts = gTTS(text=data.text.strip(), lang="en")
    tts.write_to_fp(buf)
    buf.seek(0)
    return StreamingResponse(buf, media_type="audio/mpeg")
