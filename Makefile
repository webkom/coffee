setup:
	virtualenv venv
	venv/bin/pip install -r requirements.txt
	cp example_config .coffeerc

run:
	PYTHONPATH=$(shell pwd) venv/bin/python coffee/server.py

test:
	PYTHONPATH=$(shell pwd) venv/bin/python coffee/tests.py