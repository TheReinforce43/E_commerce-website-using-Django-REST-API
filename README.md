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
- Relational data management with `ForeignKey` and `related_name` usage.
- Optimized database queries using `select_related`.
- Robust API for CRUD operations on products, brands, and categories.
- Easy-to-extend structure for future enhancements.

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
