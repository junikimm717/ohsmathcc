# OHS MathCC Management site

A Django-based site (infused with nix and docker) for keeping things organized
in the OHS Math Competition Homeroom.

## Starting up the Development Environment

### Installation (Simpler with Nix)

- You should have `virtualisation.docker.enable = true;` in your configuration
  file (probably `/etc/nixos/configuration.nix`).
- All other necessary packages are provided in the shell.nix.
- Run `nix-shell` with your working directory being in the root of this
  repository.
- Install all of the python dependencies with `poetry install`
- Run `source ./dev` (Done automatically in shell.nix), this sets the
  appropriate environmental variables and starts up the postgres develompent
  container.
- Copy over the sample environmental variables in `./clubapp/.env.example` to
  `clubapp/.env`
- Get developing!

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
# is this a development environment? (if this variable is unset, the environment
# is treated as production)
MATHCC_DEV='true'
```
