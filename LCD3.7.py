from adafruit_bme280 import basic as adafruit_bme280
from rpi_lcd import LCD


lcd = LCD()

try:
    while True:

        lcd.text("regel 1", 1)
        lcd.text("regel 2", 2)
        lcd.text("regel 3", 3)
        lcd.text("regel 4" , 4)

except KeyboardInterrupt:
    lcd.clear()