
# Django Web Development – Advanced Architecture

A Django-based Course Management System demonstrating advanced Django concepts and application architecture.

## Features

### 1. Class-Based Views (CBVs)
- Course ListView
- Course DetailView
- Course CreateView
- Course UpdateView
- Course DeleteView
- LoginRequiredMixin for authentication
- User-specific course access control

### 2. Custom Middleware
- Request and response tracking
- User information logging
- Session-based visit counter
- HTTP method restrictions

### 3. Django Signals
- post_save signal on Student model
- Automatic student registration confirmation
- Signal registration using AppConfig.ready()

### 4. Django Sessions
- Total visit tracking
- Previous page tracking
- Individual page visit history
- Session cleanup during logout

### 5. Django Cookies
- Dark and Light theme preferences
- Persistent theme selection

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS

## Installation

1. Clone the repository:

   git clone <YOUR_GITHUB_REPOSITORY_URL>

2. Navigate to the project directory:

   cd Week15_Django_Advanced

3. Create a virtual environment:

   python -m venv venv

4. Activate the virtual environment:

   Windows:
   venv\Scripts\activate

5. Install dependencies:

   pip install -r requirements.txt

6. Apply migrations:

   python manage.py migrate

7. Create an administrator account:

   python manage.py createsuperuser

8. Start the development server:

   python manage.py runserver

9. Open your browser:

   http://127.0.0.1:8000/

## Project Structure

config/       - Project configuration
courses/      - Course and Student application
manage.py     - Django management utility

## Learning Objectives

This project demonstrates the practical implementation of Django Class-Based Views, Middleware, Signals, Sessions, Cookies, and authentication.

## Author

Course Practical – Week 15