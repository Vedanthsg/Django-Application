# Django Application

This repository contains a minimal project built with **Django 5.1**. It provides a very small website with three pages: a home page, an about page and a contact page.

## Features
- Simple HTML templates located in `DjangoApp/templates/website/`
- Static CSS styling from `DjangoApp/static/`
- Standard Django configuration inside `DjangoApp/DjangoApp`

## Getting Started
1. Ensure Python 3.12 or later is available.
2. Install Django:
   ```bash
   pip install django==5.1
   ```
3. Run database migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```

Then open `http://localhost:8000/` in your browser.

## Project Structure
- `DjangoApp/` – Django project directory containing `manage.py`
- `DjangoApp/DjangoApp/` – settings and URL configuration
- `DjangoApp/templates/website/` – HTML templates
- `DjangoApp/static/` – static files such as CSS

Feel free to extend this project to suit your needs.
