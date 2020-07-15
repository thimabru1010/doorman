import RPi.GPIO as GPIO  
import time
import os
from flask import Flask
from flask import request

app = Flask(__name__)


# to use Raspberry Pi board pin numbers  
GPIO.setmode(GPIO.BOARD)

relayPin = 37

# set up GPIO output channels  
GPIO.setup(relayPin, GPIO.OUT)
GPIO.output(relayPin,GPIO.HIGH)

@app.route("/opendoor")
def abrePorta():

    GPIO.output(relayPin,GPIO.LOW)  
    time.sleep(1)
    GPIO.output(relayPin,GPIO.HIGH)
    print("Welcome!")    
    return "Welcome!"
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')




