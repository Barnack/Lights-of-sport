import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

GPIO.output(23,GPIO.HIGH)
time.sleep(60)
GPIO.output(23,GPIO.LOW)

GPIO.output(24,GPIO.HIGH)
time.sleep(15)
GPIO.output(24,GPIO.LOW)

PIO.output(23,GPIO.HIGH)
time.sleep(60)
GPIO.output(23,GPIO.LOW)

GPIO.output(24,GPIO.HIGH)
time.sleep(15)
GPIO.output(24,GPIO.LOW)

GPIO.output(23,GPIO.HIGH)
time.sleep(60)
GPIO.output(23,GPIO.LOW)

GPIO.output(24,GPIO.HIGH)
time.sleep(15)
GPIO.output(24,GPIO.LOW)

GPIO.output(18,GPIO.HIGH)
time.sleep(45)
GPIO.output(18,GPIO.LOW)

GPIO.cleanup()
