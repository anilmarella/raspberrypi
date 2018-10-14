import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)


try:
    while True:
        if GPIO.input(4):
            GPIO.output(5, False)
            GPIO.output(17, True)
        else:
            GPIO.output(5, True)
            GPIO.output(17, False)
finally:
    GPIO.cleanup()
