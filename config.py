from buttons import PlayerButton, AcceptButton
from gpiozero import Device
from gpiozero.pins.mock import MockFactory

Device.pin_factory = MockFactory()


# White button
WHITE_BTN_PIN = 27
WHITE_BTN_LED = 17

# Green button
GREEN_BTN_PIN = 23
GREEN_BTN_LED = 24

# Red button
RED_BTN_PIN = 6
RED_BTN_LED = 5

# Yellow button
YELLOW_BTN_PIN = 21
YELLOW_BTN_LED = 20

# Blue button
BLUE_BTN_PIN = 19
BLUE_BTN_LED = 26

# Accept button
ACCEPT_BTN_PIN = 0

buttons = {
    'white': PlayerButton(
        color='white',
        button_pin=WHITE_BTN_PIN,
        led_pin=WHITE_BTN_LED,
    ),
    'green': PlayerButton(
        color='green',
        button_pin=GREEN_BTN_PIN,
        led_pin=GREEN_BTN_LED,
    ),
    'red': PlayerButton(
        color='red',
        button_pin=RED_BTN_PIN,
        led_pin=RED_BTN_LED,
    ),
    'yellow': PlayerButton(
        color='yellow',
        button_pin=YELLOW_BTN_PIN,
        led_pin=YELLOW_BTN_LED,
    ),
    'blue': PlayerButton(
        color='blue',
        button_pin=BLUE_BTN_PIN,
        led_pin=BLUE_BTN_LED,
    ),
    'accept': AcceptButton(
        button_pin=ACCEPT_BTN_PIN,
    ),
}