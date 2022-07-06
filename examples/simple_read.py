from PiicoDev_Potentiometer import PiicoDev_Potentiometer
from PiicoDev_Unified import sleep_ms
 
pot = PiicoDev_Potentiometer(minimum=0.0, maximum=100.0)   # Initialise the RFID module

while True:
    value = pot.value
    print(value)
    sleep_ms(100)