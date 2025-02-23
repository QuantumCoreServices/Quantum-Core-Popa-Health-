from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes import appointments, prescriptions, lab_results, auth, ai

app = FastAPI(
    title="Popa v10 API",
    description="API for Popa v10: AI-driven patient engagement platform",
    version="0.1.0"
)

# CORS settings: adjust origins as needed for production
origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers from different modules
app.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])
app.include_router(prescriptions.router, prefix="/prescriptions", tags=["Prescriptions"])
app.include_router(lab_results.router, prefix="/lab-results", tags=["Lab Results"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(ai.router, prefix="/ai", tags=["AI Services"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Popa v10 API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
