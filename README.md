WhatsByte - Healthcare Management API
A Django REST API designed to manage doctor-patient relationships within a healthcare system.

🔧 Features
JWT-based Authentication

Admin user control

Doctor management

Patient management

Doctor–Patient mapping system

🛠️ Tech Stack
Python 3.x

Django 5.2.1

Django REST Framework 3.16.0

PostgreSQL

JWT Authentication (Simple JWT)

🚀 Getting Started
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/DarkIce000/whatsbyte.git
cd whatsbyte
2. Set up a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Configure environment variables
Create a .env file in the root directory with the following:

ini
Copy
Edit
NAME = "postgres"
USER = "postgres"
PASSWORD = "admin"
HOST = "localhost"
PORT = "5432"
5. Apply migrations
bash
Copy
Edit
python manage.py migrate
6. Create a superuser
bash
Copy
Edit
python manage.py createsuperuser
7. Start the development server
bash
Copy
Edit
python manage.py runserver
📌 API Endpoints
🔐 Authentication
POST /api/admin_register/ – Register an admin

POST /api/token/ – Get JWT token pair

POST /api/token/refresh/ – Refresh access token

👤 Admin Management
GET/PUT/PATCH/DELETE /api/admins/<id>/ – Manage admin users

🧑‍⚕️ Doctors
GET /api/doctors/ – List all doctors

POST /api/doctors/ – Add a doctor

GET/PUT/PATCH/DELETE /api/doctors/<id>/ – Manage a doctor

🧑 Patients
GET /api/patients/ – List all patients

POST /api/patients/ – Add a patient

GET/PUT/PATCH/DELETE /api/patients/<id>/ – Manage a patient

🔗 Doctor-Patient Mapping
GET /api/mappings/ – List all mappings

POST /api/mappings/ – Create a mapping

GET/PUT/PATCH/DELETE /api/mappings/<id>/ – Manage a mapping

🔒 Authentication Guide
This project uses JWT for secure authentication.

Get a token pair

bash
Copy
Edit
curl -X POST http://localhost:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "admin", "password": "password"}'
Use the token

bash
Copy
Edit
curl http://localhost:8000/api/doctors/ \
     -H "Authorization: Bearer <your-access-token>"
🧬 Data Models
🧑‍💼 User
Extends Django's AbstractUser

Used for admin authentication

🧑‍⚕️ Doctor
name: CharField

age: SmallIntegerField

address: TextField

speciality: CharField

🧑 Patient
name: CharField

age: SmallIntegerField

address: TextField

🔗 Mapping
doctor: ForeignKey to Doctor

patient: ForeignKey to Patient

assigned_at: DateTimeField (auto_now_add)
