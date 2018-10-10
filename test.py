import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup()
while True:
	GPIO.output(7, True)
    if GPIO.input(15):
    	GPIO.output(7, False)
    	GPIO.output(11, True)
    else: 
    	GPIO.output(11, False)

GPIO.cleanup()
