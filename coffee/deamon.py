#!/home/pi/coffee/venv/bin/python

import os
import sys
import time

from coffee.models import Status

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


DEBUG = 1
PIN = 14


def main():
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
    status = Status()

    def rc_time(RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(RCpin, GPIO.IN)
        while (GPIO.input(RCpin) == GPIO.LOW):
            reading += 1
            if reading > 5000:
                return reading
        return reading

    while True:
        if rc_time(PIN) <= 5000:
            status.update(True)
        else:
            status.update(False)

main()
