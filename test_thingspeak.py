
from time import time, sleep
from urllib.request import urlopen 
import sys

WRITE_API = "VC1F5TSJ3NNRS4FL" # Replace your ThingSpeak API key here
BASE_URL = "https://api.thingspeak.com/update?api_key={}".format(WRITE_API)

temperature = 100
humidity = 5



SensorPrevSec = 0
SensorInterval = 2 # 2 seconds
ThingSpeakPrevSec = 0
ThingSpeakInterval = 20 # 20 seconds

try:
    while True:
        
        
        if time() - ThingSpeakPrevSec > ThingSpeakInterval:
            ThingSpeakPrevSec = time()
            
            thingspeakHttp = BASE_URL + "&field1={:.2f}&field2={:.2f}".format(temperature, humidity, pressure)
            print(thingspeakHttp)
            
            conn = urlopen(thingspeakHttp)
            print("Response: {}".format(conn.read()))
            conn.close()
            
            
            sleep(1)
            
except KeyboardInterrupt:
    conn.close()