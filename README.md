A Django web application for managing employee information through forms.

Table of Contents
-Features
-Installation  
-Usage 
-Configuration 


Features
- Add new employee records      
- View list of employees  
- Update / edit existing employee data  
- Delete employee entries  
- Built using Django and SQLite  
- Admin dashboard interface (via Django admin)  

- `employee/` — contains models, views, templates, and forms for employee operations  
- `operations/` — possibly contains auxiliary logic or utilities  
- `db.sqlite3` — default local database (for development)  
- `manage.py` — entry point for Django commands  


Installation
Follow these steps to run the project locally:
-Clone the repository
   bash
    git clone https://github.com/Nishesh1708/Employee-Form.git
    cd Employee-Form
-Create a virtual environment (recommended)
  bash
    python3 -m venv venv
    source venv/bin/activate     # on Linux / macOS
    venv\Scripts\activate        # on Windows
-Install dependencies
  bash
    pip install -r requirements.txt
-Apply database migrations
  bash
    python manage.py makemigrations
    python manage.py migrate
-Run the development server
  python manage.py runserver
-Open your browser and go to http://127.0.0.1:8000/.

Usage
-Use the built-in pages to add, view, edit, or delete employees.
-You can further extend the project to add search, pagination, authentication, etc.

Configuration
-settings.py — adjust ALLOWED_HOSTS, DEBUG, database settings if needed.
-Database — the default uses db.sqlite3. We may switch to PostgreSQL, MySQL, etc., by editing DATABASES setting.
-Static / media files — configure static roots and media directories as needed.
