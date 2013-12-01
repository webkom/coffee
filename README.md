# coffee
[![Build Status](https://travis-ci.org/webkom/coffee.png?branch=master)](https://travis-ci.org/webkom/coffee)

An API to the Moccamaster at the Abakus office.

## Setup dev environment
```bash
git clone git@github.com:webkom/coffee.git
cd coffee
make
```

Run the project by running `make run`.

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
