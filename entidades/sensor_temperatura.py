# python_homesmart/entidades/sensor_temperatura.py

import random
from entidades.sensor import Sensor

class SensorTemperatura(Sensor):
    def __init__(self, id_sensor: int, ubicacion: str):
        super().__init__(id_sensor, "Temperatura", ubicacion)

    def leer(self):
        # valor simulado entre -5°C y 40°C
        self.valor = round(random.uniform(-5.0, 40.0), 2)
        return self.valor
