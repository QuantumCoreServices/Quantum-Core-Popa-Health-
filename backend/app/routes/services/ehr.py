from fhirclient import client
from fhirclient.models.patient import Patient
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
