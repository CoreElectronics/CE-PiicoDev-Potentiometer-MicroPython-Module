from PiicoDev_Potentiometer import PiicoDev_Potentiometer
from PiicoDev_Unified import sleep_ms
 
pot = PiicoDev_Potentiometer()   # Initialise the RFID module

while True:
    print(pot.readRaw())
    print(pot.read())
    sleep_ms(1000)