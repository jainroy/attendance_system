# Attendance System (Django)

## Setup

1. Clone this repository and enter the directory:
    git clone <repo-url>
    cd attendance_system

2. Create virtual environment and install dependencies:
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

3. Run migrations:
    python manage.py makemigrations
    python manage.py migrate

4. Create a superuser (for admin access):
    python manage.py createsuperuser

5. Run server locally:
    python manage.py runserver

6. Access at http://localhost:8000/
