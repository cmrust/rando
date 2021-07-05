# rando·nnée

A long ramble in the countryside, by foot or bicycle.

## Where am I?

This project is an exploration of modern Python solutions I'm curating for myself as a reference kit.

At a high level, this is an implementation of an API server stack, a cli tool, some shared libraries between them and all of the common build processes that usually surround a project like that. The goal is to include everything necessary for spinning up new Python applications quickly, in a structured, maintainable, free (in every sense) and modern (at least as of now) fashion.

Functionality is demoed using bicycle geometry and frame design concepts.

## Details

### Why FastAPI?
- modern python, uses asyncio (asgi) and type hints
- appears to be performant (based on starlette)
- auto-documentation with swagger (enriched with type hints)

### Why Typer?
- similar implementation to FastAPI (same author)
- modern python, supports type hints
- autogeneration of shell autocompletion

### Why pytest?
- easy to use, run `pytest` and any tests named correctly will be run
- easy to learn, uses builtin Python assert function, no new syntaxes

### Why GitHub Actions?

There's no need for CD, or anything too fancy with regards to pipeline usage, in this project so far. Executing unit tests and running linters is enough for now and GitHub Actions is free and lives with the code removing any barriers to entry.

## Setup Development Environment

### Install Python 3

Makefile functions expect `python3` and `pip3` in PATH.

### Install Docker Desktop

Instructions should be accessible on docker.com.

### Install `psql` cli

On Mac, this can be done with Homebrew.

### Clone project and initialize deps
```
git clone git@github.com:cmrust/rando.git

cd rando

make venv-install
```

### Setup Local Dev Database

Start up and initialize the database:

```
docker pull postgres

# Launch database
make run-dev-database

# Creates admin user and rando database (only necessary once)
make init-dev-database

# If you need to drop/recreate the database later, run:
# make reset-dev-database

# If you need to shutdown the database later, run:
# make stop-dev-database
```

Create `.env` file in src folder:
```
echo 'DB_USER=admin
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
DB_DATABASE=rando' > ./src/.env
```

### Run the API server

```
make run-dev-server
```

### Run the CLI

```
./rando
```

## Developer Notes

### Local shared packages

Both the API server and CLI reference packages from `src/shared/`.

### How are dependencies organized?

There are a number of `make` functions to make working with `pip` a bit easier.

If you need to add dependencies, drop into a virtual environment bash shell and use normal pip commands as usual, then use this make command to freeze the venv:
```
make venv-bash
pip install <package-name>
# Ctrl^D to leave the venv shell
# then write the new deps to the requirements.txt file with:
make venv-freeze
```

### Manage DB migrations

To instantiate alembic and run the first pass on our database:

```
# TODO: Make these better
make venv-bash
cd src/
alembic init migrations
# update migrations/env.py with db connection info
# the following command will generate migration code: ./migrations/versions/*_initial_generation.py
alembic revision --autogenerate -m 'initial generation'
# then apply the changes
alembic upgrade head
# ... make more code changes that require db changes
alembic revision --autogenerate -m 'changed something'
# then apply the changes
alembic upgrade head
```
