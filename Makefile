setup:
	virtualenv venv
	venv/bin/pip install -r requirements.txt
	cp example_config .coffeerc

run:
	venv/bin/python server.py