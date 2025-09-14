from fastapi import HTTPException, Depends, Header
from typing import Optional
import os

# API Key for your friend
FRIEND_API_KEY = "friend_access_2024_secure_key_12345"

def validate_api_key(x_api_key: Optional[str] = Header(None)):
    """
    Validate API key for accessing the PDF storage API
    """
    if not x_api_key:
        raise HTTPException(
            status_code=401, 
            detail="API key required. Please provide X-API-Key header."
        )
    
    if x_api_key != FRIEND_API_KEY:
        raise HTTPException(
            status_code=403, 
            detail="Invalid API key. Access denied."
        )
    
    return x_api_key

def get_api_key():
    """
    Get the API key for your friend
    """
    return FRIEND_API_KEY
