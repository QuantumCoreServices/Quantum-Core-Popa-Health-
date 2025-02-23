from fhirclient import client
from fhirclient.models.patient import Patient
from fastapi import APIRouter, HTTPException
from app.services import ehr
import os

def get_fhir_client():
    settings = {
        'app_id': 'popa_v10',
        'api_base': os.getenv("FHIR_API_BASE", "https://fhir.example.com")
    }
    return client.FHIRClient(settings=settings)

def get_patient_data(patient_id: str):
    smart = get_fhir_client()
    try:
        patient = Patient.read(patient_id, smart.server)
        return patient.as_json()
    except Exception as e:
        raise Exception(f"Error fetching patient data: {e}")

router = APIRouter()

@router.get("/patient/{patient_id}")
def fetch_patient(patient_id: str):
    try:
        patient_data = ehr.get_patient_data(patient_id)
        return {"patient_data": patient_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
