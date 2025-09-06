import pigpio
from time import sleep

# Connect to local Pi GPIO daemon
pi = pigpio.pi()

if not pi.connected:
    exit()

servo_pin = 18  # GPIO pin connected to the servo

# Define pulse widths for servo positions
MIN_PULSE_WIDTH = 500  # Corresponds to 0 degrees
MID_PULSE_WIDTH = 1500  # Corresponds to 90 degrees
MAX_PULSE_WIDTH = 2500  # Corresponds to 180 degrees

# Move servo from 0 to 90 degrees
pi.set_servo_pulsewidth(servo_pin, MIN_PULSE_WIDTH)
sleep(2)
pi.set_servo_pulsewidth(servo_pin, MID_PULSE_WIDTH)
sleep(2)

# Move servo from 90 to 0 degrees
pi.set_servo_pulsewidth(servo_pin, MAX_PULSE_WIDTH)
sleep(2)
pi.set_servo_pulsewidth(servo_pin, MID_PULSE_WIDTH)
sleep(2)

# Turn off the servo
pi.set_servo_pulsewidth(servo_pin, 0)

# Disconnect from the Pi
pi.stop()
