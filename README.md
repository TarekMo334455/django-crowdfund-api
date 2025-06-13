# 🌟 Django Crowdfunding API

A robust and scalable RESTful API for a crowdfunding platform built using **Django** and **Django REST Framework (DRF)**.  
This API enables users to register, authenticate, and create/manage fundraising projects securely and efficiently.

---

## ✨ Key Features

### 👤 User Management
- Full user authentication system
- JWT (JSON Web Token) based authentication
- User registration with validation:
  - Username
  - First name / Last name
  - Email
  - Egyptian phone number format validation
  - Password + confirmation
- Login & token refresh

### 💼 Project Management
- Create, Read, Update, Delete (CRUD) operations for projects
- Project attributes:
  - Title & description
  - Target amount (EGP)
  - Start and end dates (with date validation)
- Owner-based permissions (users can only edit/delete their own projects)
- Filter and search by date or other fields (planned)

---

## 🚀 Quick Start Guide

### Step-by-step setup



```bash
# Clone the repository
git clone https://github.com/TarekMo334455/django-crowdfund-api.git
cd django-crowdfund-api

# Set up virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

🔗 API Endpoints
🔐 Authentication
POST /api/register/ — Register new user

POST /api/token/ — Obtain access and refresh tokens

POST /api/token/refresh/ — Refresh access token

📊 Projects
GET /api/projects/ — List all projects

POST /api/projects/ — Create a new project

GET /api/projects/{id}/ — Retrieve specific project

PUT /api/projects/{id}/ — Update project (owner only)

DELETE /api/projects/{id}/ — Delete project (owner only)


🛠 Tech Stack
Python 3.x

Django 3.2.25

Django REST Framework 3.15.1

Simple JWT 5.3.0

django-filter 23.5

SQLite (default dev DB)

📁 Project Structure

django-crowdfund-api/
├── core/                   # Main app for projects and users
│   ├── models.py           # Database models
│   ├── serializers.py      # API serializers
│   ├── views.py            # API views
│   ├── urls.py             # App-level routing
├── crowdfunding/           # Django project settings
│   ├── settings.py
│   ├── urls.py
├── requirements.txt        # Dependencies
├── manage.py
└── README.md
🌱 Planned Enhancements
🔐 Email activation during registration

🔄 Password reset via email

🔍 Advanced search/filter by keyword, date, amount

💸 Add donation/payment system

👤 User profiles with image and bio

📦 Deploy to Render or Heroku (PostgreSQL support)

✅ API tests and test coverage reports

🧾 Admin dashboard for full control

🤝 Contributing
Pull requests are welcome!
If you plan to make major changes, please open an issue first to discuss what you’d like to change or improve.

📄 License
This project is licensed under the MIT License.

