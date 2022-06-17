# A simple class to read data from the Core Electronics PiicoDev Potentiometer
# Peter Johnston at Core Electronics
# 2022 APR 06 - Initial release

from PiicoDev_Unified import *

compat_str = '\nUnified PiicoDev library out of date.  Get the latest module: https://piico.dev/unified \n'

_BASE_ADDRESS = 0x35
_DEVICE_ID    = 379

_REG_STATUS      = 0x01
_REG_FIRM_MAJ    = 0x02
_REG_FIRM_MIN    = 0x03
_REG_I2C_ADDRESS = 0x04
_REG_POT         = 0x05
_REG_LED         = 0x07
_REG_DEV_ID      = 0x11

_min = min; _max = max # alias the builtin functions so we can use 'min' and 'max' as initialiser arguments

def _readBit(x, n):
    return x & 1 << n != 0

class PiicoDev_Potentiometer(object):
    def __init__(self, bus=None, freq=None, sda=None, scl=None, address=_BASE_ADDRESS, id=None, min=0.0, max=100.0):
        try:
            if compat_ind >= 1:
                pass
            else:
                print(compat_str)
        except:
            print(compat_str)
        self.i2c = create_unified_i2c(bus=bus, freq=freq, sda=sda, scl=scl)
        self.address = address
        self.min = min
        self.max = max
        self.last_command_known = False
        self.last_command_success = False
        if type(id) is list and not all(v == 0 for v in id): # preference using the ID argument. ignore id if all elements zero
            assert _max(id) <= 1 and _min(id) >= 0 and len(id) == 4, "id must be a list of 1/0, length=4"
            self.address=8+id[0]+2*id[1]+4*id[2]+8*id[3] # select address from pool
        else: self.address = address # accept an integer
        try:
            if self.readID() != _DEVICE_ID:
                print("* Incorrect device found at address {}".format(address))   
        except:
            print("* Couldn't find a device - check switches and wiring")   

    def _read(self, register, length=1):
        try:
            return self.i2c.readfrom_mem(self.address, register, length)
        except:
            print(i2c_err_str.format(self.address))
            return None
    
    def _write(self, register, data):
        try:
            self.i2c.writeto_mem(self.address, register, data)
        except:
            print(i2c_err_str.format(self.address))
    
    def _readInt(self, register, length=1):
        data = self._read(register, length)
        if data is None:
            return None
        else:
            return int.from_bytes(data, 'big')
        
    def _writeInt(self, register, integer, length=1):
        self._write(register, int.to_bytes(integer, length, 'big'))

    def setI2Caddr(self, newAddr):
        x=int(newAddr)
        assert 8 <= x <= 0x77, 'address must be >=0x08 and <=0x77'
        self._writeInt(_REG_I2C_ADDRESS, x)
        self.addr = x
        sleep_ms(5)
        return 0

    def readFirmware(self):
        v=[0,0]
        v[1]=self._readInt(_REG_FIRM_MAJ)
        v[0]=self._readInt(_REG_FIRM_MIN)
        self.readStatus()
        return (v[1],v[0])

    def readStatus(self):
        sts=self._readInt(_REG_STATUS)
        if sts is not None:
            self.last_command_known = _readBit(sts, 2)
            self.last_command_success = _readBit(sts, 1)
    
    def readID(self):
        x=self._readInt(_REG_DEV_ID, 2)
        self.readStatus()
        return x

    def pwrLED(self, x):
        self._writeInt(_REG_LED, int(x)); return 0
            
    def read(self, raw=False):
        raw_value = self._readInt(_REG_POT, 2)
        self.readStatus()
        if raw_value is None:
            return(float('NaN'))
        if raw:
            return raw_value
        else:
            return round(self.min + ((self.max - self.min) / 1023) * raw_value, 1)
