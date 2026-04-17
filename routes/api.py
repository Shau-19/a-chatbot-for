from pydantic import BaseModel
from fastapi import APIRouter
from services.core import ChatService

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

chat_service = ChatService()

@router.post("/chat")
async def chat(req: ChatRequest):
    return chat_service.chat(req.message)