# Ductsoup_Python_MLX90614

This Python driver allows you to read data from an [MLX90614](https://www.adafruit.com/products/1747) on a Raspberry Pi.

## Requirements

This driver requires that you have previously installed the
[Adafruit_Python_GPIO](https://github.com/adafruit/Adafruit_Python_GPIO) package.

You can install this package with the following commands:

```
$sudo apt-get update
$sudo apt-get install build-essential python-pip python-dev python-smbus git i2c-tools
$git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
$cd Adafruit_Python_GPIO
$sudo python setup.py install
$cd ~
```

To enable I2C repeated start conditions on Raspberry Pi use the following command. You might also want to consider adding this to your /etc/rc.local file.

```
$sudo su -c 'echo "Y" > /sys/module/i2c_bcm2708/parameters/combined'
```
Finally, install this package.

```
$git clone https://github.com/ductsoup/Ductsoup_Python_MLX90614.git
$cd Ductsoup_Python_MLX90614
$sudo python setup.py install
```

## Usage

First verify that your wiring is correct and the device is available on the I2C bus.

```
$sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- 5a -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

Then try the demo progam. If all went well you should see something like this.

```
$cd Ductsoup_Python_MLX90614
$python demo.py
Ambient temperature :    21.03 C
Cloud temperature 1 :    18.15 C
Cloud temperature 2 :  -273.15 C
Estimated cloud base:   292.68 M
```

## Credits

This driver is lightly based on the examples from [Adafruit_BMP](https://github.com/adafruit/Adafruit_Python_BMP)
by Tony DiCola (Adafruit Industries) and [Adafruit MLX] (https://github.com/adafruit/Adafruit-MLX90614-Library)
by Limor Fried/Ladyada (also Adafruit Industries).

## MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
