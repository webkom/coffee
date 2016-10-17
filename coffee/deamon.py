#!/home/pi/coffee/venv/bin/python

import os
import sys
import time

from coffee.models import Status

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


DEBUG = 1

# The GPIO pin the button is connected to
BUTTON_PIN = 7
# The GPIO pin the button's LED is connected to
LED_PIN = 4


def main():
    import RPi.GPIO as GPIO

    status = Status()

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED_PIN, GPIO.OUT, initial=1)

    # Blink the LED, leave off
    def blink_led(num_blinks, blink_duration, blink_pause):
        for b in range(num_blinks):
            GPIO.output(LED_PIN, 1)
            time.sleep(blink_duration)
            GPIO.output(LED_PIN, 0)
            time.sleep(blink_pause)
        GPIO.output(LED_PIN, 0)

    # Listen for button presses
    while True:
        input_value = GPIO.input(BUTTON_PIN)
        if input_value == False:
            status.update(True)
            blink_led(3, 0.3, 0.2)
            status.update(False)
        time.sleep(0.1)

main()
