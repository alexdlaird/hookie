.PHONY: all virtualenv install nopyc clean test local validate-release upload

SHELL := /usr/bin/env bash
PYTHON_BIN ?= python

all: virtualenv install

virtualenv:
	@if [ ! -d "venv" ]; then \
		$(PYTHON_BIN) -m pip install virtualenv --user; \
		$(PYTHON_BIN) -m virtualenv venv; \
	fi

install: virtualenv
	@( \
		source venv/bin/activate; \
		python -m pip install -r requirements.txt -r requirements-dev.txt; \
	)

nopyc:
	find . -name '*.pyc' | xargs rm -f || true
	find . -name __pycache__ | xargs rm -rf || true

clean: nopyc
	rm -rf _build dist *.egg-info venv

test: install
	@( \
		source venv/bin/activate; \
		python `which nosetests` --with-coverage --cover-erase --cover-package=. --cover-html --cover-html-dir=_build/coverage; \
	)

local:
	@rm -rf *.egg-info dist
	@( \
		$(PYTHON_BIN) setup.py sdist; \
		$(PYTHON_BIN) -m pip install dist/*.tar.gz; \
	)

validate-release:
	@if [[ "${VERSION}" == "" ]]; then echo "VERSION is not set" & exit 1 ; fi

	@if [[ $$(grep "__version__ = \"${VERSION}\"" setup.py) == "" ]] ; then echo "Version not bumped in setup.py" & exit 1 ; fi
	@if [[ $$(grep "__version__ = \"${VERSION}\"" hookie/hookie.py) == "" ]] ; then echo "Version not bumped in hookie/hookie.py" & exit 1 ; fi

upload:
	@rm -rf *.egg-info dist
	@( \
		source venv/bin/activate; \
		python setup.py sdist; \
		python -m twine upload dist/*; \
	)
