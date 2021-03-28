import pyvjoy
#import js2py #https://github.com/PiotrDabkowski/Js2Py
#use vJoy

class Controller:
#Setup the controller in vJoy
    def __init__(self):
        self.p1 = setup(1)
        main()

    def setup(Num):
        done = False
        while done == False:
            try:
                Controller = pyvjoy.VJoyDevice(Num)
                done = True
            except vJoyException:
                Num = Num+1
            if (Num >= 4):
                print("No Avaliable VJoy Devices")
                break

    def reset():
        p1.reset()

    def main():
        p1.set_button(2,1)
