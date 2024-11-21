#**Django WEb-site SHOP**


![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

##**Description**
This project is a web site developed using the Django framework. It includes various features such as user authentication, content management, and integration with external APIs.


##**Features**
- User registration and authentication
- User profile management
- Create, edit, and delete content
- Integration with WeasyPrint for PDF document generation
- Responsive design for mobile devices
- 

##**Getting Started**
Follow these instructions to set up the project locally or using Docker.



**Prerequisites**
Make sure you have the following installed:
- Python (3.x) (if you are not using Docker)
- Docker and Docker Compose (if using Docker)
- 

##**Installation**


##**Option 1: Local Installation**


Clone the repository:
git clone https://github.com/vikivuki2003/web_site_django.git  
cd web_site_django  


Create a virtual environment:
python -m venv venv  
source venv/bin/activate  # On Windows use `venv\Scripts\activate`  


Install the dependencies:
pip install -r requirements.txt  


Set up the database:
Update your database configuration in settings.py. Then run the following commands to apply migrations:
python manage.py makemigrations  
python manage.py migrate  


Create a superuser (optional):
To access the Django admin interface:
python manage.py createsuperuser  

Run the development server:
python manage.py runserver  


Your application should now be accessible at http://127.0.0.1:8000/.



##**Option 2: Docker Installation**
Clone the repository:
git clone https://github.com/vikivuki2003/web_site_django.git  
cd web_site_django  


Build the Docker image:
docker-compose build  


Start the application:
docker-compose up  


Your application should be running and accessible at http://localhost:8000/.


Create a superuser (optional):
To access the Django admin interface, you may need to run the command inside the Docker container:
docker-compose exec web python manage.py createsuperuser  


##**Environment Variables**
You can configure environment variables in the .env file (make sure to provide this file). Here’s an example:
DEBUG=True  
DJANGO_SECRET_KEY=your_secret_key  
DATABASE_URL=postgres://user:password@db:5432/database_name  



##**Usage**
Once the server is running, you can:

Sign up or log in to access personalized features.
Navigate through the pages to explore the site's functionalities.
Use the admin dashboard to manage content (if set up).


##**Technologies Used**
This project is built using the following technologies:
Python
JavaScript
Ajax
CSS
HTML
Postgres
Celery Beat
Celery Result
Celery
Redis Broker
Django Htmx
Nginx
Gunicorn
API
Swagger and Redoc Docs
Celery Flower
Stripe
Yookassa
Django Rest Framework
Docker
Docker Compose
GitHub Actions
Git



##Future Improvements
This project is a work in progress and will be improved further.
