from datetime import datetime
import time
import RPi.GPIO as GPIO
import redis

from coffee.config import app_config, pool

DEBUG = 1
GPIO.setmode(GPIO.BCM)
PIN = app_config['gpio_pin']

r = redis.Redis(connection_pool=pool)


def rc_time(RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading


def get_last_start(previous, is_on):
    if is_on and not previous['status'] and datetime.now() > datetime.strptime('%Y-%m-%d %H:%M'):
        return datetime.now().strftime('%Y-%m-%d %H:%M')
    else:
        return previous['last_start']


def update_status(is_on):
    previous = r.hgetall('coffeestatus')
    if not previous == is_on:
        r.hmset('coffeestatus', {
            'status': is_on,
            'last_start': get_last_start(previous, is_on)
        })


while True:
    if rc_time(PIN) < 1500:
        update_status(True)
    else:
        update_status(False)
