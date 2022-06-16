# PiicoDev® Potentiometer MicroPython Module

This is the firmware repo for the Core Electronics [PiicoDev® Potentiometer](https://core-electronics.com.au/catalog/product/view/sku/CE08463) and [PiicoDev® Slide Potentiometer](https://core-electronics.com.au/catalog/product/view/sku/CE08502)

This module depends on the [PiicoDev Unified Library](https://github.com/CoreElectronics/CE-PiicoDev-Unified), include `PiicoDev_Unified.py` in the project directory on your MicroPython device.


# Reference

## Initialisation
```python
pot = PiicoDev_Potentiometer(min=0.0, max=100.0)
```

## read(raw=False)
Return a float between 0.0 and 100.0 (default) or a value from a user-defined scale
Returns the raw ADC value when `raw=True`

## setRange(min,max)
sets the potentiometer scale where `min`/`max` is the value that the pot returns at it's minimum/maximum *travel* ie:
```python
PiicoDev_Potentiometer.setRange(0.0, 100.0) # would be the default settings
PiicoDev_Potentiometer.setRange(100.0, 0.0) # reverses the direction of the pot
PiicoDev_Potentiometer.setRange(0.0, 1.0) # creates a 0->1 value
```

## Control onboard LED

## Read Device ID

## Change I2C address



# License
This project is open source - please review the LICENSE.md file for further licensing information.

If you have any technical questions, or concerns about licensing, please contact technical support on the [Core Electronics forums](https://forum.core-electronics.com.au/).

*\"PiicoDev\" and the PiicoDev logo are trademarks of Core Electronics Pty Ltd.*
