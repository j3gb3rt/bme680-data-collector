import time
import board
from busio import I2C
import adafruit_bme680

i2c = I2C(board.SCL, board.SDA)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

bme680.sea_level_pressure = 1013.25

#open file here

while True:
    print("\nTemperature: %0.1f C" % bme680.temperature)
    print("Gas: %d ohm" % bme680.temperature)
    print("Humidity: %0.1f %%" % bme680.temperature)
    print("Pressure: %0.3f hPa" % bme680.temperature)
    print("Altitude: %0.2f meters" % bme680.temperature)

    time.sleep(1)
