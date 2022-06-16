# A simple class to read data from the Core Electronics PiicoDev Potentiometer
# Peter Johnston at Core Electronics
# 2022 APR 06 - Initial release

from PiicoDev_Unified import *

compat_str = '\nUnified PiicoDev library out of date.  Get the latest module: https://piico.dev/unified \n'

_BASE_ADDRESS = 0x35
_DEVICE_ID    = 0x51

_REG_STATUS      = 0x01
_REG_FIRM_MAJ    = 0x02
_REG_FIRM_MIN    = 0x03
_REG_I2C_ADDRESS = 0x04
_REG_POT         = 0x05
_REG_LED         = 0x07
_REG_DEV_ID      = 0x11

_min = min; _max = max # alias the builtin functions so we can use 'min' and 'max' as initialiser arguments

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
        a=address
        if type(id) is list and not all(v == 0 for v in id): # preference using the ID argument. ignore id if all elements zero
            assert _max(id) <= 1 and _min(id) >= 0 and len(id) is 4, "id must be a list of 1/0, length=4"
            self.address=8+id[0]+2*id[1]+4*id[2]+8*id[3] # select address from pool
        else: self.address = address # accept an integer
        try:
            self.i2c.writeto_mem(self.address, _REG_LED, b'\x01') # Initialise pwr led on
        except Exception as e:
            print(i2c_err_str.format(self.address))
            raise e
        # TODO: Check device ID - seems to timeout on Raspberry Pi (clock stretching not implemented)
#         try:
#             if self.readID() != _DevID:
#                 print("* Incorrect device found at address {}".format(addr))
#         except:
#             print("* Couldn't find a device - check switches and wiring")
#  


    def setI2Caddr(self, newAddr):
        x=int(newAddr)
        assert 8 <= x <= 0x77, 'address must be >=0x08 and <=0x77'
        try:
            self.i2c.writeto_mem(self.address, _REG_I2C_ADDRESS, bytes([x]))
            self.addr = x
            sleep_ms(5)
            return 0
        except: print(i2c_err_str.format(self.address)); return 1
        

    def readFirmware(self):
        v=[0,0]
        try:
            v[1]=self.i2c.readfrom_mem(self.address, _REG_FIRM_MAJ, 1)
            v[0]=self.i2c.readfrom_mem(self.address, _REG_FIRM_MIN, 1)
            return (v[1],v[0])
        except: return(0,0)

    def readStatus(self):
        sts=self.i2c.readfrom_mem(self.address, _REG_STATUS,1)
        return sts
    
    def readID(self):
        x=self.i2c.readfrom_mem(self.address, _REG_DEV_ID,1)
        return int.from_bytes(x,'big')

    def pwrLED(self, x):
        try: self.i2c.writeto_mem(self.address, _REG_LED, bytes([x])); return 0
        except: print(i2c_err_str.format(self.address)); return 1
            
    def read(self, raw=False):
        try:
            raw_value = int.from_bytes(self.i2c.readfrom_mem(self.address, _REG_POT, 2),'big')
            if raw:
                return rawValue
            else:
                return round(self.min + ((self.max - self.min) / 1023) * raw_value, 1)
        except:
            return(float('NaN'))
        
        