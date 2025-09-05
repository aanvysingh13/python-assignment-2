sensor_data = {1: 2.3, 2: 4.5, 3: 1.8, 4: 3.6}

high_sensors = []
for sensor_id, reading in sensor_data.items():
    if reading > 3.0:
        high_sensors.append(sensor_id)

print("Sensor IDs with reading above 3.0:", high_sensors)