# Auth0 User Management API

This project provides a Function Calls and RESTful API for managing users in the Auth0 database. It allows you to perform CRUD (Create, Read, Update, Delete) operations on user data.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Auth0 Management API token
- Auth0 domain

### Installation



1. There are three directories as below:

- Function_Calls
- API_Calls
- Docker_K8s

2. To run Functions calls, follow commands:

- pip install requests
- python app.py

3. To run API calls, follow commands:

- pip install -r requirements.txt
- python app.py

4. To build and run Docker image, follow commands:

- docker build -t test-crud-image ./Docker_K8s
- docker run --name test-crud-docker-container -p 5000:5000 test-crud-image:latest
