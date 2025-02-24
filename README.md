# POPA Health Patient Portal

POPA Health AI is a comprehensive, AI-driven patient engagement platform designed for modern healthcare. Leveraging cutting-edge technologies, the platform provides personalized health recommendations, appointment management, and a virtual health assistant to answer patient queries and deliver actionable insights.

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

POPA Health Patient Portal integrates a robust FastAPI/Python backend with a modern React-based frontend to create a secure, scalable, and user-friendly patient engagement system. The platform seamlessly integrates with wearable devices (Apple HealthKit, Fitbit, Garmin) and EHR systems (FHIR/HL7) to collect and analyze patient data, providing healthcare professionals with real-time insights and patients with personalized recommendations.

## Features

- **Conversational AI:** Leverages Large Language Models (LLMs) for natural language processing and virtual health assistance.
- **Predictive Analytics:** Uses AI to monitor patient health data and generate personalized recommendations.
- **Secure APIs:** FastAPI backend with JWT-based authentication and advanced encryption for data privacy.
- **Modern Frontend:** React-based UI with animated dashboards and interactive elements.
- **Device & EHR Integration:** Connects to wearable devices and EHR systems to pull comprehensive health metrics.
- **Scalable Infrastructure:** Deployed on AWS using Kubernetes (EKS), with Infrastructure as Code (Terraform) and a robust CI/CD pipeline using GitHub Actions.

## Architecture

The system is designed with a microservices approach:

- **Backend:** FastAPI service handling secure API endpoints, authentication, and AI/ML services.
- **Frontend:** A React application providing a dynamic, user-friendly dashboard.
- **Integration Modules:** Services to connect with wearable device APIs and EHR systems using FHIR/HL7 standards.
- **Infrastructure:** AWS cloud deployment using EKS for container orchestration and Terraform for Infrastructure as Code.
- **CI/CD:** Automated builds, tests, and deployments using GitHub Actions.

## Technology Stack

- **Backend:** Python, FastAPI, SQLAlchemy, JWT
- **Frontend:** React, Vite, Tailwind CSS, Framer Motion
- **AI/ML:** Integration with LLMs (e.g., OpenAI API) and custom predictive analytics models
- **Cloud & Infrastructure:** AWS (EKS, RDS, S3), Terraform, Kubernetes
- **CI/CD:** GitHub Actions, Docker, AWS ECR

## Project Structure




POPA-Health-AI/ ├── backend/ # FastAPI backend service │
├── app/ │ │
├── main.py # FastAPI application entry point │ 
│ ├── routes/ # API route definitions │ 
│ ├── models/ # Database models │
│ └── services/ # Business logic and integrations │
├── Dockerfile # Backend Docker configuration │
└── requirements.txt # Python dependencies ├
── frontend/ # React frontend application │ 
├── src/ │ │ ├── components/ # UI components and animations │
│ ├── pages/ # Page-level components │
│ └── services/ # API utilities │
├── Dockerfile # Frontend Docker configuration │ 
├── package.json # Node.js dependencies │
└── README.md # Frontend documentation ├
── infrastructure/ # Terraform configurations │
├── main.tf # Main Terraform setup │
├── variables.tf # Variables definition │
└── outputs.tf # Outputs from Terraform ├
── .github/ # CI/CD workflows │ 
└── workflows/ │ └── ci-cd.yml # GitHub Actions pipeline ├
── .gitignore # Ignored files and folders
└── README.md # Project documentation



## Setup & Installation

# Clone the Repository

```bash
git clone https://github.com/Obionedonthoeme/POPA-Health-AI.git
cd POPA-Health-AI



cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

# Deployment
Infrastructure Provisioning
Use Terraform to set up AWS resources:


cd infrastructure
terraform init
terraform apply

#Containerization & Deployment
# Build Docker images
docker build -t backend:latest ./backend
docker build -t frontend:latest ./frontend

# Push images to AWS ECR (after login)
aws ecr get-login-password | docker login --username AWS --password-stdin <account_id>.dkr.ecr.<region>.amazonaws.com
docker tag backend:latest <ecr_repo>/backend:latest
docker tag frontend:latest <ecr_repo>/frontend:latest
docker push <ecr_repo>/backend:latest
docker push <ecr_repo>/frontend:latest

Deploy the containers to AWS EKS using Kubernetes manifests.

#CI/CD Pipeline
The project uses GitHub Actions for automated workflows:

Builds Docker images
Pushes to AWS ECR
Deploys to AWS EKS
Pipeline configuration: .github/workflows/ci-cd.yml





