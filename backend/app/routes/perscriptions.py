from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_prescriptions():
    # Retrieve prescriptions for a patient (placeholder)
    return {"prescriptions": []}
