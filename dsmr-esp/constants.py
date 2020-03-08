"""constants for dsmr-esp"""

MQTT_TOPICS = [
    "sensors/power/p1meter/", #0

]

CONSTANTS_SENSORS_METER_READINGS = {
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
    }
}
    
CONSTANTS_SENSORS_AVERAGE_READINGS = {
    "actual consumption": {
        "value": "actual_consumption",
        "topic": MQTT_TOPICS[0],
        "name": "average power consumption",
        "icon": "power-socket-de",
        "unit": "W",
    },
    "actual production": {
        "value": "actual_production",
        "topic": MQTT_TOPICS[0],
        "name": "average power production",
        "icon": "solar-panel-large",
        "unit": "W",
    }
}

CONSTANTS_SENSORS_INSTANTANEOUS_READINGS = {
    "instant consumption": {
        "value": "instant_power_usage",
        "topic": MQTT_TOPICS[0],
        "name": "instant power consumption",
        "icon": "power-socket-de",
        "unit": "W",
    },
    "instant production": {
        "value": "instant_power_production",
        "topic": MQTT_TOPICS[0],
        "name": "instant power production",
        "icon": "solar-panel-large",
        "unit": "W",
    },
    "instant current": {
        "value": "instant_current",
        "topic": MQTT_TOPICS[0],
        "name": "instant current",
        "icon": "current-ac",
        "unit": "A",
    },
    "instant voltage": {
        "value": "instant_voltage",
        "topic": MQTT_TOPICS[0],
        "name": "instant grid voltage",
        "icon": "speedometer",
        "unit": "V",
    },
}

"""
MQTT Outgoing on sensors/power/p1meter/consumption_low_tarif: 5542083
MQTT Outgoing on sensors/power/p1meter/consumption_high_tarif: 4012968
MQTT Outgoing on sensors/power/p1meter/production_low_tarif: 81160
MQTT Outgoing on sensors/power/p1meter/production_high_tarif: 286895
MQTT Outgoing on sensors/power/p1meter/gas_meter_m3: 4871804

MQTT Outgoing on sensors/power/p1meter/actual_consumption: 2045
MQTT Outgoing on sensors/power/p1meter/actual_production: 0

MQTT Outgoing on sensors/power/p1meter/instant_power_usage: 2099
MQTT Outgoing on sensors/power/p1meter/instant_power_production: 0
MQTT Outgoing on sensors/power/p1meter/instant_current: 0
MQTT Outgoing on sensors/power/p1meter/instant_voltage: 226000
"""

