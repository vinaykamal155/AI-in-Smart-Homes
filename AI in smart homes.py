import random
class SmartThermostat:
    def _init_(self):
        self.current_temp = 70
    def get_temp(self):
        return self.current_temp
    def set_temp(self, temp):
        self.current_temp = temp
class OccupancySensor:
    def _init_(self):
       self.current_occupancy = 0
    def get_occupancy(self):
        return self.current_occupancy
    def set_occupancy(self, occupancy):
        self.current_occupancy = occupancy

# Initialize devices
thermostat = SmartThermostat()
occupancy_sensor = OccupancySensor()

# Simulate occupancy data
for i in range(24):
    occupancy_sensor.set_occupancy(random.randint(0, 1))
    current_occupancy = occupancy_sensor.get_occupancy()
    if current_occupancy == 0:
        # No one is home, set temperature to 65 degrees
        thermostat.set_temp(65)
    else:
        # Someone is home, set temperature to 72 degrees
        thermostat.set_temp(72)
        current_temp = thermostat.get_temp()
    print(f"Hour {i}: Occupancy = {current_occupancy}, Temperature = {current_temp}")
    