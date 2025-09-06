from gpiozero import AngularServo
from time import sleep
#send servo a pwm = pulse width modulation signal
#width of pulse
#
servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)
enter = input()
#while True:
    #servo.angle = 90
    #sleep(2)
    #servo.angle = 0
    #sleep(2)
    #servo.angle = -90
    #sleep(2)

if enter.lower() == "go":
    servo.angle = 90
    sleep(2)
    servo.angle = 0
    sleep(2)