# coffee
[![Build Status](https://travis-ci.org/webkom/coffee.png?branch=master)](https://travis-ci.org/webkom/coffee)

An api to the moccamaster at the Abakus office.

## Setup dev environment
    git clone git@github.com:webkom/coffee.git
    make

Run the project by running `make run`.

## Use the API
### kaffe.abakus.no/api/status
Return data of last time coffee was turned on.
##### Example
```json
{
  "coffee": {
    "status": "on",
    "last_start": "2012-12-12 12:12",
  }
}
```

### kaffe.abakus.no/api/stats
Return stats of usage of the coffee machine. 
##### Example
```json
{
  "stats": {
    "2012-12-12": 3,
    "2012-12-13": 1,
    "2012-12-14": 7
  }
}
```
