import time
import board
from busio import I2C
import adafruit_bme680
from datetime import datetime

i2c = I2C(board.SCL, board.SDA)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

bme680.sea_level_pressure = 1013.25

#open file here
filename = str(datetime.now()) + ".csv"
fileRef = open(filename, "w+")

while True:
    print("\nTemperature: %0.1f C" % bme680.temperature)
    print("Gas: %d ohm" % bme680.gas)
    print("Humidity: %0.1f %%" % bme680.humidity)
    print("Pressure: %0.3f hPa" % bme680.pressure)
    print("Altitude: %0.2f meters" % bme680.altitude)

    fileRef.write("{}, {}, {}, {}, {}\r\n".format(bme680.temperature, bme680.gas, bme680.humidity, bme680.pressure, bme680.altitude))

    time.sleep(1)
