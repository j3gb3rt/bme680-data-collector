# Run at startup

To run at startup add this to the root users crontab using, `crontab -e`

```
@reboot python3 /mnt/nt-storage/bme680-data-collector/datacollector.py &
```

