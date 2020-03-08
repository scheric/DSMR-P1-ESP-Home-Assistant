"""Support for dsmr-esp through MQTT."""
from homeassistant.components import mqtt
from homeassistant.core import callback
from homeassistant.helpers.entity import Entity
from homeassistant.util import slugify
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv
import logging

from homeassistant.const import (
    ATTR_ATTRIBUTION, CONF_NAME, CONF_PASSWORD, CONF_USERNAME)

import json

DOMAIN = "dsmr-esp"

from .constants import CONSTANTS_SENSORS_SENSORS 


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default="EMS_ESP"): cv.string,
})

_LOGGER = logging.getLogger(__name__)
        #_LOGGER.error(f"sensor: {SENSOR_VALUE}")

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up dsmr-esp sensors."""
    
    sensors = []
     
    #add thermostat sensors DONE

    for sensor in CONSTANTS_SENSORS_SENSORS:
        sensors.append(EMS_ESPSensor(config, CONSTANTS_SENSORS_SENSORS[sensor].get("name"), CONSTANTS_SENSORS_SENSORS[sensor].get("unit") , CONSTANTS_SENSORS_SENSORS[sensor].get("icon"), CONSTANTS_SENSORS_SENSORS[sensor].get("value"), CONSTANTS_SENSORS_SENSORS[sensor].get("topic")))

    
    async_add_entities(sensors)


class EMS_ESPSensor(Entity):
    """Representation of a dsmr-esp sensor that is updated via MQTT."""

    def __init__(self, config, Name, Unit, Icon, Value, Topic):
        """Initialize the sensor."""

        self._Name = "(" + config[CONF_NAME]+ ")" + " "
        
        #self._topic = self._base + "/ems-esp/boiler_data"
        
        self._name = Name
        self._unit_of_measurement = Unit      
        self._icon = "mdi:" + Icon      
        self._value = Value
        self._topic = Topic
        self._full_topic = Topic + Value
         
        self._in = None
        self._out = None

    async def async_added_to_hass(self):
        """Subscribe to MQTT events."""

        @callback
        def message_received(message):
            """Handle new MQTT messages."""
            self._in = int(message.payload)

            self.async_schedule_update_ha_state()

        await mqtt.async_subscribe(self.hass, self._full_topic, message_received, 1)

    @property
    def name(self):
        """Return the name of the sensor supplied in constructor."""
        return self._Name + self._name

    @property
    def state(self):
        """Return the current state of the entity."""
        
        #give state to frontend
        self._out = self._in 
        
        #give state to frontend with calculation 
        if self._value == "consumption_low_tarif":
            try:
                self._out = round((self._in / 1000),2)
            except:
                pass
                
        if self._value == "consumption_high_tarif":
            try:
                self._out = round((self._in/1000),2)
            except:
                pass
                
        if self._value == "production_low_tarif":
            try:
                self._out = round((self._in/1000),2)
            except:
                pass
                
        if self._value == "production_high_tarif":
            try:
                self._out = round((self._in/1000),2)
            except:
                pass
                    
        if self._value == "gas_meter_m3":
            try:
                self._out = round((self._in/1000),2)
            except:
                pass
                
                
      
        return self._out
        
    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return {
                "topic": self._topic,
                "value: ": self._value,
                "full topic": self._full_topic,
                "input": self._in,
                "output": self._out
                } 

    @property
    def unit_of_measurement(self):
        """Return the unit_of_measurement of this sensor."""
        return self._unit_of_measurement

    @property
    def icon(self):
        """Return the icon of this sensor."""
        return self._icon
