from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    # API Keys
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "")
    
    # Application
    APP_NAME: str = "Coach José"
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    
    # URLs
    NEOLIFE_SHOP_URL: str = os.getenv("NEOLIFE_SHOP_URL", "https://shopneolife.com/startupforworld")
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000")
    
    class Config:
        env_file = ".env"

settings = Settings()
