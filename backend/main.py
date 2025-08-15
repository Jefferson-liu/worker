from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.message import Message
#from agents.Manager import Manager
from openai_api.chat import get_gpt_response
from typing import List
import time

app = FastAPI()

# Allow CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"] ,
    allow_headers=["*"]
)

@app.post("/chat")
async def chat(messages: List[Message]):
    try:
        gpt_reply = await get_gpt_response([m.model_dump() for m in messages])
        return {
            "text": gpt_reply,
            "sender": "assistant",
            "timestamp": int(time.time() * 1000)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
