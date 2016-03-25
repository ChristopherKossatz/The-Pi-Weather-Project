import time
from Adafruit_BME280 import *

sensor = BME280(mode=BME280_OSAMPLE_8)

temp = sensor.read_temperature()
pascals = sensor.read_pressure()
press = pascals / 100
hum = sensor.read_humidity()

def writeDATA(data):
	f = open('LOG.txt', 'a')
	f.write('TEMP ' + temp + ' | PRESS ' + press + ' | HUM ' + hum + '\n')
	f.close()

def __mai	
while True:
	#getWS()
	#getT()
	#getHU()
	writeDATA(data)
	time.sleep(5)
