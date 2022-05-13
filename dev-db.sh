#!/bin/sh

DIR="$(realpath "$(dirname "$0")")"

case "$1" in
  up|u)
    docker-compose -f "$DIR/docker-compose.dev.yml" up -d
    ;;
  down|d)
    docker-compose -f "$DIR/docker-compose.dev.yml" down
    ;;
  *)
    echo "Invalid command. must be either 'up' or 'down'"
    exit 1
    ;;
esac