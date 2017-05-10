# coffee [![Build Status](https://ci.abakus.no/api/badges/webkom/coffee/status.svg)](https://ci.abakus.no/webkom/coffee)

An API to the Moccamaster at the Abakus office.

## Raspberry Pi
### Setup
```bash
git clone git@github.com:webkom/coffee.git
cd coffee
pip install -r requirements/rpi.txt
```
Configure environment variables mentioned in `coffee/config.py`.
Make sure the `coffee` module is part of your `PYTHONPATH`.  

### Run
Run `python3 -m coffee.deamon` using your favorite daemonizer.


## Server
### Setup dev environment

You will need to have redis installed and configured. Here's [a guide for Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-redis-on-ubuntu-16-04).

```bash
git clone git@github.com:webkom/coffee.git
cd coffee
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements/base.txt
npm install
```

### Run the server
```bash
npm run build
python -m coffee.server
```

You can mock a button press by running `python mock_button_press.py`

### Run the tests
```bash
pip install tox
tox
```

## Use the API
### GET [kaffe.abakus.no/api/status](http://kaffe.abakus.no/api/status)
Return data of last time coffee was turned on.
##### Example response
HTTP/1.1 200 OK   
Content-Type: application/json

```json
{
  "coffee": {
    "status": true,
    "last_start": "2012-12-12 12:12",
    "time_since": {
	  "hours": 0,
	  "minutes": 0
	}
  }
}
```

### GET [kaffe.abakus.no/api/stats](http://kaffe.abakus.no/api/stats)
Return stats of usage of the coffee machine.
##### Example response
HTTP/1.1 200 OK   
Content-Type: application/json

```json
{
  "stats": {
    "2012-12-12": 3,
    "2012-12-13": 1,
    "2012-12-14": 7
  }
}
```
--------
MIT © webkom, Abakus Linjeforening
