# Restaurant Review System

🌐 **Language**

- 🇺🇸 English (Current)
- 🇹🇼 [繁體中文](README_zh.md)
- 
A Django-based web application that allows users to browse restaurants, view menus, and leave comments. This project was built as a learning exercise to practice modern Django development, including authentication, class-based views, ORM relationships, form handling, and user permissions.

---

## Features

* User registration
* User login and logout
* Restaurant list
* Restaurant detail page
* Restaurant menu display
* Comment submission
* Authentication and authorization
* Class-Based Views (CBVs)
* Django ORM relationships

---

## Tech Stack

* Python 3.12
* Django 5.x
* SQLite
* Bootstrap
* HTML
* CSS

---

## Project Structure

```text
restaurant/
│
├── manage.py
├── restaurant/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── menu/
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── permissions.py
    ├── admin.py
    ├── templates/
    └── migrations/
```

---

## Database Design

```
Restaurant
│
├── Food
│
└── Comment
```

### Restaurant

* Name
* Phone Number
* Address

### Food

* Name
* Price
* Description
* Spicy Flag

### Comment

* Visitor
* Email
* Content
* Created Time

---

## Authentication

Only authenticated users can:

* View restaurant details
* Browse restaurant menus
* Submit comments

User permissions are implemented using Django's authentication and authorization system.

---

## Installation

Clone the repository

```bash
git clone https://github.com/<your_username>/restaurant-review.git
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

macOS / Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run database migrations

```bash
python manage.py migrate
```

Create a superuser (optional)

```bash
python manage.py createsuperuser
```

Start the development server

```bash
python manage.py runserver
```

Open your browser

```
http://127.0.0.1:8000/
```

---

## Learning Objectives

This project demonstrates the following Django concepts:

* Django Models
* ForeignKey relationships
* Model permissions
* Class-Based Views
* Generic Views
* Django Forms
* Authentication
* Authorization
* Template rendering
* URL routing
* ORM CRUD operations

---

## Future Improvements

* Restaurant search
* Restaurant categories
* Rating system
* Pagination
* Image upload
* REST API (Django REST Framework)
* Docker support
* Unit tests
* CI/CD workflow with GitHub Actions

---

## Screenshots

Screenshots will be added after the UI is completed.

---

## License

This project is for educational purposes only.
