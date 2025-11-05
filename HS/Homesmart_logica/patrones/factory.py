from entidades.luz import Luz
from entidades.camara import Camara

class DispositivoFactory:
    """Creador de dispositivos inteligentes."""

    @staticmethod
    def crear_dispositivo(tipo: str, id: int, ubicacion: str):
        tipo = tipo.lower()
        print(f"[FACTORY] Creando dispositivo '{tipo}'...")

        if tipo == "luz":
            return Luz(id, ubicacion)
        elif tipo == "camara":
            return Camara(id, ubicacion)
        else:
            raise ValueError(f"Tipo de dispositivo desconocido: '{tipo}'")
