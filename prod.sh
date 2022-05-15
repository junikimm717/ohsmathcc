#!/usr/bin/env bash

DIR="$(dirname "$(realpath "$0")")"
cd "$DIR" || exit 1

create_docker_compose() {
  SECRET_KEY="$(LC_CTYPE=C tr -dc '[:alpha:]' < /dev/random | fold -w 40 | head -n 1)"
  read -rp "Postgres User: " POSTGRES_USER
  read -rp "Postgres Password: " POSTGRES_PASSWORD
  sed -e "s/username/$POSTGRES_USER/g"\
      -e "s/password/$POSTGRES_PASSWORD/g"\
      -e "s/secretkey/$SECRET_KEY/g"\
      "$DIR/docker-compose.prod.yml" > "$DIR/docker-compose.yml"
}

help() {
  cat <<EOF

Usage: ./prod.sh [OPTIONS]

Script that sets up the ohsmathcc app for production.

Options:
-h, --help    Display this message
-a, --admin   Create a superuser
-d, --deploy  Deploy

EOF
}

DEPLOY=0
ADMIN=0

for arg in "$@"; do
  case "$arg" in
    --help|-h)
      help
      exit 0
    ;;
    --deploy|-d)
      DEPLOY=1
    ;;
    --admin|-a)
      ADMIN=1
    ;;

    *)
      echo "Unknown option $arg"
      exit 1
    ;;
  esac
done

if ! test -f "$DIR/docker-compose.yml"; then
  create_docker_compose
fi

if test $DEPLOY -eq 1 && test $ADMIN -eq 0 && ! test -d "$DIR/.postgres/postgres-data-prod"; then
  echo "I won't let you deploy if you don't have at least one admin account."
  exit 1
fi

if test $DEPLOY -eq 1; then
  docker-compose up -d --build
fi

if test $ADMIN -eq 1; then
  if test $DEPLOY -ne 1; then
    echo "You cannot create admin without the container running first."
    echo "Note: Don't use the --admin option if you already have an accessible admin account up."
    exit 1
  else
    docker-compose exec web python manage.py createsuperuser
  fi
fi
