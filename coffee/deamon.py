from datetime import datetime
import time
import redis

from coffee.config import app_config, pool

DEBUG = 1
PIN = 14

r = redis.Redis(connection_pool=pool)


def get_last_start(previous, is_on):
    if is_on and not previous['status'] and\
       datetime.now() > datetime.strptime(previous['last_start'], '%Y-%m-%d %H:%M'):
        return datetime.now().strftime('%Y-%m-%d %H:%M')
    else:
        return previous['last_start']


def update_status(is_on):
    previous = r.hgetall('coffeestatus')
    if not 'status' in previous:
        previous = {
            'status': False,
            'last_start': '1977-11-21 12:00'
        }

    if not previous == is_on:
        r.hmset('coffeestatus', {
            'status': is_on,
            'last_start': get_last_start(previous, is_on)
        })


def main():
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)

    def rc_time(RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(RCpin, GPIO.IN)
        while (GPIO.input(RCpin) == GPIO.LOW):
            reading += 1
        return reading

    while True:
        if rc_time(PIN) < 1500:
            update_status(True)
        else:
            update_status(False)

main()
