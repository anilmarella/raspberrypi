import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

try:
    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        if GPIO.input(4):
            print("Switch off")
finally:
    GPIO.cleanup()
