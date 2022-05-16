import RPi.GPIO as GPIO
import time
PIR_PIN= 4
LED_1_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_1_PIN, GPIO.OUT)
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(LED_1_PIN, GPIO.LOW)
try:
    while True:
        time.sleep(0.1)
        print(GPIO.input(PIR_PIN))
        if GPIO.input(PIR_PIN)==1:
            GPIO.output(LED_1_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_1_PIN, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup