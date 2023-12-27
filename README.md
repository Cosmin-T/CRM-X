# Ticket-X

## Overview

* This Django project is designed to provide a comprehensive system for managing records. It offers a user-friendly platform for users to register, add, update, and delete records, ensuring a seamless experience.

### Prerequisites

* Python 3.x
* Django 3.x
* Other libraries as required in the project dependencies.

### Installation

* Clone the repository to your local machine.
* Install required packages using `pip install -r requirements.txt`.

### Setting up a virtual environment

* Run `python -m venv venv` to create a virtual environment.
* Activate the virtual environment.

### Running the server

* Cd to where manage.py is.
* Start the Django development server using `python manage.py runserver`.

## Configuration

* Configure the settings.py file according to your requirements, including database settings, static and media files management.

## Usage

* Access the home page through the server's root URL.
* Register as a new user, log in, add, view, update, or delete records as needed.

## Running Tests

* Run tests using the `python manage.py test` command.

## Built With

* Django - The web framework used.
* Other libraries and frameworks as included in the project's requirements.

## Authors

* Cosmin-T

## License

* The project is licensed under the MIT License.

### Specific Project Adjustments:

**Admin:**

* Integrated the `Record` model into the Django admin for easy management.

**Apps:**

* Configured the application with the necessary Django configurations.

**Forms:**

* Customized user registration and record addition forms with appropriate fields and validation.

**Models:**

* Defined a `Record` model to store user records with fields such as first name, last name, subject, email, etc.

**URLs:**

* Mapped URLs to view functions for home, logout, register, individual records view, delete, add, and update records.

**Views:**

* Created views to handle authentication, record management, and user interactions with forms and models.
