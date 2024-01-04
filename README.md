# Django Auth

## Description

A very basic implementation of django auth.

## Installation

### Prerequisites
- Python (version 3.11.6)
- Django (version 5.0.1)

### Steps

1. Clone the repository.
   ```bash
   git clone https://github.com/RoyalBosS-Ayush/Django-Auth.git
   ```

2. Navigate to the project directory.
   ```bash
   cd Django-Auth
   ```

3. Create a virtual environment (optional but recommended).
   ```bash
   python -m venv env
   ```

4. Activate the virtual environment.
   - For Windows:
     ```bash
     env\Scripts\activate
     ```
   - For macOS and Linux:
     ```bash
     source env/bin/activate
     ```

5. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```

6. Apply database migrations.
   ```bash
   python manage.py migrate
   ```

7. Create a superuser (optional - for admin access).
   ```bash
   python manage.py createsuperuser
   ```

## Usage

1. Run the development server.
   ```bash
   python manage.py runserver
   ```

2. Access the application in your browser at `http://127.0.0.1:8000/`.
