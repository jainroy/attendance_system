Attendance System (Django)
Setup
Clone this repository and enter the directory:

powershell
git clone https://github.com/jainroy/attendance_system.git
cd attendance_system
Create a virtual environment and install dependencies:

powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
Run migrations:

powershell
python manage.py makemigrations
python manage.py migrate
Create a superuser (for admin access):

powershell
python manage.py createsuperuser
Run the server locally:

powershell
python manage.py runserver
Access the application at:
http://localhost:8000/