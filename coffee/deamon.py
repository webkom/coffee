#!/home/pi/coffee/venv/bin/python

import time
from datetime import datetime
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from coffee.models import Status

DEBUG = 1
PIN = 14


def main():
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
    status = Status()
    on = False

    def rc_time(RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.setup(RCpin, GPIO.IN)
        while (GPIO.input(RCpin) == GPIO.LOW):
            reading += 1
            if on = True and reading > 5000: #ugly hack
                status.uppdate(False)
                on = False
        return reading

    while True:
        if rc_time(PIN) < 5000:
            status.update(True)
            on = True

main()
