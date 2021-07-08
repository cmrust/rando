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

### Why Gino?

Gino implements an async ORM (Object-relational mapping) for PostgreSQL, built on top of SQLAlchemy, the most popular ORM for Python.

SQLAlchemy comes with a large open source community providing excellent documentation and complex toolsets, such as Alembic for managing database migrations.

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
```bash
git clone git@github.com:cmrust/rando.git

cd rando

make venv-install
```

### Setup local dev database

Start up and initialize the database:

```bash
docker pull postgres

# Launch database
make run-dev-database

# Creates admin user and rando database (only necessary once)
make init-dev-database

# Migrates database to latest revision
make migrate-dev-database

# If you need to drop/recreate the database later, run:
# make reset-dev-database
# make migrate-dev-database

# If you need to shutdown the database later, run:
# make stop-dev-database
```

Create `.env` file in src folder:
```bash
echo 'DB_USER=admin
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
DB_DATABASE=rando' > ./src/.env
```

### Run the API server

```bash
make run-dev-server
```

### Run the CLI

```bash
./rando
```

## Developer Notes

### Local shared packages

Both the API server and CLI reference packages from `src/shared/`.

### Managing `pip` installations

There are a number of `make` functions to make working with `pip` a bit easier. Check out the comments in the [Makefile](Makefile) for more information.

For example, if you need to add dependencies just drop into a virtual environment bash shell and use normal pip commands per usual, before using this make command to freeze the `requirements.txt` file:
```bash
make venv-bash
pip install <package-name>
# Ctrl^D to leave the venv shell
# then write the new deps to the requirements.txt file with:
make venv-freeze
```

### Using Alembic

Alembic is a tool that can be used with SQLAlchemy to automate complex database migration processes.

Alembic code is kept in `src/alembic.ini` and `src/migrations/`.

Note: Alembic uses the same `src/.env` database credentials as the application server.

Common `alembic` commands are:
```bash
# To use the alembic cli, load virtual env shell and cd into place:
make venv-bash
cd ./src/

# Show current revision for a database
alembic current

# After making new changes to SQL models in the application code, generate migration code:
alembic revision --autogenerate -m 'useful comment goes here'
# The above command would generate the following migration script: ./migrations/versions/<rev>_useful_comment_goes_here.py

# List migration code revisions in order
alembic history

# Apply latest migration code to database
alembic upgrade head
```
