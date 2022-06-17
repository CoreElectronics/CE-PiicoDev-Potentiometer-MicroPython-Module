from PiicoDev_Potentiometer import PiicoDev_Potentiometer
from PiicoDev_Unified import sleep_ms
 
pot = PiicoDev_Potentiometer(address=0x35, min=0.0, max=100.0)   # Initialise the RFID module

while True:
    firmware = pot.readFirmware()
    print('Firmware: ' + str(firmware[0]) + '.' + str(firmware[1]))
    print('ID: ' + str(pot.readID()))
    print('Last Command Known: ' + str(pot.last_command_known))
    print('Last Command Success: ' + str(pot.last_command_success))
    print('Flashing LED 3 times')
    for x in range(3):
        pot.pwrLED(0)
        sleep_ms(500)
        pot.pwrLED(1)
        sleep_ms(500)
    print(pot.read())
    #pot.setI2Caddr(0x20)