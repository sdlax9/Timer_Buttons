from time import sleep

from typing import List

from config import BUTTON_LIST, ACCEPT_BUTTON, PLAYER_BUTTON_BOARD
from buttons import PlayerButton, AcceptButton, PlayerButtonBoard

class SessionState():
    '''Base class for session state'''

    def __init__(self, accept_button: AcceptButton = ACCEPT_BUTTON):
        self.accept_button = accept_button

    def startup_pattern():
        '''LED pattern on startup'''
        pass

    def set_accept_button_press(self):
        '''Set accept button press function'''
        pass

    def set_accept_button_hold(self):
        '''Set accept button hold function'''
        pass

    def set_player_button_press(self):
        '''Set player buttons press function'''
        pass

    def set_player_button_hold(self):
        '''Set player buttons hold function'''
        pass

    def start(self):
        '''Runs session state pattern and sets button functions'''
        self.startup_pattern()

class SetupState(SessionState):
    '''Startup session state'''

    def __init__(self, buttons: List[PlayerButton] = BUTTON_LIST):
        self.buttons = buttons

    def startup_pattern(self):
        '''Starting LED pattern'''
        pass # TODO

    def set_accept_button_press(self):
        '''Set accept button press function'''
        pass # TODO
        # End session state
        # Add active buttons to active_button_list
        # Initialize GameState

    def set_accept_button_hold(self):
        '''Set accept button hold function'''
        pass # TODO

    def set_player_button_press(self):
        '''Set player buttons press function'''
        pass # TODO
        # Toggle LED
        # Toggle is_active

    def set_player_button_hold(self):
        '''Set player buttons hold function'''
        pass # TODO

    def start(self):
        '''Start session state'''
        self.startup_pattern()

class GameState(SessionState):
    '''Startup session state'''

    def startup_pattern():
        '''Starting LED pattern'''
        pass # TODO

    def set_accept_button_press(self):
        '''Set accept button press function'''
        pass # TODO

    def set_accept_button_hold(self):
        '''Set accept button hold function'''
        pass # TODO

    def set_player_button_press(self):
        '''Set player buttons press function'''
        pass # TODO

    def set_player_button_hold(self):
        '''Set player buttons hold function'''
        pass # TODO

    def start(self):
        '''Start session state'''
        self.startup_pattern()




    

class Session():
    '''Class for session'''

    def __init__(
            self,
            buttons: List[PlayerButton] = BUTTON_LIST,
            accept_button: AcceptButton =  ACCEPT_BUTTON,
            session_state: SessionState = SetupState(),
        ):
            self.buttons = buttons
            self.accept_button = accept_button
            self.session_state = session_state

    
    def start(self):
        '''Initialize session'''

        self.session_state.start()

        if isinstance(self.session_state, SetupState):
            for button in self.buttons.values():
                button.when_held
        else isinstance(self.session_state, GameState):
            pass # TODO
