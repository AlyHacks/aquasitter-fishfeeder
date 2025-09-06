import pigpio
from time import sleep

pi = pigpio.pi()

if not pi.connected:
    SystemExit("Pi not connected.")

gpio_pin = 18


ZERO_DEGREES = 500
NINTY_DEGREES = 1500
ONE_EIGHTY_DEGREES = 2500

def convert_ms_angle(angle):
    if angle < 0:angle = 0
    elif angle > 180:angle = 180
    pulse = ZERO_DEGREES + (angle*(1000/90))
    return int(pulse)

pi.set_servo_pulsewidth(gpio_pin, convert_ms_angle(90))
sleep(2)
pi.set_servo_pulsewidth(gpio_pin, convert_ms_angle(0))
sleep(2)

pi.set_servo_pulsewidth(gpio_pin, 0)
pi.stop()







