import time
import board
from busio import I2C
from adafruit_bme280 import basic as adafruit_bme280
import adafruit_ds3231
from datetime import datetime

i2c = I2C(board.SCL, board.SDA)
rtc = adafruit_ds3231.DS3231(i2c)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c,address=0x76)

bme280.sea_level_pressure = 1013.25

def writeFirstLine(ref):
    ref.write("time, temp (C), humidity (%), pressure (hPa), altitude (meters)\r\n")

def getTime():
    #print(rtc.datetime)
    rtctime = rtc.datetime
    rtime = "{}-{}-{} {:0=2d}.{:0=2d}.{:0=2d}".format( \
        rtctime.tm_mon, rtctime.tm_mday, rtctime.tm_year, \
        rtctime.tm_hour, rtctime.tm_min, rtctime.tm_sec \
    )
    #print(rtime)
    return rtime


#open file here
baseFilename = "/mnt/nt-storage/data/"
filename = baseFilename + "full-" + getTime() + ".csv"
fullFileRef = open(filename, "w+")
writeFirstLine(fullFileRef)

minuteTimer = 60

while True:
    if (minuteTimer == 60):
        filename = baseFilename + getTime() + ".csv"
        #print(filename)
        newRef = open(filename, "w+")
        writeFirstLine(newRef)
        newRef.close()
        minuteTimer = 0

    #print("\nTemperature: %0.1f C" % bme680.temperature)
    #print("Gas: %d ohm" % bme680.gas)
    #print("Humidity: %0.1f %%" % bme680.humidity)
    #print("Pressure: %0.3f hPa" % bme680.pressure)
    #print("Altitude: %0.2f meters" % bme680.altitude)

    data = "{}, {}, {}, {}, {}\r\n".format(getTime(), bme280.temperature, bme280.humidity, bme280.pressure, bme280.altitude)
    
    fullFileRef.write(data)

    fileRef = open(filename, "a+")
    fileRef.write(data)
    fileRef.close()

    minuteTimer += .1
    time.sleep(.1)

