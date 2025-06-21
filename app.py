from fastapi import FastAPI, Request, Form
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from model import generate_audio_stream
import io

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# For frontend form
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# For frontend form POST
@app.post("/speak-form")
async def speak_form(text: str = Form(...)):
    if not text.strip():
        return HTMLResponse("No input provided", status_code=400)
    audio_stream = generate_audio_stream(text)
    return StreamingResponse(audio_stream, media_type="audio/mpeg")

# ✅ For OpenAI SDK JSON POST
class TTSRequest(BaseModel):
    text: str

@app.post("/speak")
async def speak_json(request: TTSRequest):
    audio_stream = generate_audio_stream(request.text)
    return StreamingResponse(audio_stream, media_type="audio/mpeg")
