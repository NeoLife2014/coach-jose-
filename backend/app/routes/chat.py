from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import openai
from ..config import settings

router = APIRouter(prefix="/api/chat", tags=["chat"])

# Configure OpenAI
if settings.OPENAI_API_KEY:
    openai.api_key = settings.OPENAI_API_KEY

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    conversation_id: str = None
    user_name: str = None

class ChatResponse(BaseModel):
    message: str
    conversation_id: str
    timestamp: str

@router.post("/message")
async def send_message(request: ChatRequest) -> ChatResponse:
    """Send a message to the AI chatbot"""
    try:
        if not settings.OPENAI_API_KEY:
            raise HTTPException(status_code=500, detail="OpenAI API key not configured")
        
        # System prompt for Neolife product sales
        system_prompt = f"""You are Coach José, an AI assistant helping people discover Neolife products.
        
Your goals:
1. Help customers understand Neolife wellness products
2. Answer questions about health and nutrition
3. Guide interested prospects to: {settings.NEOLIFE_SHOP_URL}
4. Be friendly, professional, and helpful
5. Always encourage trying products through the official shop

Neolife Focus: Premium wellness, health supplements, natural products
        """
        
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": request.message}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        bot_message = response.choices[0].message.content
        
        from datetime import datetime
        return ChatResponse(
            message=bot_message,
            conversation_id=request.conversation_id or "default",
            timestamp=datetime.now().isoformat()
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/info")
async def chat_info():
    """Get chatbot information"""
    return {
        "name": "Coach José",
        "role": "Sales & Product Consultant",
        "specialization": "Neolife Wellness Products",
        "shop_url": settings.NEOLIFE_SHOP_URL,
        "available": True
    }
