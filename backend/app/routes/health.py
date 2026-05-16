from fastapi import APIRouter
from ..config import settings

router = APIRouter(prefix="/api", tags=["health"])

@router.get("/health")
async def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Coach José API",
        "version": "1.0.0",
        "environment": "production" if not settings.DEBUG else "development"
    }

@router.get("/status")
async def status():
    """Detailed status"""
    return {
        "api": "operational",
        "chatbot": "online",
        "crm": "ready",
        "timestamp": "2026-05-16T03:00:00Z"
    }
