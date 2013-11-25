import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from coffee.config import pool
from coffee.models import Status

DEBUG = 1
PIN = 14


def main():
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
    status = Status(pool)

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
            status.update(True)
        else:
            status.update(False)

main()
