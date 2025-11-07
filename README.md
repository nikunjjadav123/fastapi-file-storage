# FastAPI File Storage Service

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-lightgreen)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange)

A simple FastAPI project to **upload, store, list, and download files** in a folder.  
Includes **Docker support** and a **CI/CD pipeline** for automatic deployment.

---

## Features

- Upload files to a designated folder
- List all uploaded files
- Download files
- Dockerized for easy deployment
- CI/CD pipeline to automatically build and deploy Docker images

---

## Tech Stack

- **Backend**: Python, FastAPI  
- **File Storage**: files folder  
- **Docker**: Containerization  
- **CI/CD**: GitHub Actions (example)  
- **Python Libraries**: `fastapi`, `uvicorn`, `python-multipart`

---

## Project Structure

fastapi-file-storage/
│
├── app/
│ ├── main.py
│ ├── config.py
│ └── schemas.py 
│ └── file_manager.py
├── files / # Folder to store uploaded images
│
├── Dockerfile # Docker configuration
├── requirements.txt # Python dependencies
├── .github/workflows/ci-cd.yml # CI/CD pipeline configuration
└── README.md # Project documentation
└── .gitignore


---

## Installation (Local)

1. Clone the repository:

```bash
git clone https://github.com/yourusername/fastapi-file-storage.git
cd fastapi-file-storage
```
---

## Docker Setup

### 1. Build Docker Image Manually

```bash
docker build -t fastapi-file-storage .
docker run -d -p 8000:8000 fastapi-file-storage
http://localhost:8000/docs

```

## CI/CD Pipeline (GitHub Actions)

This project includes a **CI/CD pipeline using GitHub Actions** that automates the deployment of your FastAPI Docker container.  

### Pipeline Steps

1. **Build Docker Image**  
   The pipeline automatically builds the Docker image of your FastAPI app whenever you push to the `main` branch.

2. **Push Docker Image to DockerHub**  
   After building, the image is pushed to your DockerHub repository using the credentials stored in GitHub Secrets.

3. **Pull Docker Image on the Server**  
   The server pulls the latest Docker image from DockerHub to ensure the deployment uses the newest version.

4. **Run the Docker Container Automatically**  
   The pipeline stops any running container with the same name, removes it, and starts a new container with the updated image.
