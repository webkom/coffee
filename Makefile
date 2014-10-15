BIN=node_modules/.bin
PIP=venv/bin/pip
PYTHON=venv/bin/python

setup: venv
	${PIP} install -r requirements/dev.txt

rpi: venv
	${PIP} install -r requirements/rpi.txt

run:
	${BIN}/gulp
	PYTHONPATH=$(shell pwd) ${PYTHON} coffee/server.py

test:
	PYTHONPATH=$(shell pwd) ${PYTHON} coffee/tests.py

update:
	git fetch && git reset --hard origin/master
	${PIP} install -r requirements/base.txt
	${BIN}/gulp

venv:
	virtualenv venv

.cofferc:
	cp example_config .coffeerc

production: update test run rpi
