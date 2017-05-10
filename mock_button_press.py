import time
import redis

from coffee.models import Status

status = Status()


# Blink the LED, leave in same state as when called
def mock_blink_led(num_blinks, blink_duration, blink_pause):
    for b in range(num_blinks):
        time.sleep(blink_duration)
        time.sleep(blink_pause)


def mock_button_press():
    status.update(True)
    mock_blink_led(3, 0.3, 0.2)  # equals sleep of 3 * (0.3 + 0.2) = 1.5 seconds
    time.sleep(300)  # Sleep for five minutes to avoid spamming the button
    status.update(False)

mock_button_press()
