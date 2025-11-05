# ======================================================================
#  PATRÓN SINGLETON - GESTOR CENTRAL DEL SISTEMA
# ======================================================================

class SingletonMeta(type):
    """Metaclase Singleton: garantiza que solo exista una instancia."""

    _instancias = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancias:
            instancia = super().__call__(*args, **kwargs)
            cls._instancias[cls] = instancia
        return cls._instancias[cls]


class ControlCentral(metaclass=SingletonMeta):
    """Control central del sistema HomeSmart."""

    def __init__(self):
        self.dispositivos = []
        self.sensores = []
        print("[SINGLETON] Control central iniciado.")

    def registrar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)
        print(f"[CONTROL CENTRAL] Dispositivo registrado: {dispositivo.nombre}")

    def registrar_sensor(self, sensor):
        self.sensores.append(sensor)
        print(f"[CONTROL CENTRAL] Sensor registrado: {sensor.tipo}")

    def listar(self):
        print("\n--- Dispositivos Registrados ---")
        for d in self.dispositivos:
            print(f" • {d}")
        print("\n--- Sensores Registrados ---")
        for s in self.sensores:
            print(f" • {s}")
