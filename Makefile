setup:
	virtualenv venv
	venv/bin/pip install -r requirements/dev.txt
	cp example_config .coffeerc

run:
	PYTHONPATH=$(shell pwd) venv/bin/python coffee/server.py

test:
	PYTHONPATH=$(shell pwd) venv/bin/python coffee/tests.py

update:
	git fetch && git reset --hard origin/master
	venv/bin/pip install -r requirements/base.txt
	node_modules/.bin/gulp
