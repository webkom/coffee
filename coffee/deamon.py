import time

from coffee.models import Status

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

    # Blink the LED, leave in same state as when called
    def blink_led(num_blinks, blink_duration, blink_pause):
        initial = GPIO.input(LED_PIN)
        for b in range(num_blinks):
            GPIO.output(LED_PIN, not initial)
            time.sleep(blink_duration)
            GPIO.output(LED_PIN, initial)
            time.sleep(blink_pause)

    # Listen for button presses
    while True:
        input_value = GPIO.input(BUTTON_PIN)
        if not input_value:
            status.update(True)
            blink_led(3, 0.3, 0.2)  # equals sleep of 3 * (0.3 + 0.2) = 1.5 seconds
            GPIO.output(LED_PIN, 0)  # Turn off light to signalize button cannot be pushed
            time.sleep(300)  # Sleep for five minutes to avoid spamming the button
            status.update(False)
            GPIO.output(LED_PIN, 1)  # Turn on light when button is ready to be pushed again
        time.sleep(0.1)

main()
