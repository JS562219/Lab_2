
import hardware_setup #Instantiate display, setup color LUT (if present) 
from gui.core.ugui import Screen, ssd

from gui.widgets import Label, Button, CloseButton, Adjuster
#from gui.core.writer import Writer #Monochrome display
from gui.core.writer import Cwriter

#Font for Cwriter
import gui.fonts.arialle as arialle
from gui.core.colors import *

from machine import Pin, ADC, PWM

led_RED = PWM(Pin(1), freq = 20000000)
led_GREEN = PWM(Pin(2), freq = 20000000)
led_BLUE = PWM(Pin(3), freq = 20000000)

class BaseScreen(Screen):

        def __init__(self):
              
            def my_callback(button, arg): 
                print('Button pressed', arg)

        super().__init__()
        # wri = Writer(ssd, arial10, verbose=False)
        wri = CWriter(ssd, arial10, GREEN, BLACK, verbose=False)

        col = 2 
        row = 2


        self.lbl1 = Label(wri, row, col, 60, bdcolor=RED)
        a = Adjuster(wri, row, self.lbl1.mcol + 2, fgcolor=RED, 
                      callback=self.adj1_callback)
        Label(wri, row, a.mcol + 2, "RED")
        row = self.lbl1.mrow + 5
        self.lbl2 = Label(wri, row, col, 60, bdcolor=RED)
        a = Adjuster(wri, row, self.1b12.mcol + 2,
                     fgcolor=RED, value=0.5,
                     callback=self.adj2_callback)
        Label(wri, row, a.mcol + 2, "GREEN")
        row = self.lbl2.mrow + 5
        self.lbl3 = Label(wri, row, col, 60, bdcolor=YELLOW)
        a = Adjuster (wri, row, self.1b13.mcol + 2, fgcolor=YELLOW,
                     callback=self.adj3_callback)
        Label(wri, row, a.mcol + 2, "BLUE")

        CloseButton(wri)

    def adj1_callback(self, adj): 
        v = adj.value()
        led_RED.duty_u16(int(v*65535))
        print(v)
        self.lbl1.value(f"{v:4.2f}")

    def adj2_callback(self, adj): 
        v = adj.value()
        led_GREEN.duty_u16 (int(v*65535)) 
        print(v)
        self.lbl2.value(f"{v:4.2f}")

    def adj3_callback(self, adj):
        v = adj.value()
        led_BLUE.duty_u16 (int(v*65535)) 
        print(v)
        self.lbl3.value(f"{v:4.2f}")

def test():
    print('Testing micro-gui...')
    Screen.change(BaseScreen)

test()
