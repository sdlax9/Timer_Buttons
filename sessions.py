import random

from typing import List, Optional
from enum import Enum

from config import BUTTON_LIST, ACCEPT_BUTTON, PLAYER_BUTTON_BOARD
from buttons import PlayerButton, AcceptButton, PlayerButtonBoard

# --------------------
# Turn order Modes
# --------------------
"""
Select modes control how player turn order will be selected during the game

- Resume:           continue with the current active player
- Clockwise:        the next active player will be in clockwise order
- CounterClockwise: the next active player will be in counter clockwise order
- Random:           the next active player will be selected randomly and
                    proceed in clockwise order
- Selected:         the player order is selected by the players
"""

# class TOMode():
#     '''Base class for turn order mode'''

#     def __init__(
#             self,
#             buttons: List[PlayerButton],
#             button_board: PlayerButtonBoard,
#         ):
#         self.buttons = buttons
#         self.button_board = button_board
#         self.is_active = False
#         self.current_player = self._get_current_player()

#     def _get_current_player(self):
#         '''Get current player from button_board'''
#         current_player = None
#         for button in self.button_board:
#             if button.is_player_turn:
#                 current_player = button
#         return current_player

#     def _player_button_pressed(self):
#         '''Function when PlayerButton is pressed'''
#         pass

#     def _mode_pattern():
#         '''LED pattern on startup'''
#         pass

#     def _set_player_button_pressed(self):
#         '''Set player buttons press function'''
#         pass

#     def start():
#         '''Runs the mode pattern and sets button functions'''
#         pass

# class ResumeMode(TOMode):
#     '''Mode that continues with the current active player'''

#     def __init__(
#             self,
#             buttons: List[PlayerButton],
#             button_board: PlayerButtonBoard
#         ):
#         super().__init__(
#             buttons=buttons,
#             button_board=button_board
#         )

#     def _player_button_pressed(self, button: PlayerButton):
#         '''Function when PlayerButton is pressed. (Do nothing)'''
#         pass

#     def _mode_pattern(self):
#         '''LED pattern for mode. (Current player flashes)'''
#         while self.is_active and self.current_player is not None:
#             self.current_player.led_flash(delay=1)

#     def _set_player_button_pressed(self):
#         '''Set player buttons press function'''
#         for button in self.buttons:
#             button.when_pressed = self._player_button_pressed

#     def start(self):
#         '''Runs the mode pattern and sets button functions'''
#         self._set_player_button_pressed()
#         self._mode_pattern()

# class ClockwiseMode():
#     '''The next player turn will be in clockwise order'''

#     def __init__(
#             self,
#             current_player: PlayerButton,
#             buttons: List[PlayerButton],
#             button_board: PlayerButtonBoard
#         ):
#         super().__init__(
#             current_player=current_player,
#             buttons=buttons,
#             button_board=button_board
#         )

#     def _player_button_pressed(self):
#         '''Function when PlayerButton is pressed. (Set current player)'''
#         pass # TODO

#     def _mode_pattern(self):
#         '''LED pattern on startup'''
#         pass # TODO

#     def _set_player_button_pressed(self):
#         '''Set player buttons press function'''
#         pass # TODO

#     def start(self):
#         '''Runs the mode pattern and sets button functions'''
#         pass # TODO

# class CounterClockwiseMode():
#     '''The next player turn will be in counter clockwise order'''

#     def __init__(self, buttons: List[PlayerButton], button_board: PlayerButtonBoard):
#         super().__init__()
#         self.buttons = buttons
#         self.button_board = button_board

#     def _player_button_pressed(self):
#         '''Function when PlayerButton is pressed'''
#         pass # TODO

#     def _mode_pattern(self):
#         '''LED pattern on startup'''
#         pass # TODO

#     def _set_player_button_pressed(self):
#         '''Set player buttons press function'''
#         pass # TODO

#     def start(self):
#         '''Runs the mode pattern and sets button functions'''
#         pass # TODO

# class RandomMode():
#     '''The next player turn will be randomly selected and continue in clockwise order'''

#     def __init__(self, buttons: List[PlayerButton], button_board: PlayerButtonBoard):
#         super().__init__(
#             buttons=buttons,
#             button_board=button_board,
#         )

#     def _player_button_pressed(self):
#         '''Function when PlayerButton is pressed. (Do nothing)'''
#         pass

