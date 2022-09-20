# Use the potentiometer as a control input - change the flash speed of the on-board LED
from PiicoDev_Potentiometer import PiicoDev_Potentiometer
from PiicoDev_Unified import sleep_ms

# Initialise the module - here the range corresponds to millisecond delays
pot = PiicoDev_Potentiometer(minimum=500, maximum=50)

while True:
    delay_ms = int(pot.value)    # sample the pot, we know the value is already useful as milliseconds
    pot.led = not pot.led        # toggle the LED
    
    hz = round(1000/delay_ms/2, 1) # convert delay [ms] to frequency [Hz]
    print('Flash rate ' + str(hz) + ' Hz')
    
    sleep_ms(delay_ms)           # wait for the delay time
    