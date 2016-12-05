Django non-profit
=================

[![Build Status](https://travis-ci.org/NBajanca/django-non-profit.svg?branch=master)](https://travis-ci.org/NBajanca/django-non-profit)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/78f2889c44324f26a46629cef775a6ed)](https://www.codacy.com/app/NBajanca/django-non-profit?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=NBajanca/django-non-profit&amp;utm_campaign=Badge_Coverage)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/78f2889c44324f26a46629cef775a6ed)](https://www.codacy.com/app/nbajanca_first/django-non-profit?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=NBajanca/django-non-profit&amp;utm_campaign=Badge_Grade)


Django non-profit is a web application built with Django that will be used as a management platform for a non-profit. It is being developed in [REFOOD CASCAIS CPR](http://www.re-food.org/pt/nucleos/portugal/lisboa/cascais-cpr), and the first release will be out in December!

The objective is to create a web-application that may be customized and expanded as wished. Not only for Re-food but any non-profit. The final product will be independent working modules (Django Apps) that will be decoupled when generic enough, so they are reusable. The first one will be django-volunteers!


## How to get started (easy way):
First of all, you should know [Python](https://www.python.org/) and [Django](https://www.djangoproject.com/), at least the basics.

1. Download, Fork or Clone this repository.
2. In the main directory create a file named ``db.sqlite3``.
3. Set the environmental variables. See the section above.
4. Migrate Django to create your DB: ``python manage.py migrate``
5. Run the server: ``python manage.py runserver``

It should be working by now, but it is sending you to the login page (And you have no account!)

6. Kill the server
7. Create a superuser: ``python manage.py createsuperuser``
8. Run the server again: ``python manage.py runserver``
9. Log in with your fresh credentials and explore the App!

### Notes
- You won't be able to submit any form with a catcha. [Sign up for reCAPTCHA](https://www.google.com/recaptcha/intro/index.html) and change your Env vars.
- You just need to change the Env vars if you want to use this in production.
- Go to the Development Section when you'r ready!

## Environmental Variables
Every configuration that is sectret or may change between deploys is set as an env var. See [this](https://12factor.net/config) if you want to understand why.

To get started (easy way) you may run this script in a python console:

        import os
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        DB_NAME = os.path.join(BASE_DIR, "db.sqlite3")
        
        os.environ.setdefault("DEBUG", "True")
        os.environ.setdefault("DB_ENGINE","django.db.backends.sqlite3")
        os.environ.setdefault("DB_NAME", str(DB_NAME))
        os.environ.setdefault("SECRET_KEY", "super-secure-django-key")
        os.environ.setdefault("RECAPTCHA_PUBLIC_KEY", "notvalid")
        os.environ.setdefault("RECAPTCHA_PRIVATE_KEY", "notvalid")

This defines the basic variables with basic and insecure configurations. 

#### Complete list of Environmental Variables
If a variable is not mandatory, the default value is in front of it. If you have a ``=`` and nothing in front of it the default value is ``''``

- SECRET_KEY [[Django Docs](https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-SECRET_KEY)]
- DEBUG = False
- ALLOWED_HOSTS = 
- Database:
    -  DB_ENGINE
    -  DB_NAME
    -  DB_USER = 
    -  DB_PASS = 
    -  DB_HOST = 
    -  DB_PORT = 
- LANGUAGE_CODE = pt-pt
- TIME_ZONE = UTC
- AXES_COOLOFF_TIME = 2 [[Axes Docs](https://django-axes.readthedocs.io/en/latest/configuration.html)]
- RECAPTCHA_PUBLIC_KEY
- RECAPTCHA_PRIVATE_KEY
- Email:
    - DEFAULT_FROM_EMAIL = webmaster@django-non-profit
    - EMAIL_SUBJECT_PREFIX = 
    - EMAIL_HOST = localhost
    - EMAIL_HOST_PASSWORD = 
    - EMAIL_HOST_USER = 
    - EMAIL_PORT= 25

## Features and Roadmap

The first release will allow (December 2016):

- The creation of volunteers both in Django admin and through a front-office.
- The volunteers should be able to change their personal information and its preferences (timetable)
- The timetable (a group of weekdays and time intervals) should be created through Django Admin, but volunteers should be able to define its preferences in the front-office.
- It should be possible to see a list the volunteers and to search them organized by schedules.
- The volunteers should be manually added by a manager a shift map may be created manually.

Ideas for the upcoming versions are welcomed and should be added in [Issues](https://github.com/NBajanca/django-non-profit/issues)

## Development

This app follows the [Twelve-Factor-App](https://12factor.net/) methodology, so give it a look. 

If you wish to help me developing it for Re-Food, send me an email (nunombajanca@gmail.com)! 
Find out more about [Re-food](http://www.re-food.org/pt) - This project is being implemented in Re-Food Cascais CPR where more than 300 volunteers help people in need by collecting and distributing the food excess in restaurants, events, and supermarkets.

If it for other project go ahead and fork it.

## Documentation
On the roadmap and will be out with the first release.

## Dependencies
Dependencies that must be met to use the application:

- [Django](https://www.djangoproject.com/) 1.10
- [django-axes](https://github.com/jazzband/django-axes) 2.3
- [django-ipware](https://github.com/un33k/django-ipware) 1.1
- [django-phonenumber-field](https://github.com/stefanfoulis/django-phonenumber-field) 1.1
- [django-recaptcha](https://github.com/praekelt/django-recaptcha) 1.1
- [django-dual-authentication](https://github.com/Zeioth/django-dual-authentication) 1.0

The rest of the dependencies come from these and are automatically installed with pip.
These dependencies are stated in requirements.txt, together with the ones needed for CI.

## License

[MIT](https://github.com/NBajanca/django-non-profit/blob/master/LICENSE)