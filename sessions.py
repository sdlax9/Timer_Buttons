from gpiozero import Button, LED, LEDBoard
from time import sleep

from typing import List

from config import buttons
from buttons import PlayerButton

class Session():
    '''Class for game session'''

    def __init__(self):
        self.player_buttons = []
        self.session_state = None
        self.current_player = 0

    def setup(self):
        '''Initializes session setup'''
        self.session_state = 'setup'


    def add_player_button(self, button: PlayerButton):
        '''Append PlayerButton to buttons'''
        self.player_buttons.append(button)
    
        
    def end():
        pass # TODO