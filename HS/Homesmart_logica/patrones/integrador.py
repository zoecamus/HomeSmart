"""
Archivo integrador generado automaticamente
Directorio: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/patrones
Fecha: 2025-11-05 09:42:55
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/patrones/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: factory.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/patrones/factory.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/5: observer.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/patrones/observer.py
# ================================================================================

class Sujeto:
    """El objeto que notifica a los observadores."""

    def __init__(self):
        self._observadores = []

    def agregar_observador(self, observador):
        self._observadores.append(observador)

    def notificar(self, mensaje: str):
        for obs in self._observadores:
            obs.actualizar(mensaje)


class Observador:
    """Interfaz base de los observadores."""
    def actualizar(self, mensaje: str):
        raise NotImplementedError


# Ejemplo de un observador concreto:
class NotificadorApp(Observador):
    """Simula la app móvil del usuario."""

    def actualizar(self, mensaje: str):
        print(f"[📱 APP] Notificación: {mensaje}")


# ================================================================================
# ARCHIVO 4/5: singleton.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/patrones/singleton.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/5: strategy.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/patrones/strategy.py
# ================================================================================

from excepciones.modo_no_disponible_excepcion import ModoNoDisponibleException

class EstrategiaAhorro:
    """Estrategia base para manejo de energía."""
    def aplicar(self, dispositivos):
        raise NotImplementedError


class ModoNormal(EstrategiaAhorro):
    def aplicar(self, dispositivos):
        print("[MODO NORMAL] Todos los dispositivos funcionan sin restricción.")


class ModoEco(EstrategiaAhorro):
    def aplicar(self, dispositivos):
        print("[MODO ECO] Bajando intensidad y apagando no esenciales...")
        for d in dispositivos:
            if "Luz" in d.nombre:
                d.ajustar_intensidad(40)
            elif "Cámara" in d.nombre:
                d.apagar()


class ModoAusente(EstrategiaAhorro):
    def aplicar(self, dispositivos):
        print("[MODO AUSENTE] Apagando todo excepto seguridad...")
        for d in dispositivos:
            if "Cámara" in d.nombre:
                d.encender()
            else:
                d.apagar()


class GestorModo:
    """Permite cambiar dinámicamente de estrategia."""
    def __init__(self, estrategia: EstrategiaAhorro):
        self.estrategia = estrategia

    def cambiar_modo(self, nuevo_modo: str):
        modos = {
            "normal": ModoNormal(),
            "eco": ModoEco(),
            "ausente": ModoAusente()
        }
        if nuevo_modo not in modos:
            raise ModoNoDisponibleException(nuevo_modo)
        self.estrategia = modos[nuevo_modo]
        print(f"[GESTOR MODO] Cambiado a '{nuevo_modo.upper()}'")

    def aplicar(self, dispositivos):
        self.estrategia.aplicar(dispositivos)


