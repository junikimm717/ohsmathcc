#!/bin/sh

python manage.py migrate auth || exit 1
python manage.py migrate || exit 1
python manage.py collectstatic || exit 1
hypercorn -w 3 -b 0.0.0.0:8000 clubapp.asgi:application
