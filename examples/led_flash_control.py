from PiicoDev_Potentiometer import PiicoDev_Potentiometer
from PiicoDev_Unified import sleep_ms
 
pot = PiicoDev_Potentiometer(minimum=300, maximum=50)   # Initialise the module

while True:
    value = int(pot.value)
    print('Value: ' + str(value))
    pot.led = False
    sleep_ms(value)
    pot.led = True
    sleep_ms(value)