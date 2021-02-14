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

### Local shared packages

Both the API server and CLI reference packages from `src/shared/`.

### How are dependencies organized?

There are a number of `make` functions to make working with `pip` a bit easier.

If you need to add dependencies, drop into a venv bash shell and use normal pip commands as usual:
```
make venv-bash
pip install <package-name>
# Ctrl^D to leave the venv shell
# then write the new deps to the requirements.txt file
make venv-freeze
```

## Setup Development Environment

### Prerequisites
```
# install python3

# clone and cd into the project
git clone git@github.com:cmrust/rando.git && cd rando

# initialize the virtualenv and install dependencies
make venv-install

# install docker and setup a local postgres instance
docker pull postgres
# setup a local directory for postgres data:
mkdir ${HOME}/postgres-data/
# run the docker postgres instance
docker run -d \
    --name dev-postgres \
    -e POSTGRES_PASSWORD=postgres \
    -v ${HOME}/postgres-data/:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres


psql postgresql://postgres:postgres@localhost:5432/postgres -c 'create user admin'
psql postgresql://postgres:postgres@localhost:5432/postgres -c 'create database rando'
psql postgresql://postgres:postgres@localhost:5432/postgres -c "ALTER USER admin WITH PASSWORD 'password'"
psql postgresql://postgres:postgres@localhost:5432/postgres -c 'grant all privileges on database rando to admin'
```

Connection string is then:
```
psql postgresql://admin:password@localhost:5432/rando
```

If you need to reset the database, then run this followed by the initialization commands above:
```
psql postgresql://postgres:postgres@localhost:5432/postgres -c 'drop database rando'
```

### Run the API server

```
make run-dev-server
```

### Run the CLI

```
./rando
```
