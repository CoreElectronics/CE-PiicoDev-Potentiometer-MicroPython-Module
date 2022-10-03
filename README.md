# PiicoDev® Potentiometer MicroPython Module

This is the firmware repo for the Core Electronics [PiicoDev® Potentiometer](https://core-electronics.com.au/catalog/product/view/sku/CE08463) and [PiicoDev® Slide Potentiometer](https://core-electronics.com.au/catalog/product/view/sku/CE08502)

This module depends on the [PiicoDev Unified Library](https://github.com/CoreElectronics/CE-PiicoDev-Unified), include `PiicoDev_Unified.py` in the project directory on your MicroPython device.

## Initialisation
`PiicoDev_Potentiometer(bus=, freq=, sda=, scl=, address=0x35, id=, minimum=0.0, maximum=100.0)`
Parameter | Type | Range | Default | Description
--- | --- | --- | --- | ---
bus | int | 0,1 | Raspberry Pi Pico: 0, Raspberry Pi: 1 | I2C Bus.  Ignored on Micro:bit
freq | int | 100 to 1000000 | Device dependent | I2C Bus frequency (Hz).  Ignored on Raspberry Pi
sda | Pin | Device Dependent | Device Dependent | I2C SDA Pin. Implemented on Raspberry Pi Pico only
scl | Pin | Device Dependent | Device Dependent | I2C SCL Pin. Implemented on Raspberry Pi Pico only
address | int | 0x35 | 0x35, 0x08 - 0x77 | Manually specify the address of the connected device. For when a software address is set on the device.
id | List[int, int, int, int] | 1=ON, 0=OFF | [0,0,0,0] | Hardware switches change the device address - Abstracts the need for user to look up an address, simply input the switch positions. Alternatively, use `address` for explicit address.
minimum | float | -1.797*10^308 to 1.797*10^308 | 0.0 | The value that the pot returns at it's minimum *travel*
maximum | float | -1.797*10^308 to 1.797*10^308  | 100.0 | The value that the pot returns at it's maximum *travel*

**Example Usage**

Initialise the potentiometer with a default range 0.0 - 1.0

```python
pot = PiicoDev_Potentiometer(minimum=0.0, maximum=1.0)
```

Initialise the potentiometer with address switch ASW(1 to 4) configuration [1,0,1,0]

```python
pot = PiicoDev_Potentiometer(asw=[1,0,1,0])
```

## Properties

### `.value`
Returns a float between 0.0 and 100.0 (default) or a value from a user-defined scale

**Example Usage**
```python
value = pot.value
```


### `.raw`
Returns the raw ADC value

**Example Usage**
```python
raw_value = pot.raw
```

### `.minimum` and `.maximum`
Returns/Sets the potentiometer scale where `min`/`max` is the value that the pot returns at it's minimum/maximum *travel*

**Example Usage**
```python
# Set the full output range to [-1:1]
pot.minimum = -1
pot.maximum = 1
```

### `.led`
Returns/controls the state onboard "Power" LED. accepts `True` / `False`

**Example Usage**
```python
pot.led = False # turn the LED off
```

### `.address`
Returns the currently configured 7-bit I2C address

**Example Usage**
```python
a = pot.address
```

### `.whoami`
Returns the device identifier.  Will always return 379.

**Example Usage**
```python
deviceID = pot.whoami
```

### `.firmware`
Returns the major version, minor version
```python
firmware = pot.firmware
```

## Methods

### `setI2Caddr(a)`
Set a new 7-bit I2C address (0x08 to 0x77)

**Example Usage**
```python
pot.setI2Caddr(0x45)
```

## Device Registers
The PiicoDev Potentiometer is an I2C device with default address 0x35.

| Register Name    | Address   | Bytes  | Mode | Default Value    | Description
| ---------------- | --------- | ------ | ---- | ---------------- | -----------
| Device ID        | 0x11      | 2      | R    | 0x01EF (d495)              | I2C device ID
| Firmware Major   |           | 1      | R    | Varies           | Major firmware version
| Firmware Minor   |           | 1      | R    | Varies           | Minor firmware version
| I2C Address      |           | 1      | W    | 0x35             | Set new I2C address
| LED (Read status)| 0x07      | 1      | R    | 1                | 0=OFF, 1=ON
| LED (Write status)| 0x87      | 1      | W    | 1                | 0=OFF, 1=ON


# License
This project is open source - please review the LICENSE.md file for further licensing information.

If you have any technical questions, or concerns about licensing, please contact technical support on the [Core Electronics forums](https://forum.core-electronics.com.au/).

*\"PiicoDev\" and the PiicoDev logo are trademarks of Core Electronics Pty Ltd.*
