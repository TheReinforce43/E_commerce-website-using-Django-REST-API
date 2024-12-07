# E-Commerce Project Using Django REST Framework

A Django-based application to manage products, brands, and categories, complete with an API and relational data handling.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Manage products with associated brands and categories.
- Optimized database queries using `select_related` for better performance.
- RESTful APIs for CRUD operations on products, brands, and categories.
- Extensible design for future features.
- Integrated admin panel for easy management.

---

## Requirements

- **Python 3.8+**
- **Django 4.0+**
- **Database**: PostgreSQL/MySQL/SQLite (Configurable)
- **Dependencies**: Listed in `requirements.txt`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/django-product-management.git
   cd django-product-management
Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install project dependencies:

bash
Copy code
pip install -r requirements.txt
Configure your database in settings.py.

Run migrations to set up the database schema:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a superuser:

bash
Copy code
python manage.py createsuperuser
Start the development server:

bash
Copy code
python manage.py runserver
Access the application at http://127.0.0.1:8000/.

Usage
Admin Panel: Manage products, brands, and categories from the admin interface at http://127.0.0.1:8000/admin/.
API Endpoints: Interact with the system programmatically using the provided RESTful APIs.
API Endpoints
Products
List Products: GET /api/products/
Retrieve Product: GET /api/products/<id>/
Create Product: POST /api/products/
Update Product: PUT /api/products/<id>/
Delete Product: DELETE /api/products/<id>/
Brands
List Brands: GET /api/brands/
Retrieve Brand: GET /api/brands/<id>/
Create Brand: POST /api/brands/
Update Brand: PUT /api/brands/<id>/
Delete Brand: DELETE /api/brands/<id>/
Categories
List Categories: GET /api/categories/
Retrieve Category: GET /api/categories/<id>/
Create Category: POST /api/categories/
Update Category: PUT /api/categories/<id>/
Delete Category: DELETE /api/categories/<id>/
 management with `ForeignKey` and `related_name` usage.
- Optimized database queries using `select_related`.
- Robust API for CRUD operations on products, brands, and categories.
- Easy-to-extend structure for future enhancements.

---

## Requirements

- **Python 3.8+**
- **Django 4.0+**
- **Database**: PostgreSQL e (Configurable)
- **Dependencies**: Listed in `requirements.txt`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TheReinforce43/E_commerce-website-using-Django-REST-API.git
   cd E_commerce_project
