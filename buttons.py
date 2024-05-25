from time import sleep
from functools import wraps
from typing import List

from config import BUTTON_LIST
from gpiozero import Button, LED


class PlayerButton(Button):
    '''Class for player button and LED'''

    def __init__(self, color: str, button_pin: int, led_pin: int):
        super().__init__(
            button_pin,
            hold_time=2,
        )
        self.color = color
        self.led = LED(led_pin)
        self.total_time = 0
        self.running = False
        self.is_disabled = False
        self.is_active = False
        self.is_player_turn = False

    def toggle_disabled(self):
        '''Toggles disabled state'''
        self.is_disabled = not self.is_disabled

    def led_on(self):
        '''Turns button LED on'''
        if not self.is_disabled:
            self.led.on()

    def led_off(self):
        '''Turns button LED off'''
        if not self.is_disabled:
            self.led.off()

    def led_toggle(self):
        '''Toggles button LED state'''
        self.led.toggle()

    def led_flash(self, flashes: int, delay: float = 0.05):
        '''Flashes LED a number of times'''
        if not self.is_disabled:
            for i in range(flashes):
                self.led_on()
                sleep(delay)
                self.led_off()
                sleep(delay)
    
    def toggle_player_turn(self):
        if not self.is_disabled:
            self.is_player_turn = not self.is_player_turn
            while self.is_player_turn:
                sleep(1)
                self.total_time += 1



class AcceptButton(Button):
    '''Class for the accept button'''

    def __init__(self, button_pin: int):
        super().__init__(
            button_pin,
            hold_time=5,
        )


def PlayerButtonBoard():
    '''Class for group of PlayerButtons'''

    def __init__(self, buttons: List[PlayerButton] = BUTTON_LIST):
        self.buttons=buttons
        

    def led_cycle(self, num: int = 1, delay: float = 0.5):
        '''Cycles the LEDs on and off in order'''
        for _ in range(num):
            for button in self.buttons:
                button.led_on()
                sleep(delay)
                button.led_off()

    def led_flash(self, num: int = 1, delay: float = 0.5):
        '''Flashes the LEDS on and off'''
        for _ in range(num):
            for button in self.buttons:
                button.led_on()
            sleep(delay)
            for button in self.buttons:
                button.led_off()
    
