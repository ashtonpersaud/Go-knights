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

    @intent_handler('goknights.intent')
    def handle_not_are_you_intent(self, message):
        self.speak_dialog("Charge on")
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.flush()
        ser.write(b"charge")
        
    @intent_handler('greeting.intent')
    def handle_not_are_you_intent(self, message):
        self.speak_dialog("greeting")
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.flush()
        ser.write(b"wave")

    def stop(self):
        pass

def create_skill():
    return GoKnightsSkill()
