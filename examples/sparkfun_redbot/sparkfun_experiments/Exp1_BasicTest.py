#!/usr/bin/python
"""
  Exp1_BasicTest -- RedBot Experiment 1

  Time to make sure the electronics work! To test everything out, we're
  going to blink the LED on the board.
"""

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

WIFLY_IP_ADDRESS = None            # Leave set as None if not using WiFly
WIFLY_IP_ADDRESS = "137.112.217.88"  # If using a WiFly on the RedBot, set the ip address here.
if WIFLY_IP_ADDRESS:
    board = PyMata3(ip_address=WIFLY_IP_ADDRESS)
else:
    # Use a USB cable to RedBot or an XBee connection instead of WiFly.
    COM_PORT = None # Use None for automatic com port detection, or set if needed i.e. "COM7"
    board = PyMata3(com_port=COM_PORT)


def setup():
    """setup() function runs once at the very beginning."""
    board.set_pin_mode(13, Constants.OUTPUT)
    # The RedBot has an LED connected to pin 13.
    # Pins are all generic, so we have to first configure it
    # as an OUTPUT using this command.


def loop():
    """loop() function repeats over and over... forever!"""
    print("Blink sequence")
    board.digital_write(13, 1)  # Turns LED ON -- HIGH puts 5V on pin 13.
    board.sleep(0.500)          # "pauses" the program for 500 milliseconds
    board.digital_write(13, 0)  # Turns LED OFF -- LOW puts 0V on pin 13.
    board.sleep(0.500)          # "pauses" the program for 500 milliseconds
    # The total delay period is 1000 ms, or 1 second.


if __name__ == "__main__":
    setup()
    while True:
        loop()


# **********************************************************************
#  In Arduino, an LED is often connected to pin 13 for "debug" purposes.
#  This LED is used as an indicator to make sure that we're able to upload
#  code to the board. It's also a good indicator that your program is running.
# **********************************************************************
