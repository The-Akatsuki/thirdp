

# thirdp

thirdp is a _short description_. It is built with [Python][0] using the [Django Web Framework][1].

This project has the following basic apps:

* Payments
* Book Ride for corporate User

## Installation

### Quick start

To set up a development environment quickly, first install Python. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ virtualenv venv`
    2. `$ . venv/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

copy `/local.env.example` to `/local.env` in src/thirdp/setting

configure your database setting in local.env

Run migrations:

    python manage.py migrate
   
Run it on apache

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
