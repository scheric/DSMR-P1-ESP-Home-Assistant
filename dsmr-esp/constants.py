"""constants for dsmr-esp"""

MQTT_TOPICS = [
    "sensors/power/p1meter/", #0

]
    
CONSTANTS_SENSORS_SENSORS = {
    "low tarif consumption": {
        "value": "consumption_low_tarif",
        "topic": MQTT_TOPICS[0],
        "name": "low tarif consumprion",
        "icon": "flash",
        "unit": kwh,
    },
}

