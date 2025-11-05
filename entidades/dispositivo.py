# python_homesmart/entidades/dispositivos.py

class Dispositivo:
    """
    Clase base para todos los dispositivos inteligentes.
    Define atributos y comportamiento común.
    """

    def __init__(self, id_dispositivo: int, nombre: str, ubicacion: str):
        self.id = id_dispositivo
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.encendido = False

    def encender(self):
        if self.encendido:
            raise Exception(f"El dispositivo '{self.nombre}' ya está encendido.")
        self.encendido = True
        print(f"[{self.nombre.upper()}] Encendido en {self.ubicacion}")

    def apagar(self):
        if not self.encendido:
            raise Exception(f"El dispositivo '{self.nombre}' ya está apagado.")
        self.encendido = False
        print(f"[{self.nombre.upper()}] Apagado en {self.ubicacion}")

    def __str__(self):
        estado = "ENCENDIDO" if self.encendido else "APAGADO"
        return f"{self.nombre.title()} (ID: {self.id}, Ubicación: {self.ubicacion}, Estado: {estado})"
