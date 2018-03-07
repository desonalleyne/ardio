from nanpy import ArduinoApi, SerialManager
arduino = ArduinoApi(connection=SerialManager())
from time import sleep

class DigitalOut(object): 
    def __init__(self, pin, name, pinType=None):
        self.pin = pin
        self.state = False
        arduino.pinMode(pin, arduino.OUTPUT)
        if pinType == None:
            pinType=self.__class__.__name__
        else:
            self.name = "{} Pin ({}, {})".format(name, pinType, pin)

    def on(self):
        arduino.digitalWrite(self.pin, arduino.HIGH)
        self.state = True
        print "{} switch turned on".format(self.getName())

    def off(self):
        arduino.digitalWrite(self.pin, arduino.LOW)
        self.state = False
        print "{} switch turned off".format(self.getName())

    def toggle(self):
        if self.state == arduino.LOW:
            self.state = arduino.HIGH
        else:
            self.state = arduino.LOW
        arduino.digitalWrite(self.pin, self.state)
        print "{} toggled to {}".format(self.name, self.state)

    def dim(self, dimVal):
        arduino.analogWrite(self.pin, dimVal)
        self.state = dimVal

    def getState(self):
        return self.state

    def setState(self, state):
        arduino.digitalWrite(self.pin, state)
        self.state = state

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name
"""
s = DigitalOut(3)
s.on()
sleep(5)
s.off()
s.off()
"""
