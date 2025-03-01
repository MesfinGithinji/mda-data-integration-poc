MDA Data Integration POC 🚀

Overview

The Multi-Agency Data (MDA) Integration Proof of Concept (POC) is a secure, scalable solution designed to facilitate inter-agency data exchange using modern cloud-based technologies. This project demonstrates a decentralized data-sharing architecture with a focus on security, reliability, and real-time data processing.

Tech Stack

Backend

FastAPI (High-performance Python framework for APIs)

SQLAlchemy & Alembic (ORM & database migrations)

PostgreSQL & SQLite (Database for persistent and mock data storage)

JWT Authentication (Secure token-based authentication)

Pydantic (Data validation and serialization)

Message Broker & Async Processing

RabbitMQ (Event-driven messaging for inter-agency data exchange)

Celery (Asynchronous task processing for data ingestion & transformation)

Frontend (Coming Soon)

React.js (Admin dashboard for monitoring integrations & analytics)

Material UI (Modern UI components)

Redux Toolkit (State management)

Cloud & Infrastructure

AWS (Free Tier for POC):

EC2 (Compute instance for hosting the backend API)

RDS (PostgreSQL) (Managed database service for production data storage)

S3 (Storage for logs and static assets)

SQS (Alternative to RabbitMQ for message queuing)

IAM Roles & Policies (Access control & security)

CloudWatch (Logging & monitoring)

Route 53 (Custom domain management)

Architecture

This system follows a microservices-inspired architecture, where different agencies interact securely without exposing direct database access.

High-Level Workflow

Agency A submits a data request via a FastAPI endpoint.

The request is authenticated using JWT tokens.

The API interacts with PostgreSQL for data retrieval/storage.

If the request requires asynchronous processing, it is sent to RabbitMQ.

A Celery worker processes the request and sends back the response.

Agency B receives the processed data through a secure API.

All requests and transactions are logged in AWS CloudWatch & S3 for auditing.

Installation & Setup

1. Clone the Repository

git clone https://github.com/YOUR_GITHUB_USERNAME/mda-data-integration-poc.git
cd mda-data-integration-poc

2. Set Up Virtual Environment

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file with the following variables:

DATABASE_URL=postgresql+asyncpg://user:password@localhost/mda_db
JWT_SECRET_KEY=your_secret_key
RABBITMQ_URL=amqp://guest:guest@localhost/

5. Run Database Migrations

alembic upgrade head

6. Start the API Server

uvicorn main:app --reload

The API will be available at: http://localhost:8000

7. Start RabbitMQ & Celery

docker-compose up -d  # Starts RabbitMQ & Celery in the background
celery -A worker.tasks worker --loglevel=info

API Endpoints

Authentication

POST /auth/login - User login & JWT token generation

POST /auth/register - Register a new agency user

Birth Records API

GET /birth_records - Fetch all birth records

POST /birth_records - Add a new birth record

Agency Data Exchange

POST /data/request - Submit a data request to another agency

GET /data/status/{request_id} - Check the status of a data request

Cloud Deployment Guide (AWS)

1. Set Up EC2 Instance

Create an EC2 instance (t2.micro, Ubuntu 22.04)

Install required dependencies:

sudo apt update && sudo apt install python3-pip nginx docker-compose

2. Deploy FastAPI on EC2

Copy project files to the EC2 instance:

scp -r mda-data-integration-poc ubuntu@your-ec2-ip:/home/ubuntu/

SSH into the EC2 instance:

ssh ubuntu@your-ec2-ip

Start the application:

cd mda-data-integration-poc
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

3. Set Up PostgreSQL on AWS RDS

Create an RDS PostgreSQL instance.

Update DATABASE_URL in the .env file to point to the RDS instance.

Apply migrations:

alembic upgrade head

4. Configure Nginx as a Reverse Proxy

Install Nginx:

sudo apt install nginx

Edit the Nginx config:

sudo nano /etc/nginx/sites-available/mda

Add the following:

server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

Enable and restart Nginx:

sudo ln -s /etc/nginx/sites-available/mda /etc/nginx/sites-enabled/
sudo systemctl restart nginx

Security Considerations

JWT authentication ensures that only authorized users can access the system.

IAM roles and security groups restrict access to AWS resources.

HTTPS (TLS/SSL) encryption is enforced for all communication.

Logging & Monitoring via AWS CloudWatch and S3 ensure traceability.

Future Enhancements

Kubernetes Deployment (EKS on AWS)

Data Transformation Pipeline (ETL using AWS Lambda & Glue)

GraphQL Support for flexible queries

Full Frontend Dashboard (React.js + Redux)

Contributors

Your Name - Backend Engineer

Other Team Members (If any)

License

This project is licensed under the MIT License.

🚀 MDA Data Integration POC - Enabling Secure & Scalable Inter-Agency Data Sharing 🚀