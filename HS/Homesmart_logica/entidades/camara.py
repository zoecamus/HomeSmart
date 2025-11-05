from entidades.dispositivo import Dispositivo 

class Camara(Dispositivo):
    """
    Cámara inteligente con detección de movimiento.
    """
    def __init__(self, id_dispositivo: int, ubicacion: str):
        super().__init__(id_dispositivo, "Cámara", ubicacion)
        self.grabando = False

    def iniciar_grabacion(self):
        self.grabando = True
        print(f"[CÁMARA] Grabando en {self.ubicacion}")

    def detener_grabacion(self):
        self.grabando = False
        print(f"[CÁMARA] Grabación detenida en {self.ubicacion}")

    def __str__(self):
        estado = "GRABANDO" if self.grabando else "EN ESPERA"
        return f"Cámara (Ubicación: {self.ubicacion}, Estado: {estado})"
