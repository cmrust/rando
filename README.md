# rando·nnée

A long ramble in the countryside, by foot or bicycle.

## Where am I?

This project is an exploration of modern Python solutions I'm curating for myself as a reference kit.

At a high level, this is an implementation of an API server stack, a cli tool, some shared libraries between them and all of the common build processes that usually surround a project like that. The goal is to include everything necessary for spinning up new Python applications quickly, in a structured, maintainable, free (in every sense) and (at least as of now) modern fashion.

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

### Local shared packages

Both the API server and CLI reference packages from `/shared/`.

## Setup Development Environment

### Prerequisites
```
# install python3

# clone and cd into the project
git clone git@github.com:cmrust/rando.git && cd rando

# initialize the virtualenv and install dependencies
make venv-install
```

### API server

```
make run-dev-server
```

### CLI

```
./rando
```
