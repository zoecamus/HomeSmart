
from typing import Any


class DispositivoService:
    """
    Servicio básico para operar sobre dispositivos del sistema domótico.
    No crea dispositivos: los recibe ya instanciados desde entidades.
    """

    def encender(self, dispositivo: Any) -> None:
        # asumimos que la entidad tiene .encendida o .activo o similar
        if hasattr(dispositivo, "encender"):
            dispositivo.encender()
            print(f"[DISPOSITIVO] {dispositivo} encendido.")
        else:
            raise AttributeError("El dispositivo no tiene método 'encender'.")

    def apagar(self, dispositivo: Any) -> None:
        if hasattr(dispositivo, "apagar"):
            dispositivo.apagar()
            print(f"[DISPOSITIVO] {dispositivo} apagado.")
        else:
            raise AttributeError("El dispositivo no tiene método 'apagar'.")

    def estado(self, dispositivo: Any) -> str:
        # intentamos varios nombres típicos
        if hasattr(dispositivo, "encendida"):
            return "ENCENDIDO" if dispositivo.encendida else "APAGADO"
        if hasattr(dispositivo, "activo"):
            return "ACTIVO" if dispositivo.activo else "INACTIVO"
        if hasattr(dispositivo, "bloqueada"):
            return "BLOQUEADO" if dispositivo.bloqueada else "DESBLOQUEADO"
        return "DESCONOCIDO"
