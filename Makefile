PYTHON_VERSION := $(shell cat .python-version)

test: pip-dev
	@python3 -m pytest

pyenv:
	pyenv install --skip-existing "$(PYTHON_VERSION)"

export CUSTOM_COMPILE_COMMAND = make pip-compile

requirements.txt: requirements.in
	python3 -m piptools compile -q requirements.in -o requirements.txt

requirements-dev.txt: requirements.in requirements-dev.in
	python3 -m piptools compile -q requirements-dev.in requirements.in -o requirements-dev.txt

pip-compile: requirements.txt requirements-dev.txt

pip: venv requirements.txt
	python3 -m pip install -r requirements.txt | (grep -v 'Requirement already satisfied' || true)

pip-dev: venv requirements-dev.txt
	python3 -m pip install -r requirements-dev.txt | (grep -v 'Requirement already satisfied' || true)

venv: pyenv
	python3 -m venv venv

.PHONY: \
	pip-compile-requirements \
	pip-compile-requirements-dev \
	pipe-compile \
	pip \
	pip-dev \
	pyenv \
	test \
	venv
