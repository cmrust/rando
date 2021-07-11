VIRTUALENV_DIR=.venv

venv-init:
	test -d $(VIRTUALENV_DIR) || python3 -m venv $(VIRTUALENV_DIR)

# first time setting up the project? run this one
# initialize the venv and installs dependencies from requirements.txt
venv-install: venv-init
	. $(VIRTUALENV_DIR)/bin/activate && \
		pip3 install --upgrade pip && \
		pip3 install -r requirements.txt

# saves any local venv changes to requirements.txt file
venv-freeze:
	. $(VIRTUALENV_DIR)/bin/activate && pip3 freeze > requirements.txt

# wipes out local venv
venv-clean:
	rm -rf $(VIRTUALENV_DIR)
	rm -rf __pycache__

# activates venv in the user's current shell
venv-activate:
	. $(VIRTUALENV_DIR)/bin/activate

# drops user into a Python REPL within virtualenv
# (note: for this and the bash function below, exec command replaces parent pid with child pid)
venv-python:
	exec $(VIRTUALENV_DIR)/bin/python

# drops user into a Bash shell with venv activated
venv-bash:
	. $(VIRTUALENV_DIR)/bin/activate && \
	export PYTHONDONTWRITEBYTECODE=1 && \
	exec bash

# runs local instance of app server
# PYTHONDONTWRITEBYTECODE disables writing *.pyc files - unnecessary for local dev
run-dev-server:
	export PYTHONDONTWRITEBYTECODE=1 && \
	. $(VIRTUALENV_DIR)/bin/activate && \
	cd src && \
	uvicorn rando_server:app --reload

# ensures local data directory exists before launching database container
run-dev-database:
	test -d $${HOME}/postgres-data/ || mkdir $${HOME}/postgres-data/
	docker run -d \
    	--name dev-postgres \
    	-e POSTGRES_PASSWORD=postgres \
    	-v $${HOME}/postgres-data/:/var/lib/postgresql/data \
    	-p 5432:5432 \
    	postgres

stop-dev-database:
	docker stop dev-postgres && docker rm dev-postgres

# configures user and database for initial db setup
init-dev-database:
	psql postgresql://postgres:postgres@localhost:5432/postgres -c 'create user admin'
	psql postgresql://postgres:postgres@localhost:5432/postgres -c "ALTER USER admin WITH PASSWORD 'password'"
	psql postgresql://postgres:postgres@localhost:5432/postgres -c 'create database rando'
	psql postgresql://postgres:postgres@localhost:5432/postgres -c 'grant all privileges on database rando to admin'
	psql postgresql://postgres:postgres@localhost:5432/postgres -c 'create database rando_test'
	psql postgresql://postgres:postgres@localhost:5432/postgres -c 'grant all privileges on database rando_test to admin'

# drops and recreates database
reset-dev-database:
	psql postgresql://postgres:postgres@localhost:5432/postgres -c 'drop database rando'
	psql postgresql://postgres:postgres@localhost:5432/postgres -c 'drop database rando_test'
	psql postgresql://postgres:postgres@localhost:5432/postgres -c 'create database rando'
	psql postgresql://postgres:postgres@localhost:5432/postgres -c 'create database rando_test'

# migrate dev database to head of alembic revisions
migrate-dev-database:
	export PYTHONDONTWRITEBYTECODE=1 && \
	. $(VIRTUALENV_DIR)/bin/activate && \
	cd src && \
	alembic upgrade head

# runs unit tests
# use python -m to run tests from ./src/ to implicitly add src dir to PYTHONPATH
test:
	. $(VIRTUALENV_DIR)/bin/activate && \
	cd src && \
	python -m pytest --cov=./ ../tests/
