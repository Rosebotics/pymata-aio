#!/usr/bin/python
"""
  Exp5_Bumpers -- RedBot Experiment 5

  Now let's experiment with the whisker bumpers. These super-simple switches
  let you detect a collision before it really happens- the whisker will
  bump something before your robot crashes into it.

  This sketch was written by SparkFun Electronics, with lots of help from
  the Arduino community.
  This code is completely free for any use.
  Visit https://learn.sparkfun.com/tutorials/redbot-inventors-kit-guide
  for SIK information.

  8 Oct 2013 M. Hord
  Revised 30 Oct 2014 B. Huang
  Revised 2 Oct 2015 L. Mathews
"""

import sys
import signal

from pymata_aio.pymata3 import PyMata3
from library.redbot import RedBotMotors, RedBotBumper


WIFLY_IP_ADDRESS = None            # Leave set as None if not using WiFly
WIFLY_IP_ADDRESS = "137.112.217.88"  # If using a WiFly on the RedBot, set the ip address here.
if WIFLY_IP_ADDRESS:
    board = PyMata3(ip_address=WIFLY_IP_ADDRESS)
else:
    # Use a USB cable to RedBot or an XBee connection instead of WiFly.
    COM_PORT = None # Use None for automatic com port detection, or set if needed i.e. "COM7"
    board = PyMata3(com_port=COM_PORT)

# Instantiate the motor control object. This only needs to be done once.
motors = RedBotMotors(board)

left_bumper = RedBotBumper(board, 3)  # initializes bumper object on pin 3
right_bumper = RedBotBumper(board, 11)  # initializes bumper object on pin 11

BUTTON_PIN = 12


def signal_handler(sig, frame):
    """Helper method to shutdown the RedBot if Ctrl-c is pressed"""
    print('\nYou pressed Ctrl+C')
    if board is not None:
        board.send_reset()
        board.shutdown()
    sys.exit(0)


def setup():
    signal.signal(signal.SIGINT, signal_handler)
    print("Experiment 5 - Bump sensors")


def loop():
    motors.drive(255)
    board.sleep(0.1)  # When using a wireless connection a small sleep is necessary

    left_bumper_state = left_bumper.read()
    right_bumper_state = right_bumper.read()
    if left_bumper_state == 0: # left bumper is bumped
        print("Left bump")
        reverse()
        turn_right()

    if right_bumper_state == 0: # left bumper is bumped
        print("Right bump")
        reverse()
        turn_left()


def reverse():
    """backs up at full power"""
    motors.drive(-255)
    board.sleep(0.5)
    motors.brake()
    board.sleep(0.1)


def turn_right():
    """turns RedBot to the Right"""
    motors.left_motor(-150)  # spin CCW
    motors.right_motor(-150)  # spin CCW
    board.sleep(0.5)
    motors.brake();
    board.sleep(0.1)  # short delay to let robot fully stop


def turn_left():
    """turns RedBot to the Left"""
    motors.left_motor(150)  # spin CCW
    motors.right_motor(150)  # spin CCW
    board.sleep(0.5)
    motors.brake();
    board.sleep(0.1)  # short delay to let robot fully stop


if __name__ == "__main__":
    setup()
    while True:
        loop()





