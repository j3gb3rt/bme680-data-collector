# Pi Setup

Install raspberry pi OS (lite) with rpi-imager
Do first boot in pi
Resize in gparted

Boot in pi
```
sudo su
apt update
apt updgrade
apt install git vim python3-pip
mkdir /mnt/nt-storage
echo '/dev/mmcblk0p3  /mnt/nt-storage auto  defaults  0 0' >> /etc/fstab
mount -a
cd /mnt/nt-storage
mkdir data
git clone git@github.com:j3gb3rt/bme680-data-collector.git
```
if bme280
```
git checkout bme280
pip install board adafruit-circuitpython-bme280 adafruit-circuitpython-ds3231
```

# Set time
```
python3
>>> import board
>>> import adafruit_ds3231
>>> i2c = board.I2C()
>>> rtc = adafruit_ds3231.DS3231(i2c)
>>> t = time.struct_time((2022, 3, 19, 1, 55, 0, 0, -1, -1))
>>> rtc.datetime = t
>>> rtc.datetime
time.struct_time(tm_year=2022, tm_mon=3, tm_mday=19, tm_hour=1, tm_min=55, tm_sec=8, tm_wday=0, tm_yday=-1, tm_isdst=-1)
>>> exit()
```


# Run at startup

To run at startup add this to the root users crontab using, `crontab -e`

```
@reboot python3 /mnt/nt-storage/bme680-data-collector/datacollector.py &
```

