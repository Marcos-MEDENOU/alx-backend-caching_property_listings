# Property Listings with Django and Redis Caching

This is a Django project that demonstrates property listings with Redis caching.

## Features

- Django 4.2 with PostgreSQL database
- Redis for caching
- Docker and Docker Compose for containerization
- Property model with title, description, price, location, and created_at fields

## Prerequisites

- Docker and Docker Compose installed on your system
- Python 3.8+ (for local development without Docker)

## Getting Started

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd alx-backend-caching_property_listings
   ```

2. Create a `.env` file in the project root with the following variables:
   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   DB_NAME=property_db
   DB_USER=property_user
   DB_PASSWORD=property_pass
   DB_HOST=db
   DB_PORT=5432
   REDIS_URL=redis://redis:6379/0
   ```

3. Build and start the containers:
   ```bash
   docker-compose up --build
   ```

4. Run migrations:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

6. Access the admin interface at http://localhost:8000/admin/

## Project Structure

- `alx_backend_caching_property_listings/` - Main Django project settings
- `properties/` - Property listings app
  - `models.py` - Property model definition
  - `urls.py` - URL routing for the properties API
  - `views.py` - API views (to be implemented)
- `docker-compose.yml` - Docker Compose configuration
- `Dockerfile` - Docker configuration for the Django app
- `requirements.txt` - Python dependencies
- `.env` - Environment variables (not version controlled)

## Development

To run the development server locally (without Docker):

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   python manage.py runserver
   ```

## License

This project is licensed under the MIT License.
