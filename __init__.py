from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
import serial
import time
import subprocess

class GoKnightsSkill(MycroftSkill):

    def __init__(self):
        super().__init__()
        self.learning = True

    def initialize(self):
        my_setting = self.settings.get('my_setting')

    @intent_handler('knights.intent')
    def handle_not_are_you_intent(self, message):
        serA = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        serA.flush()
        serA.write(b"charge")
        serB = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
        serB.flush()
        serB.write(b"charge")        
        serC = serial.Serial('/dev/ttyACM2', 9600, timeout=1)
        serC.flush()
        serC.write(b"charge")
        serD = serial.Serial('/dev/ttyACM3', 9600, timeout=1)
        serD.flush()
        serD.write(b"charge")
        self.speak_dialog("Charge on")

    def stop(self):
        pass

def create_skill():
    return GoKnightsSkill()
