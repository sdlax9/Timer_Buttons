from time import sleep
from functools import wraps

from gpiozero import Button, LED, LEDBoard



class PlayerButton():
    '''Class for player button and LED'''

    def __init__(self, color: str, button_pin: int, led_pin: int):
        self.color = color
        self.button = Button(button_pin)
        self.led = LED(led_pin)


    def led_on(self):
        '''Turns button LED on'''
        self.led.on()

    def led_off(self):
        '''Turns button LED off'''
        self.led.off()

    def led_flash(self, flashes: int, delay=0.05):
        ''''''
        for i in range(flashes):
            self.led_on()
            sleep(delay)
            self.led_off()
            sleep(delay)

    def button_pressed(self):
        print(f'{self.button.pin.number}')



class AcceptButton():
    '''Class for the accept button'''

    def __init__(self, button_pin: int):
        self.button = Button(button_pin)