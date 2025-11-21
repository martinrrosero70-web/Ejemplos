from machine import Pin, PWM
from ssd1306 import SSD1306
import time 

i2c = I2C(0, scl=i2c_scl, sda=i2c_sda, freq=400000)

print("Dispositivos I2C enocntrados:", i2c.scan())
ancho = 128
alto = 64
aled = SSD1306_I2C(ancho, alto, i2c)
oled.fill(0)
oled.text("Mocosos feos", 0, 0)
oled.text(":3", 0, 16)
oled.show()