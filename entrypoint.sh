#!/bin/sh

python manage.py collectstatic || exit 1
python manage.py migrate || exit 1
gunicorn clubapp.wsgi -w 3 -b 0.0.0.0:8000