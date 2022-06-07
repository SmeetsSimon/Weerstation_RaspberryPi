import board
import busio
from adafruit_bme280 import basic as adafruit_bme280
from rpi_lcd import LCD
import time
import csv
from urllib.request import urlopen 

WRITE_API = "VC1F5TSJ3NNRS4FL" # Replace your ThingSpeak API key here
BASE_URL = "https://api.thingspeak.com/update?api_key={}".format(WRITE_API)


csvfile = "temp.csv"
als = True

i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

lcd = LCD()

file= open('temp.csv', "a")
file.write('time and date, temperature (C), humidity, pressure\n')

SensorPrevSec = 0
SensorInterval = 2 # 2 seconds
ThingSpeakPrevSec = 0
ThingSpeakInterval = 20 # 20 seconds


try:
    while True:

        print(f"\n{'Temperature:':<13} {round(bme280.temperature, 1)} °C")
        print(f"{'Humidity:':<13} {round(bme280.humidity, 1)} %") 
        print(f"{'Pressure:':<13} {round(bme280.pressure)} hPa")

        timeC = time.strftime("%I")+':' +time.strftime("%M")+':'+time.strftime("%S")
        data = [ timeC, round(bme280.temperature, 1), round(bme280.humidity, 1) , round(bme280.pressure, 1)]
		

        with open(csvfile, "a")as output:
			
            writer = csv.writer(output, delimiter=' ', lineterminator = '\n')
            writer.writerow(data)

        lcd.clear()
        string1 = "temperatuur:" + str(round(bme280.temperature, 1)) + " C"
        string2 = "vochtigheid:" + str(round(bme280.humidity, 1)) + " %"
        string3 = "luchtdruk:" + str(round(bme280.pressure, 1)) + " hPa"
        lcd.text(string1, 1)
        lcd.text(string2, 2)
        lcd.text(string3, 3)
        lcd.text( "" , 4)

        #if time.time() - ThingSpeakPrevSec > ThingSpeakInterval:
        #   ThingSpeakPrevSec = time.time()
            
        thingspeakHttp = BASE_URL + "&field1={:.2f}&field2={:.2f}&field3={:.2f}".format(bme280.temperature, bme280.humidity, bme280.pressure)
        print(thingspeakHttp)
            
        conn = urlopen(thingspeakHttp)
        print("Response: {}".format(conn.read()))
        conn.close()

        time.sleep(5)

except KeyboardInterrupt:
    lcd.clear()
    conn.close()
