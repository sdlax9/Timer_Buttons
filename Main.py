from gpiozero import LED
from gpiozero import Button
from time import sleep


whiteButton = Button(27)
whiteLED = LED(17)

greenButton = Button(23)
greenLED = LED(24)

redButton = Button(6)
redLED = LED(5)

yellowButton = Button(21)
yellowLED = LED(20)

blueButton = Button(19)
blueLED = LED(26)

x = 0

while x < 2:

    x+=1

whiteLED.on()
whiteButton.wait_for_press()
whiteLED.off()

yellowLED.on()
yellowButton.wait_for_press()
yellowLED.off()

redLED.on()
redButton.wait_for_press()
redLED.off()

greenLED.on()
greenButton.wait_for_press()
greenLED.off()

blueLED.on()
blueButton.wait_for_press()
blueLED.off()

print('complete')

exit