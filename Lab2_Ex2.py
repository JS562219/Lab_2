# This code is built from Peter Hinch's micropython-micro-gui, section 2.1 of the README
import hardware_setup  # Instantiate display, setup color LUT (if present)
from gui.core.ugui import Screen, ssd

from gui.widgets import Label, Button, CloseButton
#from gui.core.writer import Writer  # Monochrome display
from gui.core.writer import Cwriter

# Font for CWriter
import gui.fonts.arial10 as arial10
from gui.core.colors import *

from machine import Pin, ADC, PWM

led_RED = Pin(1, Pin.OUT)
led_GREEN = Pin(2, Pin.OUT)
led_BLUE = Pin(3, Pin.OUT)

class BaseScreen(Screen):
    def __init__(self):

        def my_callback(button, arg):
            print('Button pressed', arg)

        def button_on_red(button, arg):
            led_RED.on()
        def button_on_green(button, arg):
            led_GREEN.on()
        def button_on_blue(button,arg):
            led_BLUE.on()
        def button_off(button, arg):
            led_RED.off()
            led_GREEN.off() 
            led_BLUE.off()

        super().__init__()
        #wri = Writer(ssd, arialle, verbose=False)
        wri = Cwriter(ssd, arial10, GREEN, BLACK, verbose=False)
        col = 2
        row = 2
        Label(wri, row, col, 'Simple Demo')
        row = 20
        Button(wri, row, col, text='red', callback=button_on_red, args=('red',)) 
        row = 40
        Button(wri, row, col, text='green', callback=button_on_green, args=('green',)) 
        row = 60
        Button(wri, row, col, text='blue', callback=button_on_blue, args=('blue',)) 
        col += 60
        Button(wri, row, col, text='off', callback=button_off, args=('off',)) 
        CloseButton(wri) #Quit the application

def test():
    print('Testing micro-gui...')
    Screen.change(BaseScreen)

test()
