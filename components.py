from gpiozero import LED
from gpizero import Button
from gpiozero import LEDBoard
from time import sleep

class PlayerButton():
    '''Player button and led'''

    def __init__(self, color, button_pin, led_pin):
        self.color = color
        self.pin = pin
        self.button = Button(button_pin)
        self.led = LED(led_pin)


    def led_on(self):
        '''Turns button LED on'''
        self.led.on()

    def led_off(self):
        '''Turns button LED off'''
        self.led.off()

    
        