import Controller
#import StreamingVoice.js

from Naked.toolshed.shell import execute_js, muterun_js

class V2Input:
    def __init__(self):
        self.Control = Controller()
        Main()
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
    #run StreamingVoice.js to create the audio input and stream
    response = execute_js('StreamingVoice.js')
    #if response.exitcode == 0:
    #    print(response.stdout)
    #else:
      # sys.stderr.write(response.stderr)
    print(response)

if __name__ == "__main__":Main()
