from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta
import jwt

router = APIRouter()
SECRET_KEY = "your_secret_key"  # Replace with a secure secret key
ALGORITHM = "HS256"

class Token(BaseModel):
    access_token: str
    token_type: str

@router.post("/login", response_model=Token)
def login(user: dict):
    # Placeholder authentication logic
    # Validate user credentials here...
    token_expires = timedelta(hours=1)
    expiration = datetime.utcnow() + token_expires
    token = jwt.encode({"sub": user.get("username"), "exp": expiration}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}
