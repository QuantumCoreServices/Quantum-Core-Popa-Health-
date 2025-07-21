# Popa-Health - White-Label Patient Portal

Quantum-Core-Popa-Health is a comprehensive, white-label patient portal designed to enhance patient engagement for healthcare providers. This platform provides features such as appointment management, lab result viewing, prescription management, and personalized health recommendations. The solution leverages modern technologies, ensuring secure and seamless integration with EHR systems and wearable devices while maintaining a customizable interface for different clinics and healthcare providers.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Deployment](#deployment)
- [CI/CD Pipeline](#cicd-pipeline)
- [Contributing](#contributing)
- [License](#license)

## Overview

Quantum-Core-Popa-Health integrates a robust FastAPI/Python backend with a modern React-based frontend to deliver a customizable patient engagement solution. The platform allows clinics to brand the portal with their logos, color schemes, and custom content while offering patients a unified experience for managing appointments, prescriptions, lab results, and health data. The platform ensures HIPAA compliance, secure API interactions, and seamless data synchronization with wearable devices (Apple HealthKit, Fitbit, Garmin) and EHR systems using FHIR/HL7 standards.

## Features

- Customizable branding for clinics, including logos, colors, and content.
- Secure patient authentication with JWT-based access control.
- Appointment booking, rescheduling, and cancellation functionalities.
- Access to lab results, prescription management, and medical records.
- Integration with wearable devices and EHR systems using FHIR/HL7 protocols.
- Personalized health recommendations powered by AI and predictive analytics.
- Scalable cloud deployment using AWS EKS with Infrastructure as Code via Terraform.
- Automated CI/CD pipeline using GitHub Actions for seamless deployments.

## Architecture

The platform is designed with a microservices architecture, ensuring scalability and maintainability:

- Backend: FastAPI service handling authentication, appointments, lab results, prescriptions, and AI-driven health insights.
- Frontend: React application offering an intuitive user interface with customizable branding options.
- Integration Modules: Services to connect with wearable APIs and EHR systems.
- Infrastructure: AWS deployment managed through Terraform and Kubernetes for container orchestration.
- CI/CD: Automated workflows for continuous integration and deployment using GitHub Actions.

## Technology Stack

- Backend: Python, FastAPI, SQLAlchemy, JWT, Pydantic
- Frontend: React, Vite, Tailwind CSS
- AI/ML: Integration with LLMs for conversational AI and predictive analytics
- Infrastructure: AWS (EKS, RDS, S3), Terraform, Kubernetes, Docker
- CI/CD: GitHub Actions, AWS ECR

## Project Structure

```
Quantum-Core-Popa-Health/
├── backend/                      # FastAPI backend service
│   ├── app/
│   │   ├── main.py                # Entry point for the FastAPI app
│   │   ├── routes/                # API routes (appointments, patients, lab results, prescriptions)
│   │   ├── models/                # Database models
│   │   ├── services/              # Business logic and external service integrations
│   │   └── utils/                 # Utility functions and helpers
│   ├── Dockerfile                 # Docker configuration for backend
│   └── requirements.txt           # Python dependencies
├── frontend/                      # React frontend application
│   ├── src/
│   │   ├── components/            # Reusable UI components
│   │   ├── pages/                 # Page-level components (Appointments, Lab Results, Profile, etc.)
│   │   └── services/              # API service calls
│   ├── Dockerfile                 # Docker configuration for frontend
│   ├── package.json               # Node.js dependencies
│   └── README.md                  # Frontend documentation
├── infrastructure/                # Terraform configurations for AWS resources
│   ├── main.tf                    # Main Terraform configuration
│   ├── variables.tf               # Terraform variables
│   └── outputs.tf                 # Terraform output configurations
├── .github/                       # GitHub Actions workflows
│   └── workflows/
│       └── ci-cd.yml              # CI/CD pipeline configuration
├── .gitignore                     # Files and folders to ignore
└── README.md                      # This file
```

## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Obionedonthoeme/Quantum-Core-Popa-Health.git
cd Quantum-Core-Popa-Health
```

### 2. Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 3. Frontend Setup

```bash
cd ../frontend
npm install
npm run dev
```

## Deployment

### Infrastructure Provisioning

Provision AWS resources using Terraform:

```bash
cd ../infrastructure
terraform init
terraform apply
```

### Containerization and Deployment

Build and push Docker images to AWS ECR:

```bash
# Build images
docker build -t backend:latest ../backend
docker build -t frontend:latest ../frontend

# Authenticate with AWS ECR
aws ecr get-login-password | docker login --username AWS --password-stdin <account_id>.dkr.ecr.<region>.amazonaws.com

# Tag and push images
docker tag backend:latest <ecr_repo>/backend:latest
docker tag frontend:latest <ecr_repo>/frontend:latest
docker push <ecr_repo>/backend:latest
docker push <ecr_repo>/frontend:latest
```

Deploy containers to AWS EKS:

```bash
kubectl apply -f k8s/backend-deployment.yml
kubectl apply -f k8s/frontend-deployment.yml
```

## CI/CD Pipeline

The project includes a GitHub Actions-based CI/CD pipeline:

- Triggers on pushes to the `main` branch.
- Builds Docker images for the backend and frontend.
- Pushes images to AWS ECR.
- Deploys services to AWS EKS using Kubernetes manifests.

To manually trigger the pipeline:

```bash
git commit -am "Trigger deployment"
git push origin main
```

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to your fork:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request for review.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
