import RPi.GPIO as GPIO
import time
import os
from flask import Flask
from flask import request

app = Flask(__name__)


# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

relayPin = 37
relayPin2 = 33

# set up GPIO output channels
GPIO.setup(relayPin, GPIO.OUT)
GPIO.output(relayPin,GPIO.HIGH)

GPIO.setup(relayPin2, GPIO.OUT)
GPIO.output(relayPin2,GPIO.HIGH)

@app.route("/opendoor2")
def abrePorta():

    GPIO.output(relayPin2,GPIO.LOW)
    time.sleep(5)
    GPIO.output(relayPin2,GPIO.HIGH)
    print("Welcome2!")
    return "Welcome2!"

@app.route("/opendoor")
def abrePorta():

    GPIO.output(relayPin,GPIO.LOW)
    time.sleep(5)
    GPIO.output(relayPin,GPIO.HIGH)
    print("Welcome!")
    return "Welcome!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
