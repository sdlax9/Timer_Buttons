from gpiozero import LED
from gpizero import Button
from gpiozero import LEDBoard
from time import sleep

from typing import List

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
        pass # TODO


class AcceptButton():
    '''Class for the accept button'''

    def __init__(self, button_pin: int):
        self.button = Button(button_pin)


class Session():
    '''Class for game session'''

    def __init__(self):
        self.player_buttons = []
        self.session_state = None

    def setup(self):
        '''Initializes session setup'''
        self.session_state = 'setup'
        

    def add_player_button(self, button: PlayerButton):
        '''Append PlayerButton to buttons'''
        self.buttons.append(button)

    def start():
        self.session_state = 'game'
        pass # TODO
    
        
    def end():
        pass # TODO

