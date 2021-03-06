# OHS MathCC Management site

A Django-based site (infused with nix and docker) for keeping things organized
in the OHS Math Competition Homeroom.

It should be deployed [here](https://ohsmathc.club).

## Starting up the Development Environment

### With NixOS

- You should have `virtualisation.docker.enable = true;` in your configuration
  file (probably `/etc/nixos/configuration.nix`).
- All other necessary packages are provided in the shell.nix.
- Run `nix-shell` with your working directory being in the root of this
  repository (sets up environmental variables and activates the poetry shell).
- Install all of the python dependencies with `poetry install`
- Copy over the sample environmental variables in `./clubapp/.env.example` to
  `clubapp/.env`

### In other environments

- Have Docker, the latest possible version of docker-compose, Python, and Poetry
  installed on your system.
- Install all of the python dependencies with `poetry install`
- Run `source ./dev` (Done automatically in shell.nix), this sets the
  appropriate environmental variables.
- Copy over the sample environmental variables in `./clubapp/.env.example` to
  `clubapp/.env`

### Setting up the database (Both Types)

- Run `./dev-db.sh up`. This starts up a postgres docker container with all data
  being stored at `.postgres/postgres-data`.
- In order to stop the database, run `./dev-db.sh down`. All data will still be
  saved.

## Deploying a Production Server (in a VPS)

- Install Docker, the latest version of docker-compose, and Git on the system.
- Git clone this repository (and `cd` into it)
- Use the `prod.sh` script.

## The prod.sh script

NOTE: **Be very careful about not deleting your local `docker-compose.yml` file
if the container database is already running with critical data**. You may be
locked out if the database passwords don't match.

- To learn more about this script, run `prod.sh -h`.
- To just generate a ready `docker-compose.yml` file, run `./prod.sh`. The file
  will not be overwritten if it exists.
- To deploy the production containers, run `prod.sh -d`.
- To deploy the production containers _and create a superuser while doing so_,
  run `prod.sh -a -d`.

## All Environmental Variables

```sh
# sets the session secret key (using the django default for now)
SECRET_KEY='vf$(sc2(1umf&c(o+#b$&isk71&fm5h1o&tyd(9&-#)y%7n16d'
# these three environment variables are set in the development
# docker-compose.yml, so make sure to revise that if you want to change
# something.
POSTGRES_DB=ohsmathcc
POSTGRES_USER=username
POSTGRES_PASSWORD=password
# this is not actually required in development (used in docker containers e.g.)
POSTGRES_HOST=127.0.0.1
# is this a development environment? (if this variable is not set, the environment
# is treated as production)
MATHCC_DEV='true'
```
