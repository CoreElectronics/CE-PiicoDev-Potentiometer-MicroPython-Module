# Use a PiicoDev Potentiometer to control the tone of a micro:bit's buzzer
from PiicoDev_Potentiometer import PiicoDev_Potentiometer
from PiicoDev_Unified import sleep_ms
import music

pot = PiicoDev_Potentiometer() # Initialise the potentiometer as a frequency-control
pot.maximum = 440 # Hz
pot.minimum = -1 # micro:bit will constantly "tick" if using 0Hz, so we'll use -1 for 'no sound'

while True:
    frequency = int(pot.value) # pitch accepts whole-numbers only!
    music.pitch(frequency)
    print(frequency, 'Hz') # read the pot and print the result
    sleep_ms(100)