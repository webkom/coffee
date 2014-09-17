setup: venv
	venv/bin/pip install -r requirements/dev.txt

run:
	gulp
	PYTHONPATH=$(shell pwd) venv/bin/python coffee/server.py

test:
	PYTHONPATH=$(shell pwd) venv/bin/python coffee/tests.py

update:
	git fetch && git reset --hard origin/master
	venv/bin/pip install -r requirements/base.txt
	node_modules/.bin/gulp

venv:
	virtualenv venv


.cofferc:
	cp example_config .coffeerc

production: update test run
