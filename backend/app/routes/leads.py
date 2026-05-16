from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from datetime import datetime
import os

router = APIRouter(prefix="/api/leads", tags=["leads"])

class Lead(BaseModel):
    email: str
    phone: str = None
    name: str = None
    source: str = "chatbot"
    interested_products: list = None
    notes: str = None

class LeadResponse(BaseModel):
    id: str
    email: str
    created_at: str
    status: str

# In-memory storage (replace with Supabase in production)
leads_db = {}

@router.post("/capture")
async def capture_lead(lead: Lead) -> LeadResponse:
    """Capture lead information from chatbot"""
    try:
        lead_id = f"lead_{int(datetime.now().timestamp())}"
        
        leads_db[lead_id] = {
            "email": lead.email,
            "phone": lead.phone,
            "name": lead.name,
            "source": lead.source,
            "interested_products": lead.interested_products,
            "notes": lead.notes,
            "created_at": datetime.now().isoformat(),
            "status": "new"
        }
        
        return LeadResponse(
            id=lead_id,
            email=lead.email,
            created_at=datetime.now().isoformat(),
            status="new"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/list")
async def list_leads():
    """List all captured leads"""
    return {
        "total": len(leads_db),
        "leads": leads_db
    }

@router.get("/{lead_id}")
async def get_lead(lead_id: str):
    """Get specific lead details"""
    if lead_id not in leads_db:
        raise HTTPException(status_code=404, detail="Lead not found")
    
    return leads_db[lead_id]

@router.post("/{lead_id}/status")
async def update_lead_status(lead_id: str, status: str):
    """Update lead status"""
    if lead_id not in leads_db:
        raise HTTPException(status_code=404, detail="Lead not found")
    
    leads_db[lead_id]["status"] = status
    return {"id": lead_id, "status": status}
