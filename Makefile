VIRTUALENV_DIR=.venv
PIP_DEPS=fastapi uvicorn typer rich

venv-init:
	test -d $(VIRTUALENV_DIR) || python3 -m venv $(VIRTUALENV_DIR)

# first time setting up the project? run this one
# initialize the venv and installs dependencies from requirements.txt
venv-install: venv-init
	. $(VIRTUALENV_DIR)/bin/activate && pip3 install -r requirements.txt

# saves any local venv changes to requirements.txt file
venv-freeze:
	. $(VIRTUALENV_DIR)/bin/activate && pip3 freeze > requirements.txt

# wipes out local venv
venv-clean:
	rm -rf $(VIRTUALENV_DIR)
	rm -rf __pycache__

# reinstall all pip deps from higher-order dependencies (see list at top of file) and refresh (git-versioned) requirements.txt
# note: appears to be no way to separate higher-level dependencies from the rest with requirements.txt
venv-refresh-reqs: venv-clean venv-init
	. $(VIRTUALENV_DIR)/bin/activate && pip3 install $(PIP_DEPS) && pip3 freeze > requirements.txt

# drops user into a Python REPL within virtualenv
# note: for this and the bash function below; exec replaces parent pid with child pid
venv-python:
	exec $(VIRTUALENV_DIR)/bin/python

# drops user into a Bash shell with venv activated
venv-bash:
	. $(VIRTUALENV_DIR)/bin/activate && exec bash

run-dev-server:
	. $(VIRTUALENV_DIR)/bin/activate && cd src && uvicorn rando-server:app --reload

test:
	. $(VIRTUALENV_DIR)/bin/activate && pytest
