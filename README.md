# Baykar Tech UAV Rental Platform

This project is a web application built with Python, Django, PostgreSQL,for managing and renting UAVs for Technical Evaluation.

## Functionalities

### Membership and Login Screen

- Users can sign up for a new account.
- Existing users can log in to their accounts.

### UAV Management

- Add, delete, update, and list UAVs available for rent.
  - UAV Features: Brand, Model, Weight, Category.

### UAV Rental

- Add, delete, update, and list UAV rentals.
  - Rental Features: UAV, Start Date, End Date, Renting User.

### UAV Category

- Add, delete, update, and list UAV categories.
- Category Features: Name.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Django (version)
- PostgreSQL
- Django Rest Framework (version)

## Getting Started

- Clone the repository:

  ```bash
  git clone https://github.com/your-username/baykar-tech-uav-rental.git
  ```

## Navigate to the project directory:

- cd baykar-tech-uav-rental

## Install dependencies:

- pip install -r requirements.txt
- Apply migrations:

python manage.py migrate

## Run the development server:

- python manage.py runserver
- The project should be accessible at http://127.0.0.1:8000/.
