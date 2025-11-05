import random
from entidades.sensor import Sensor

class SensorHumedad(Sensor):
    def __init__(self, id_sensor: int, ubicacion: str):
        super().__init__(id_sensor, "Humedad", ubicacion)

    def leer(self):
        # valor simulado entre 20% y 90%
        self.valor = round(random.uniform(20.0, 90.0), 2)
        return self.valor
