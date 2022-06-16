from PiicoDev_Potentiometer import PiicoDev_Potentiometer
from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms
 
pot_x = PiicoDev_Potentiometer(min=0, max=127)   # Initialise the RFID module
pot_y = PiicoDev_Potentiometer(id=[1,0,0,0], min=127, max=0)
display = create_PiicoDev_SSD1306()

display.load_pbm('splash.pbm', 1)
display.show()
sleep_ms(3000)
display.fill(0)
x_prev = int(pot_x.read())
y_prev = int(pot_y.read())


while True:
    x = int(round(pot_x.read()))
    y = int(round(pot_y.read()))
    if y > 63:
        y = 63
    display.line(x_prev, y_prev, x, y, 1)
    display.show()
    x_prev = x
    y_prev = y
    sleep_ms(10)