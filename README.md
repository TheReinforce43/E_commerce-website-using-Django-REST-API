
# E-Commerce Project Using Django REST Framework

A Django-based application to manage products, brands, and categories, complete with APIs for CRUD operations and relational data handling.

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

- Comprehensive product, brand, and category management with `ForeignKey` and `related_name` usage.
- Optimized database queries using `select_related` for performance improvements.
- RESTful APIs for CRUD operations on products, brands, and categories.
- Extensible design for future enhancements.
- Integrated admin panel for easy management.

---

## Requirements

- **Python 3.8+**
- **Django 4.0+**
- **Database**: PostgreSQL/MySQL/SQLite (Configurable)
- **Dependencies**: Listed in `requirements.txt`

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TheReinforce43/E_commerce-website-using-Django-REST-API.git
   cd E_commerce_project
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install project dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database**:
   Update your database settings in `settings.py`.

5. **Run migrations to set up the database schema**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:  
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.

---

## Usage

- **Admin Panel**: Manage products, brands, and categories via the admin interface at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
- **API Endpoints**: Interact with the system programmatically using the provided RESTful APIs.

---

## API Endpoints

### Products
- **List Products**: `GET /api/products/`
- **Retrieve Product**: `GET /api/products/<id>/`
- **Create Product**: `POST /api/products/`
- **Update Product**: `PUT /api/products/<id>/`
- **Delete Product**: `DELETE /api/products/<id>/`

### Brands
- **List Brands**: `GET /api/brands/`
- **Retrieve Brand**: `GET /api/brands/<id>/`
- **Create Brand**: `POST /api/brands/`
- **Update Brand**: `PUT /api/brands/<id>/`
- **Delete Brand**: `DELETE /api/brands/<id>/`

### Categories
- **List Categories**: `GET /api/categories/`
- **Retrieve Category**: `GET /api/categories/<id>/`
- **Create Category**: `POST /api/categories/`
- **Update Category**: `PUT /api/categories/<id>/`
- **Delete Category**: `DELETE /api/categories/<id>/`

---

## Database Schema

### ProductModel
| Field         | Type         | Description              |
|---------------|--------------|--------------------------|
| category      | ForeignKey   | Links to `CategoryModel` |
| brand         | ForeignKey   | Links to `BrandModel`    |
| name          | CharField    | Unique product name      |
| price         | DecimalField | Product price            |
| quantity      | IntegerField | Stock quantity           |
| created_at    | DateTimeField| Auto-added on creation   |
| updated_at    | DateTimeField| Auto-updated on change   |

---

## Contributing

We welcome contributions to improve this project!

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Submit a pull request for review.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For questions, suggestions, or issues, please contact:  
**[your-email@example.com](mailto:your-email@example.com)**
