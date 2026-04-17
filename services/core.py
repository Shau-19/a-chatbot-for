import httpx


class ChatService:
    def chat(self, message: str):
        # Use httpx for external API calls
async def some_function():
    async with httpx.AsyncClient() as client:
            response = await client.get("https://example.com/api/chat", params={"message": message})
            return response.json()