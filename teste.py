import RPi.GPIO as GPIO
import time
import os


def acende_apaga(relayPin):
    GPIO.output(relayPin,GPIO.LOW)
    time.sleep(5)
    GPIO.output(relayPin,GPIO.HIGH)
    print("Welcome!")

if __name__ == "__main__":
    #to use Raspberry Pi board pin numbers
    GPIO.setmode(GPIO.BOARD)

    relayPin = 37

    # set up GPIO output channels
    GPIO.setup(relayPin, GPIO.OUT)
    GPIO.output(relayPin,GPIO.HIGH)

    acende_apaga(relayPin)
