# Pi Setup

Install raspberry pi OS (lite) with rpi-imager
Do first boot in pi
Resize in gparted

Boot in pi
```
sudo su
apt install git vim
mkdir /mnt/nt-storage
echo '/dev/mmcblk0p3  /mnt/nt-storage auto  defaults  0 0' >> /etc/fstab
mount -a
cd /mnt/nt-storage
mkdir data
git clone



# Run at startup

To run at startup add this to the root users crontab using, `crontab -e`

```
@reboot python3 /mnt/nt-storage/bme680-data-collector/datacollector.py &
```

