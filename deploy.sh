#!/bin/sh

docker-compose -f ./docker-compose.prod.yml up -d --build
docker-compose -f ./docker-compose.prod.yml exec web python manage.py createsuperuser