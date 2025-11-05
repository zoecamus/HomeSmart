class Sensor:
    """
    Clase base para sensores. Se especializa en temperatura, humedad, etc.
    """
    def __init__(self, id_sensor: int, tipo: str, ubicacion: str):
        self.id = id_sensor
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.valor = None

    def leer(self):
        """
        Devuelve un valor simulado (cada subclase lo redefine).
        """
        raise NotImplementedError("El método 'leer()' debe ser implementado en subclases.")

    def __str__(self):
        return f"Sensor({self.tipo}, {self.ubicacion})"
