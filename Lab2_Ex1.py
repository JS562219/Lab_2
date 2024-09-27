# This code is built from Peter Hinch's micropython-micro-gui, section 2.1 of the README
import hardware_setup # Instantiate display, setup color LUT (if present) from gui.core.ugui import Screen, ssd
from gui.widgets import Label, Button, CloseButton
from gui.core.writer import Writer #Monochrome display
from gui.core.writer import CWriter

#Font for Cwriter
import gui.fonts.arialle as arialle
from gui.core.colors import *
from machine import Pin, ADC, PWM

ledPin = Pin(1,Pin.OUT)

class BaseScreen(Screen):

    def __init__(self):

        def my_callback(button, arg): 
            print("Button pressed",arg) 

        def button_on (button,arg): 
            ledPin.on()

        def button_off(button,arg):
            ledPin.off()

        super().__init__()
        # wri = Writer(ssd, arial10, verbose=False)
        wri = CWriter(ssd, arial10, GREEN, BLACK, verbose=False)
        col = 2
        row = 2
        Label(wri, row, col, 'Simple Demo')
        row = 20
        Button (wri, row, col, text='Yes', callback=button_on, args=('Yes',)) 
        col += 60
        Button (wri, row, col, text='No', callback=button_off, args=('No',)) 
        CloseButton(wri) # Quit the application


def test():
    print('Testing micro-gui...')
    Screen.change(BaseScreen)

test()
