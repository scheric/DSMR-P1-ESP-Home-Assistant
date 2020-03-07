# DSMR data aver mqtt to Home Assistant
Custom component for receiving MQTT values from dsmr-esp. I made this for clearing up the configuration.yaml files. 
 

# This project is in alpha state

### my wishlist

- [ ] Add all received mqtt states.
  - [ ] sensors
  - [ ] icons 
  - [ ] units


topics
- [x] consumption_low_tarif 
- [ ] consumption_high_tarif 
- [x] actual_consumption 
- [ ] instant_power_usage 
- [ ] instant_power_current 
- [ ] gas_meter_m3 
- [ ] actual_tarif_group 
- [ ] short_power_outages 
- [ ] long_power_outages 
- [ ] short_power_drops 
- [ ] short_power_peaks 

### How to use this

1. Create a `custom_components` folder located inside the Home Assistant `config` folder.
2. Copy the folder `dsmr-esp` into the `custom_components` folder. 
3. Add the yaml code below to your `configuration.yaml`

```yaml
sensor:
  - platform: dsmr-esp
    name: dsmr meter
```
4. reboot Home Assistant


## Notes: 

