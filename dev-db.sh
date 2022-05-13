#!/bin/sh

DIR="$(realpath "$(dirname "$0")")"
docker-compose -f "$DIR/docker-compose.dev.yml" up -d