import Controller
import speech_recognition as sr
from Naked.toolshed.shell import execute_js, muterun_js
from datetime import datetime

class V2Input:
    def __init__(self):
        self.Control = Controller()

    #Turn a voice command into a single button press
    def Single_ButtonPress():
        print('but')
    def Single_ButtonHold():
        print('but')
    #Turn a voice command into a series of inputs
    def Multi_Button():
        print('but')
    #resets in case of mess-up situation
    def Reset():
        print('but')

    def CommandCatcher(VData):
        print(VData)

    #Main run loop
def Main():
    buttons = V2Input()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    filestring = dt_string + 'RecordingFile' +.wav
    file = open(filestring,w+)
    file.close
    record = sr.AudioFile(filestring)

    exit= False
    while exit == False
        with record as asource:
            r.adjust_for_ambient_noise(asource)
            audio = r.record(asource)
        r.recognize_sphinx(audio)

if __name__ == "__main__":Main()
