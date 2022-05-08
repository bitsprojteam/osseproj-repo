#!/bin/bash

python manage.py makemigrations
python manage.py migrate
gunicorn project.wsgi --bind :8030