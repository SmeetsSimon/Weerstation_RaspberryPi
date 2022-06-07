import board
import busio
from adafruit_bme280 import basic as adafruit_bme280
import time

i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)


while True:
    print(f"\n{'Temperature:':<13} {round(bme280.temperature, 1)} °C")
    print(f"{'Humidity:':<13} {round(bme280.humidity, 1)} %")
    print(f"{'Pressure:':<13} {round(bme280.pressure, 1)} hPa")
    time.sleep(5)