#     def _mode_pattern(self):
#         '''LED pattern on startup'''
#         while self.is_active:
#             random.choice(self.button_board).led_flash(delay=0.5)

#     def _set_player_button_pressed(self):
#         '''Set player buttons press function'''
#         for button in self.buttons:
#             button.when_pressed = self._player_button_pressed

#     def start(self):
#         '''Runs the mode pattern and sets button functions'''
#         self._set_player_button_pressed()
#         self._mode_pattern()

# class SelectedMode():
#     '''Players select player order'''

#     def __init__(self, buttons: List[PlayerButton], button_board: PlayerButtonBoard):
#         super().__init__()
#         self.buttons = buttons
#         self.button_board = button_board

#     def _player_button_pressed(self):
#         '''Function when PlayerButton is pressed'''
#         pass # TODO

#     def _mode_pattern(self):
#         '''LED pattern on startup'''
#         pass # TODO

#     def _set_player_button_pressed(self):
#         '''Set player buttons press function'''
#         pass # TODO

#     def start(self):
#         '''Runs the mode pattern and sets button functions'''
#         pass # TODO
# --------------------
# Session States
# --------------------
"""
Session states control how buttons behave at different stages of the program.

- Setup:    the stage when players select which buttons are in the game
- Game:     the stage when a single player is active and being timed
- Pause:    the stage when no player is active and the program is waiting
            for a new active player
"""
class SessionState():
    '''Base class for session state'''

    def __init__(self, accept_button: AcceptButton = ACCEPT_BUTTON):
        self.accept_button = accept_button
        self.is_active = True

    def _accept_button_pressed(self):
        '''Fuction when AcceptButton is pressed'''
        pass

    def _player_button_pressed(self):
        '''Function when PlayerButton is pressed'''
        pass

    def _startup_pattern():
        '''LED pattern on startup'''
        pass

    def _set_accept_button_pressed(self):
        '''Set accept button press function'''
        pass

    def _set_player_button_pressed(self):
        '''Set player buttons press function'''
        pass

    def start(self):
        '''Runs session state pattern and sets button functions'''
        self.startup_pattern()

class SetupState(SessionState):
    '''Setup session state'''

    def __init__(
            self,
            buttons: List[PlayerButton] = BUTTON_LIST,
            button_board: PlayerButtonBoard = PLAYER_BUTTON_BOARD,
        ):
        super().__init__()
        self.buttons = buttons
        self.button_board = button_board
        self.is_active = True
        self.active_buttons = set()

    def _accept_button_pressed(self):
        '''Function when AcceptButton is pressed'''
        # Create inactive button list
        inactive_buttons = list(set(self.buttons).difference(self.active_buttons))

        # Disable buttons for the rest of the session
        for button in inactive_buttons:
            button.disabled_toggle()

        # End setup session state
        self.is_active = False

    def _player_button_pressed(self, button: PlayerButton):
        '''Function when PlayerButton is pressed'''
        # Toggle the LED
        button.led_toggle()

        # Toggle button active status
        button.active_button_toggle()

        # Add or remove button from active button list
        if button in self.active_buttons:
            self.active_buttons.remove(button)
        else:
            self.active_buttons.add(button)

    def _set_accept_button_pressed(self):
        '''Set accept button press function'''
        self.accept_button.when_pressed = self._accept_button_pressed

    def _set_player_button_pressed(self):
        '''Set player buttons press function'''
        for button in self.buttons:
            button.when_pressed = self._player_button_pressed

    def _startup_pattern(self):
        '''Starting LED pattern'''
        self.button_board.led_cycle(2)
        self.button_board.led_flash(3)

    def start(self):
        '''Runs session state pattern and sets button functions'''
        self._startup_pattern()
        self._set_player_button_pressed()
        self._set_accept_button_pressed()

class GameState(SessionState):
    '''Game session state'''

    def __init__(
            self,
            buttons: List[PlayerButton],
            button_board: PlayerButtonBoard
        ):
        super().__init__()
        self.buttons = buttons
        self.button_board = button_board
        self.current_player = self._get_current_player()

    def _get_current_player(self):
        '''Get current player from button_board'''
        current_player = None
        for button in self.button_board:
            if button.is_player_turn:
                current_player = button
        return current_player

    def _accept_button_pressed(self):
        '''Function when AcceptButton is pressed'''
        self.current_player.player_turn_toggle()
        self.is_active = False

    def _player_button_pressed(self, button: PlayerButton):
        '''Function when PlayerButton is pressed. (Pass to next player)'''
        if button == self.current_player:
            self.current_player.player_turn_toggle()
            self.current_player.next_player.player_turn_toggle()
            self.current_player = self.current_player.next_player

    def _set_accept_button_pressed(self):
        '''Set active button press function'''
        self.active_button.when_pressed = self._active_button_pressed

    def _set_player_button_pressed(self):
        '''Set player buttons press function'''
        for button in self.buttons:
            button.when_pressed = self._player_button_pressed

    def start(self):
        '''Runs session state pattern and sets button functions'''
        self._set_player_button_pressed()
        self._set_accept_button_pressed()

