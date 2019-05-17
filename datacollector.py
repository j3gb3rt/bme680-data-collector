import time
import board
from busio import I2C
import adafruit_bme680
from datetime import datetime

i2c = I2C(board.SCL, board.SDA)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

bme680.sea_level_pressure = 1013.25

def writeFirstLine(ref):
    ref.write("time, temp (C), gas (ohm), humidity (%), pressure (hPa), altitude (meters)\r\n")

#open file here
baseFilename = "/mnt/nt-storage/data"
filename = baseFilename + "full" + str(datetime.now()) + ".csv"
fullFileRef = open(filename, "w+")
writeFirstLine(fullFileRef)

minuteTimer = 60

while True:
    if (minuteTimer == 60):
        filename = baseFileName + str(datetime.now()) + ".csv"
        newRef = open(filename, "w+")
        writeFirstLine(newRef)
        newRef.close()
        minuteTimer = 0

    #print("\nTemperature: %0.1f C" % bme680.temperature)
    #print("Gas: %d ohm" % bme680.gas)
    #print("Humidity: %0.1f %%" % bme680.humidity)
    #print("Pressure: %0.3f hPa" % bme680.pressure)
    #print("Altitude: %0.2f meters" % bme680.altitude)

    data = "{}, {}, {}, {}, {}, {}\r\n".format(datetime.now(), bme680.temperature, bme680.gas, bme680.humidity, bme680.pressure, bme680.altitude)
    
    fullFileRef.write(data)

    fileRef = open(filename, "a+")
    fileRef.write(data)
    fileRef.close()

    minuteTimer += 1
    time.sleep(1)

