from gpiozero import Device, Button, LED

from config import buttons

from time import sleep


buttons['white'].button.when_pressed = buttons['white'].button_pressed

buttons['white'].button.pin.drive_low()  # This simulates pressing the button
buttons['white'].button.pin.drive_high()  # This simulates releasing the button