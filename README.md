# WhatsByte - Healthcare Management API

A Django REST API for managing doctor-patient relationships in a healthcare system.

## Features

- JWT Authentication
- Admin user management
- Doctor management
- Patient management
- Doctor-Patient mapping system

## Tech Stack

- Python 3.x
- Django 5.2.1
- Django REST Framework 3.16.0
- PostgreSQL
- JWT Authentication (Simple JWT)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/DarkIce000/whatsbyte.git
cd whatsbyte
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
Create a `.env` file in the root directory with:
```
NAME = "postgres"
USER = "postgres"
PASSWORD = "admin"
HOST = "localhost"
PORT = "5432"
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
- `POST /api/admin_register/` - Register new admin user
- `POST /api/token/` - Obtain JWT token pair
- `POST /api/token/refresh/` - Refresh JWT token

### Admin Management
- `GET/PUT/PATCH/DELETE /api/admins/<id>/` - Manage admin users

### Patients
- `GET /api/patients/` - List all patients
- `POST /api/patients/` - Create new patient
- `GET/PUT/PATCH/DELETE /api/patients/<id>/` - Manage individual patient

### Doctors
- `GET /api/doctors/` - List all doctors
- `POST /api/doctors/` - Create new doctor
- `GET/PUT/PATCH/DELETE /api/doctors/<id>/` - Manage individual doctor

### Doctor-Patient Mappings
- `GET /api/mappings/` - List all mappings
- `POST /api/mappings/` - Create new mapping
- `GET/PUT/PATCH/DELETE /api/mappings/<id>/` - Manage individual mapping

## Authentication

The API uses JWT (JSON Web Token) authentication. To access protected endpoints:

1. Obtain token pair:
```bash
curl -X POST http://localhost:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "admin", "password": "password"}'
```

2. Use the access token in subsequent requests:
```bash
curl http://localhost:8000/api/doctors/ \
     -H "Authorization: Bearer <your-access-token>"
```

## Models

### User
- Extended Django's AbstractUser
- Used for admin authentication

### Doctor
- name (CharField)
- age (SmallIntegerField)
- address (TextField)
- speciality (CharField)

### Patient
- name (CharField)
- age (SmallIntegerField)
- address (TextField)

### Mapping
- doctor (ForeignKey to Doctor)
- patient (ForeignKey to Patient)
- assigned_at (DateTimeField, auto_now_add)