class PauseState(SessionState):
    '''Pause session state'''

    def __init__(
        self,
        buttons: List[PlayerButton],
        button_board: PlayerButtonBoard,
        current_player: PlayerButton,
    ):
        super().__init__()
        self.buttons = buttons
        self.button_board = button_board
        self.is_active = True
        self.current_player = current_player

    def _accept_button_pressed(self):
        '''Function when AcceptButton is pressed'''
        # Toggle current player turn
        self.current_player.player_turn_toggle()

        # End setup session state
        self.is_active = False

    def _player_button_pressed(self, button: PlayerButton):
        '''Function when PlayerButton is pressed. (Do nothing)'''
        pass

    def _set_accept_button_pressed(self):
        '''Set active button press function'''
        self.active_button.when_pressed = self._active_button_pressed

    def _set_player_button_pressed(self):
        '''Set player buttons press function'''
        for button in self.buttons:
            button.when_pressed = self._player_button_pressed

    def _startup_pattern(self):
        '''LED pattern for mode. (Current player flashes)'''
        while self.is_active and self.current_player is not None:
            self.current_player.led_flash(delay=1)

    def start(self):
        '''Runs the mode pattern and sets button functions'''
        self._set_player_button_pressed()
        self._set_accept_button_pressed()
        self._startup_pattern()

class RandomState(SessionState):
    '''Pause session state'''

    def __init__(
        self,
        buttons: List[PlayerButton],
        button_board: PlayerButtonBoard,
    ):
        super().__init__()
        self.buttons = buttons
        self.button_board = button_board
        self.is_active = True
        self.current_player = None

    def _accept_button_pressed(self):
        '''Function when AcceptButton is pressed'''
        # Randomly select current player
        self.current_player = random.choice(self.button_board)

        # End setup session state
        self.is_active = False

    def _player_button_pressed(self, button: PlayerButton):
        '''Function when PlayerButton is pressed. (Do nothing)'''
        pass

    def _set_accept_button_pressed(self):
        '''Set active button press function'''
        self.active_button.when_pressed = self._active_button_pressed

    def _set_player_button_pressed(self):
        '''Set player buttons press function'''
        for button in self.buttons:
            button.when_pressed = self._player_button_pressed

    def _startup_pattern(self):
        '''LED pattern for session state (Random)'''
        while self.is_active:
            random.choice(self.button_board).led_flash(delay=0.5)

    def start(self):
        '''Runs the mode pattern and sets button functions'''
        self._set_player_button_pressed()
        self._set_accept_button_pressed()
        self._startup_pattern()
# --------------------
# Session
# --------------------
"""
A session is a single game. Session states are an attribute of a session.
"""
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

        # Setup state
        self.session_state.start()

        while self.session_state.is_active:
            pass
        
        active_buttons = list(self.session_state.active_buttons)
        for i, button in enumerate(active_buttons[:-1]):
            button.next_player = active_buttons[i+1]
        active_buttons[-1].next_player = active_buttons[0]

        button_board = PlayerButtonBoard(active_buttons)

        # Init PauseState with active buttons
        self.session_state = RandomState(
            buttons=active_buttons,
            button_board=button_board,
        )

        # Start RandomState
        self.session_state.start()

        current_player = self.session_state.current_player

        while True:
            self.session_state = PauseState(
                buttons=active_buttons,
                button_board=button_board,
                current_player=current_player,
            )

            self.session_state.start()

            self.session_state = GameState(
                buttons=active_buttons,
                button_board=button_board,
            )

            while self.session_state.is_active:
                pass



    def reset(self):
        '''Reset session'''
        # Reset session state to new SetupState instance
        self.session_state = SetupState()
        
        # Reset all buttons
        for button in self.buttons:
            button.reset()

        
