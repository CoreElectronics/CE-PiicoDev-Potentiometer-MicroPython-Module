from PiicoDev_Potentiometer import PiicoDev_Potentiometer
from PiicoDev_Unified import sleep_ms
 
pot = PiicoDev_Potentiometer(min=0.0, max=100.0)   # Initialise the RFID module

while True:
    print('Firmware------')
    print(pot.readFirmware())
    print('Firmware------')
#     print(pot.read())
#     print(pot.readStatus())

    print('power LED set')
    print('Firmware------2')
    print(pot.readFirmware())
    print('Firmware------2')
    
    print(pot.readDebug())
    for x in range(255):
        pot.pwrLED(1)
        sleep_ms(256-x)
        pot.pwrLED(0)
        sleep_ms(256-x)
    sleep_ms(1000)