from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextData(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Backend is running"}

@app.post("/generate")
def generate_voice(data: TextData):
    return {
        "status": "success",
        "received_text": data.text
    }
