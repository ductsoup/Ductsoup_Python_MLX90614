'''
MLX90614 class for Raspberry Pi

https://cdn-shop.adafruit.com/datasheets/MLX90614.pdf
https://www.adafruit.com/product/1747
https://www.adafruit.com/product/1748

Notes:
(1) This device requires repeated start conditions for I2C register
reads. On Raspberry Pi you will likely have to enable this behavior
by running this shell command or placing it in your /etc/rc.local.

    sudo su -c 'echo "Y" > /sys/module/i2c_bcm2708/parameters/combined'

    Reference:
    http://www.raspberrypi.org/forums/viewtopic.php?f=44&t=15840

(2) Add two 10k pull up resistors on SCL and SDA.
'''

MLX90614_I2CADDR       = 0x5a

MLX90614_RAM_REG_TA    = 0x06
MLX90614_RAM_REG_TOBJ1 = 0x07
MLX90614_RAM_REG_TOBJ2 = 0x08

MLX90614_UNIT_C        = 0x00
MLX90614_UNIT_F        = 0x01

class MLX90614:
    def __init__(self, addr = MLX90614_I2CADDR, i2c = None, **kwargs):
        if i2c is None:
            import Adafruit_GPIO.I2C as I2C
            i2c = I2C
        self._device = i2c.get_i2c_device(addr, **kwargs)

    def read_temp(self, reg = MLX90614_RAM_REG_TOBJ1, unit = MLX90614_UNIT_C):
        temp = self._device.readS16(reg) * 0.02 - 273.15
        if (unit == MLX90614_UNIT_F):
            temp = (temp * 9 / 5) + 32
        return temp

    def read_ambient(self, unit = MLX90614_UNIT_C):
        return self.read_temp(MLX90614_RAM_REG_TA, unit)

    def read_object1(self, unit = MLX90614_UNIT_C):
        return self.read_temp(MLX90614_RAM_REG_TOBJ1, unit)

    def read_object2(self, unit = MLX90614_UNIT_C):
        return self.read_temp(MLX90614_RAM_REG_TOBJ2, unit)

    '''
    Calculate the cloud height based on the assumption that the air temperature drops 9.84 degrees C
    per 1000 m of altitude and the dewpoint drops 1.82 degrees C per 1000 meters altitude.

        cloudTemp = - 0.00984 * cloudHeight + airTemp

        Reference:
        http://www.shodor.org/os411/courses/_master/tools/calculators/cloudbaseheight/
    '''
    def read_cloud_base(self):
        Ta  = self.read_ambient()
        To  = self.read_object1()
        To2 = self.read_object2()
        if (To2 > -273.15):
            To = (To + To2) / 2
        return (Ta - To) / 0.00984
