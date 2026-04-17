import httpx
from pydantic import BaseModel

class ChatService:
    def chat(self, message: str):
        # Use httpx for external API calls
        async with httpx.AsyncClient() as client:
            response = await client.get("https://example.com/api/chat", params={"message": message})
            return response.json()