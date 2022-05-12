#!/usr/bin/env bash

DIR="$(dirname "$(realpath "$0")")"
create_docker_compose() {
  SECRET_KEY="$(LC_CTYPE=C tr -dc '[:alpha:]' < /dev/random | fold -w 40 | head -n 1)"
  read -rp "Postgres User: " POSTGRES_USER
  read -rp "Postgres Password: " POSTGRES_PASSWORD
  sed -e "s/username/$POSTGRES_USER/g"\
      -e "s/password/$POSTGRES_PASSWORD/g"\
      -e "s/secretkey/$SECRET_KEY/g"\
      "$DIR/docker-compose.prod.yml" > "$DIR/docker-compose.yml"
}

if ! test -f "$DIR/docker-compose.yml"; then
  create_docker_compose
fi

case "$1" in
  --deploy|-d)
    docker-compose up -d --build
    docker-compose exec web python manage.py createsuperuser
  ;;
esac
