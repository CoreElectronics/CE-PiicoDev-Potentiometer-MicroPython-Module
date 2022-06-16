from PiicoDev_Potentiometer import PiicoDev_Potentiometer
from PiicoDev_Unified import sleep_ms
 
pot = PiicoDev_Potentiometer(min=0.0, max=100.0)   # Initialise the RFID module

while True:
    print(pot.read())
    sleep_ms(1000)