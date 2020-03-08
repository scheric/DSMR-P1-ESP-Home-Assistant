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
        "unit": "kwh",
    },
    "high tarif consumption": {
        "value": "consumption_high_tarif",
        "topic": MQTT_TOPICS[0],
        "name": "high tarif consumprion",
        "icon": "flash",
        "unit": "kwh",
    },
    "low tarif production": {
        "value": "production_low_tarif",
        "topic": MQTT_TOPICS[0],
        "name": "low tarif production",
        "icon": "flash",
        "unit": "kwh",
    },
    "high tarif production": {
        "value": "production_high_tarif",
        "topic": MQTT_TOPICS[0],
        "name": "high tarif production",
        "icon": "flash",
        "unit": "kwh",
    },
    "gas consumprion": {
        "value": "gas_meter_m3",
        "topic": MQTT_TOPICS[0],
        "name": "gas usage",
        "icon": "gas-cylinder",
        "unit": "m3",
    },
    "actual consumption": {
        "value": "actual_consumption",
        "topic": MQTT_TOPICS[0],
        "name": "average power consumption",
        "icon": "power-socket-de",
        "unit": "W",
    },
}

"""
MQTT Outgoing on sensors/power/p1meter/consumption_low_tarif: 5537351
MQTT Outgoing on sensors/power/p1meter/consumption_high_tarif: 4012968
MQTT Outgoing on sensors/power/p1meter/production_low_tarif: 80701
MQTT Outgoing on sensors/power/p1meter/production_high_tarif: 286895

MQTT Outgoing on sensors/power/p1meter/actual_consumption: 2242
MQTT Outgoing on sensors/power/p1meter/gas_meter_m3: 4867290
"""

