from fastapi import APIRouter, HTTPException, Request
import requests, base64
import os

router = APIRouter()

# Replace these with your actual Fitbit credentials and redirect URI
CLIENT_ID = os.getenv("FITBIT_CLIENT_ID", "YOUR_CLIENT_ID")
CLIENT_SECRET = os.getenv("FITBIT_CLIENT_SECRET", "YOUR_CLIENT_SECRET")
REDIRECT_URI = os.getenv("FITBIT_REDIRECT_URI", "https://yourdomain.com/api/wearables/fitbit/callback")

@router.get("/fitbit/connect")
def connect_fitbit():
    # Redirect the user to Fitbit's OAuth authorization page
    authorization_url = (
        "https://www.fitbit.com/oauth2/authorize?"
        f"response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
        "&scope=activity%20heartrate%20sleep"
    )
    return {"authorization_url": authorization_url}

@router.get("/fitbit/callback")
def fitbit_callback(code: str):
    # Exchange authorization code for access token
    token_url = "https://api.fitbit.com/oauth2/token"
    client_credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
    b64_credentials = base64.b64encode(client_credentials.encode()).decode()
    headers = {
        "Authorization": f"Basic {b64_credentials}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "client_id": CLIENT_ID,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI,
        "code": code,
    }
    response = requests.post(token_url, data=data, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to retrieve token from Fitbit")
    token_data = response.json()
    # Save token_data securely (e.g., in your database associated with the user)
    return {"token_data": token_data}
