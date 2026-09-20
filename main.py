from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from response_engine import generate_response


app = FastAPI(title="Useless Chatbot API")


# Allow the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    text: str
    emotion: str
    meme: str | None = None


@app.get("/")
def root():
    return {
        "status": "online",
        "message": "The useless bot has awakened."
    }


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    user_message = request.message.strip()

    return generate_response(user_message)
