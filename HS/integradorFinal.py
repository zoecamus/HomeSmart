"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/zoe/Diseño de sistemas /HomeSmart/HS
Fecha de generacion: 2025-11-05 09:42:55
Total de archivos integrados: 28
Total de directorios procesados: 6
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. main.py
#
# DIRECTORIO: Homesmart_logica/entidades
#   2. __init__.py
#   3. camara.py
#   4. dispositivo.py
#   5. luz.py
#   6. sensor.py
#   7. sensor_humedad.py
#   8. sensor_temperatura.py
#   9. usuario.py
#
# DIRECTORIO: Homesmart_logica/excepciones
#   10. __init__.py
#   11. dispositivo_inaccesible_Excepcion.py
#   12. domotica_excepcion.py
#   13. homesmart_excepcion.py
#   14. modo_no_disponible_excepcion.py
#   15. sensor_error_excepcion.py
#
# DIRECTORIO: Homesmart_logica/patrones
#   16. __init__.py
#   17. factory.py
#   18. observer.py
#   19. singleton.py
#   20. strategy.py
#
# DIRECTORIO: Homesmart_logica/python_homesmart
#   21. __init__.py
#   22. constantes.py
#
# DIRECTORIO: Homesmart_logica/servicios
#   23. __init__.py
#   24. automatizacion_service.py
#   25. dispositivos_service.py
#   26. registro_domotico_service.py
#   27. sensor_service.py
#   28. usuario_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/28: main.py
# Directorio: .
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/main.py
# ==============================================================================

import time
import random
from datetime import datetime

# === IMPORTS DE ENTIDADES ===
from HS.Homesmart_logica.entidades.usuario import Usuario
from HS.Homesmart_logica.entidades.luz import Luz
from HS.Homesmart_logica.entidades.camara import Camara
from HS.Homesmart_logica.entidades.sensor_humedad import SensorHumedad
from HS.Homesmart_logica.entidades.sensor_temperatura import SensorTemperatura
# === IMPORTS DE SERVICIOS ===
from HS.Homesmart_logica.servicios.dispositivos_service import DispositivoService
from HS.Homesmart_logica.servicios.sensor_service import SensorService
from HS.Homesmart_logica.servicios.usuario_service import UsuarioService
from HS.Homesmart_logica.servicios.automatizacion_service import AutomatizacionService, ReglaAutomatica
from HS.Homesmart_logica.servicios.registro_domotico_service import RegistroDomoticoService
# === IMPORTS DE EXCEPCIONES ===
from HS.Homesmart_logica.excepciones.domotica_excepcion import DomoticaException


# === CONFIGURACIÓN DE DISPOSITIVOS ===
CONFIG_DISPOSITIVOS = {
    "luces": 3,
    "camaras": 2,
    "sensores_temperatura": 1,
    "sensores_humedad": 1
}

# ======================================================================
#                 SISTEMA DOMÓTICO INTELIGENTE - HOMESMART
# ======================================================================

print("=" * 70)
print("      SISTEMA DOMÓTICO INTELIGENTE - HOMESMART (Proyecto Final)")
print("=" * 70)

try:
    # ------------------------------------------------------------------
    # INICIALIZACIÓN DE USUARIO Y SERVICIOS
    # ------------------------------------------------------------------
    usuario = Usuario("Zoe Camus")

    disp_service = DispositivoService()
    sensor_service = SensorService()
    user_service = UsuarioService()
    auto_service = AutomatizacionService()
    registro_service = RegistroDomoticoService()

    print("\n[INICIO] Servicios inicializados correctamente.")
    print(f"[USUARIO] Bienvenida, {usuario.nombre}.\n")

    # ------------------------------------------------------------------
    # CREACIÓN DE DISPOSITIVOS DESDE CONFIGURACIÓN
    # ------------------------------------------------------------------
    print("Creando dispositivos inteligentes...\n")

    luces = [Luz(i + 1, f"Ambiente {i + 1}") for i in range(CONFIG_DISPOSITIVOS["luces"])]
    camaras = [Camara(i + 1, f"Sector {i + 1}") for i in range(CONFIG_DISPOSITIVOS["camaras"])]
    sensores_temp = [SensorTemperatura(1, "Sala Principal")]
    sensores_hum = [SensorHumedad(2, "Cocina")]

    for d in luces + camaras + sensores_temp + sensores_hum:
        user_service.registrar_dispositivo(usuario, d)

    usuario.listar_dispositivos()

    # ------------------------------------------------------------------
    # DEMOSTRACIÓN DE LECTURA DE SENSORES
    # ------------------------------------------------------------------
    print("\n--- Lectura de Sensores ---")
    temp = sensor_service.leer_sensor(sensores_temp[0])
    hum = sensor_service.leer_sensor(sensores_hum[0])

    if sensor_service.es_temperatura_peligrosa(temp):
        print(f"[ALERTA] Temperatura fuera de rango: {temp}°C")
    else:
        print(f"[OK] Temperatura normal: {temp}°C")

    if sensor_service.es_humedad_baja(hum):
        print(f"[ALERTA] Humedad baja: {hum}%")
    else:
        print(f"[OK] Humedad estable: {hum}%")

    # ------------------------------------------------------------------
    # DEMOSTRACIÓN DE AUTOMATIZACIONES (PATRÓN OBSERVER)
    # ------------------------------------------------------------------
    print("\n--- Reglas Automáticas ---")
    aire = Luz(99, "Aire Acondicionado", intensidad=100)

    regla_temp = ReglaAutomatica(
        "Encender Aire por Calor",
        condicion=lambda: sensores_temp[0].leer() > 28,
        accion=lambda: disp_service.encender(aire)
    )

    regla_hum = ReglaAutomatica(
        "Apagar Aire por Humedad Alta",
        condicion=lambda: sensores_hum[0].leer() > 70,
        accion=lambda: disp_service.apagar(aire)
    )

    auto_service.registrar_regla(regla_temp)
    auto_service.registrar_regla(regla_hum)

    print("[SIMULACIÓN] Evaluando reglas automáticas (5 ciclos)...")
    for _ in range(5):
        auto_service.evaluar_todas()
        time.sleep(0.8)

    # ------------------------------------------------------------------
    # GUARDAR ESTADO DEL SISTEMA
    # ------------------------------------------------------------------
    print("\n--- Guardando estado del sistema ---")
    estado_casa = {
        "usuario": usuario.nombre,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "dispositivos": [str(d) for d in usuario.dispositivos] + [str(aire)]
    }

    registro_service.persistir(usuario.nombre, estado_casa)
    print("[OK] Estado del hogar guardado exitosamente.")

    # ------------------------------------------------------------------
    # MOSTRAR RESUMEN FINAL
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("                   EJEMPLO COMPLETADO EXITOSAMENTE")
    print("=" * 70)
    print(" [OK] SINGLETON   - Gestor único de dispositivos")
    print(" [OK] FACTORY     - Creación de sensores y luces")
    print(" [OK] OBSERVER    - Reglas automáticas ejecutadas")
    print(" [OK] STRATEGY    - Evaluación de condiciones ambientales")
    print(" [OK] PERSISTENCIA - Estado del sistema guardado correctamente")
    print("=" * 70)

except DomoticaException as e:
    print(f"[ERROR DOMÓTICO] {e}")

except Exception as ex:
    print(f"[ERROR CRÍTICO] {ex}")

finally:
    print("\n[FIN DEL PROGRAMA] Ejecución finalizada.")



################################################################################
# DIRECTORIO: Homesmart_logica/entidades
################################################################################

# ==============================================================================
# ARCHIVO 2/28: __init__.py
# Directorio: Homesmart_logica/entidades
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/entidades/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 3/28: camara.py
# Directorio: Homesmart_logica/entidades
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/entidades/camara.py
# ==============================================================================

from Homesmart_logica.entidades.dispositivo import Dispositivo

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


# ==============================================================================
# ARCHIVO 4/28: dispositivo.py
# Directorio: Homesmart_logica/entidades
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/entidades/dispositivo.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 5/28: luz.py
# Directorio: Homesmart_logica/entidades
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/entidades/luz.py
# ==============================================================================

from Homesmart_logica.entidades.dispositivo import Dispositivo

class Luz(Dispositivo):
    """
    Luz inteligente, con control de intensidad y modo automático.
    """
    def __init__(self, id_dispositivo: int, ubicacion: str, intensidad: int = 100):
        super().__init__(id_dispositivo, "Luz", ubicacion)
        self.intensidad = intensidad  # 0 a 100 %

    def ajustar_intensidad(self, valor: int):
        if 0 <= valor <= 100:
            self.intensidad = valor
            print(f"[LUZ] Intensidad ajustada al {valor}% en {self.ubicacion}")
        else:
            raise ValueError("La intensidad debe estar entre 0 y 100.")

    def __str__(self):
        estado = "ENCENDIDA" if self.encendido else "APAGADA"
        return f"Luz (Ubicación: {self.ubicacion}, Intensidad: {self.intensidad}%, Estado: {estado})"


# ==============================================================================
# ARCHIVO 6/28: sensor.py
# Directorio: Homesmart_logica/entidades
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/entidades/sensor.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 7/28: sensor_humedad.py
# Directorio: Homesmart_logica/entidades
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/entidades/sensor_humedad.py
# ==============================================================================

import random
from Homesmart_logica.entidades.sensor import Sensor

class SensorHumedad(Sensor):
    def __init__(self, id_sensor: int, ubicacion: str):
        super().__init__(id_sensor, "Humedad", ubicacion)

    def leer(self):
        # valor simulado entre 20% y 90%
        self.valor = round(random.uniform(20.0, 90.0), 2)
        return self.valor


# ==============================================================================
# ARCHIVO 8/28: sensor_temperatura.py
# Directorio: Homesmart_logica/entidades
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/entidades/sensor_temperatura.py
# ==============================================================================

import random
from  Homesmart_logica.entidades.sensor import Sensor

class SensorTemperatura(Sensor):
    def __init__(self, id_sensor: int, ubicacion: str):
        super().__init__(id_sensor, "Temperatura", ubicacion)

    def leer(self):
        # valor simulado entre -5°C y 40°C
        self.valor = round(random.uniform(-5.0, 40.0), 2)
        return self.valor


# ==============================================================================
# ARCHIVO 9/28: usuario.py
# Directorio: Homesmart_logica/entidades
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/entidades/usuario.py
# ==============================================================================

class Usuario:
    """
    Representa al propietario o usuario del sistema HomeSmart.
    """
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.dispositivos = []

    def agregar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)

    def listar_dispositivos(self):
        print(f"[USUARIO] {self.nombre} posee {len(self.dispositivos)} dispositivos:")
        for d in self.dispositivos:
            print(f"  - {d}")

    def __str__(self):
        return f"Usuario({self.nombre}, {len(self.dispositivos)} dispositivos)"



################################################################################
# DIRECTORIO: Homesmart_logica/excepciones
################################################################################

# ==============================================================================
# ARCHIVO 10/28: __init__.py
# Directorio: Homesmart_logica/excepciones
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/excepciones/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 11/28: dispositivo_inaccesible_Excepcion.py
# Directorio: Homesmart_logica/excepciones
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/excepciones/dispositivo_inaccesible_Excepcion.py
# ==============================================================================

from Homesmart_logica.excepciones.homesmart_excepcion import HomeSmartException

class DispositivoInaccesibleException(HomeSmartException):
    """Error lanzado cuando un dispositivo no responde o está fuera de línea."""

    def __init__(self, nombre_dispositivo: str):
        super().__init__(
            mensaje=f"El dispositivo '{nombre_dispositivo}' no responde o está desconectado.",
            codigo="ERROR 01"
        )


# ==============================================================================
# ARCHIVO 12/28: domotica_excepcion.py
# Directorio: Homesmart_logica/excepciones
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/excepciones/domotica_excepcion.py
# ==============================================================================

class DomoticaException(Exception):
    """
    Excepción base para todo el sistema HomeSmart.
    Incluye código de error, mensaje técnico y mensaje de usuario.
    """
    def __init__(self, codigo: str, mensaje_usuario: str, mensaje_tecnico: str = None):
        self.codigo = codigo
        self.mensaje_usuario = mensaje_usuario
        self.mensaje_tecnico = mensaje_tecnico or mensaje_usuario
        super().__init__(self.__str__())

    def __str__(self):
        return f"[ERROR {self.codigo}] {self.mensaje_usuario}"


class SensorInactivoException(DomoticaException):
    """
    Se lanza cuando un sensor no responde o está fuera de servicio.
    """
    def __init__(self, sensor_nombre: str):
        super().__init__(
            codigo="HS-001",
            mensaje_usuario=f"El sensor '{sensor_nombre}' no responde o está inactivo.",
            mensaje_tecnico=f"Fallo al leer el sensor: {sensor_nombre}"
        )


class ErrorPersistenciaException(DomoticaException):
    """
    Se lanza cuando hay un error al guardar o leer datos en disco.
    """
    def __init__(self, operacion: str, causa: str):
        super().__init__(
            codigo="HS-002",
            mensaje_usuario=f"Error durante la operación de {operacion.lower()}.",
            mensaje_tecnico=f"Fallo en persistencia ({operacion}): {causa}"
        )


# ==============================================================================
# ARCHIVO 13/28: homesmart_excepcion.py
# Directorio: Homesmart_logica/excepciones
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/excepciones/homesmart_excepcion.py
# ==============================================================================

class HomeSmartException(Exception):
    """Excepción base para todos los errores del sistema HomeSmart."""

    def __init__(self, mensaje: str, codigo: str = "ERROR 00"):
        super().__init__(mensaje)
        self.codigo = codigo
        self.mensaje = mensaje

    def __str__(self):
        return f"[{self.codigo}] {self.mensaje}"


# ==============================================================================
# ARCHIVO 14/28: modo_no_disponible_excepcion.py
# Directorio: Homesmart_logica/excepciones
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/excepciones/modo_no_disponible_excepcion.py
# ==============================================================================

from Homesmart_logica.excepciones.homesmart_excepcion import HomeSmartException

class ModoNoDisponibleException(HomeSmartException):
    """Error lanzado cuando el modo seleccionado no está disponible."""

    def __init__(self, modo: str):
        super().__init__(
            mensaje=f"El modo '{modo}' no está disponible en este sistema.",
            codigo="ERROR 03"
        )


# ==============================================================================
# ARCHIVO 15/28: sensor_error_excepcion.py
# Directorio: Homesmart_logica/excepciones
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/excepciones/sensor_error_excepcion.py
# ==============================================================================

from Homesmart_logica.excepciones.homesmart_excepcion import HomeSmartException

class SensorErrorException(HomeSmartException):
    """Error lanzado cuando un sensor devuelve valores fuera de rango o falla la lectura."""

    def __init__(self, tipo_sensor: str, valor):
        super().__init__(
            mensaje=f"Error en sensor '{tipo_sensor}': valor inválido ({valor}).",
            codigo="ERROR 02"
        )



################################################################################
# DIRECTORIO: Homesmart_logica/patrones
################################################################################

# ==============================================================================
# ARCHIVO 16/28: __init__.py
# Directorio: Homesmart_logica/patrones
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/patrones/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 17/28: factory.py
# Directorio: Homesmart_logica/patrones
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/patrones/factory.py
# ==============================================================================

from Homesmart_logica.entidades.luz import Luz
from Homesmart_logica.entidades.camara import Camara

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


# ==============================================================================
# ARCHIVO 18/28: observer.py
# Directorio: Homesmart_logica/patrones
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/patrones/observer.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 19/28: singleton.py
# Directorio: Homesmart_logica/patrones
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/patrones/singleton.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 20/28: strategy.py
# Directorio: Homesmart_logica/patrones
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/patrones/strategy.py
# ==============================================================================

from Homesmart_logica.excepciones.modo_no_disponible_excepcion import ModoNoDisponibleException

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



################################################################################
# DIRECTORIO: Homesmart_logica/python_homesmart
################################################################################

# ==============================================================================
# ARCHIVO 21/28: __init__.py
# Directorio: Homesmart_logica/python_homesmart
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/python_homesmart/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 22/28: constantes.py
# Directorio: Homesmart_logica/python_homesmart
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/python_homesmart/constantes.py
# ==============================================================================

# MODOS DE FUNCIONAMIENTO (Strategy)
MODO_ECOLOGICO = "Ecológico"
MODO_SEGURIDAD = "Seguridad Nocturna"
MODO_NORMAL = "Normal"

MODOS_DISPONIBLES = [MODO_ECOLOGICO, MODO_SEGURIDAD, MODO_NORMAL]

# CONFIGURACIÓN DE DISPOSITIVOS
CONFIG_DISPOSITIVOS = {
    "luz": {
        "consumo": 0.06,  # kWh por minuto
        "ubicaciones": ["Living", "Dormitorio", "Cocina"]
    },
    "camara": {
        "consumo": 0.12,
        "ubicaciones": ["Entrada", "Garaje"]
    },
}

# UMBRALES DE SENSORES
SENSOR_TEMPERATURA_UMBRAL = {
    "min": 18,  # °C
    "max": 26
}

SENSOR_HUMEDAD_UMBRAL = {
    "min": 30,  # %
    "max": 70
}

# ALERTAS DEL SISTEMA
ALERTA_MOVIMIENTO = "Movimiento detectado"
ALERTA_TEMPERATURA = "Temperatura fuera de rango"
ALERTA_HUMEDAD = "Humedad fuera de rango"

# DATOS DEL HOGAR (para simular en la salida)
HOGAR_INFO = {
    "propietario": "Zoe Camus",
    "ubicacion": "Mendoza, Argentina",
    "superficie": 120.0,  # m²
    "dispositivos": 5,
}



################################################################################
# DIRECTORIO: Homesmart_logica/servicios
################################################################################

# ==============================================================================
# ARCHIVO 23/28: __init__.py
# Directorio: Homesmart_logica/servicios
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/servicios/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 24/28: automatizacion_service.py
# Directorio: Homesmart_logica/servicios
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/servicios/automatizacion_service.py
# ==============================================================================

# servicios/automatizacion_service.py

class ReglaAutomatica:
    """
    Representa una regla domótica que se ejecuta automáticamente
    cuando se cumple una condición del sistema.
    """
    def __init__(self, nombre, condicion, accion):
        self.nombre = nombre
        self.condicion = condicion  # función que devuelve True/False
        self.accion = accion        # función que se ejecuta al cumplirse

    def __str__(self):
        return f"ReglaAutomatica({self.nombre})"


class AutomatizacionService:
    """
    Servicio encargado de registrar y evaluar reglas automáticas.
    Implementa una versión simple del patrón OBSERVER/STRATEGY.
    """
    def __init__(self):
        self.reglas = []
        self.reglas_ejecutadas = set()

    def registrar_regla(self, regla: ReglaAutomatica):
        print(f"[AUTOMATIZACIÓN] Regla registrada: {regla.nombre}")
        self.reglas.append(regla)

    def evaluar_todas(self):
        for regla in self.reglas:
            try:
                if regla.condicion():
                    if regla.nombre not in self.reglas_ejecutadas:
                        print(f"[AUTOMATIZACIÓN] Regla '{regla.nombre}' disparada.")
                        regla.accion()
                        self.reglas_ejecutadas.add(regla.nombre)
                else:
                    # Si ya no se cumple, se habilita nuevamente
                    if regla.nombre in self.reglas_ejecutadas:
                        self.reglas_ejecutadas.remove(regla.nombre)
            except Exception as e:
                print(f"[ERROR AUTOMATIZACIÓN] Regla '{regla.nombre}' falló: {e}")


# ==============================================================================
# ARCHIVO 25/28: dispositivos_service.py
# Directorio: Homesmart_logica/servicios
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/servicios/dispositivos_service.py
# ==============================================================================


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


# ==============================================================================
# ARCHIVO 26/28: registro_domotico_service.py
# Directorio: Homesmart_logica/servicios
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/servicios/registro_domotico_service.py
# ==============================================================================

import os
import pickle
from Homesmart_logica.excepciones.domotica_excepcion import ErrorPersistenciaException

class RegistroDomoticoService:

    def persistir(self, usuario_nombre, estado):
        try:
            os.makedirs("data", exist_ok=True)
            path = f"data/{usuario_nombre}.dat"
            with open(path, "wb") as f:
                pickle.dump(estado, f)
            print(f"[PERSISTENCIA] Estado domótico guardado en {path}")
        except Exception as e:
            raise ErrorPersistenciaException("escritura", str(e))


# ==============================================================================
# ARCHIVO 27/28: sensor_service.py
# Directorio: Homesmart_logica/servicios
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/servicios/sensor_service.py
# ==============================================================================

from typing import Any

class SensorService:
    """
    Servicio para leer sensores (temperatura, humedad, movimiento, etc.)
    Las entidades de sensor deberían exponer un método .leer() o similar.
    """

    def leer_sensor(self, sensor: Any) -> float:
        if not hasattr(sensor, "leer"):
            raise AttributeError("El sensor no implementa 'leer()'.")
        valor = sensor.leer()
        print(f"[SENSOR] {sensor} → valor leído: {valor}")
        return valor

    def es_temperatura_peligrosa(self, valor: float) -> bool:
        # regla simple, la podemos mover a constantes
        return valor >= 30.0 or valor <= 5.0

    def es_humedad_baja(self, valor: float) -> bool:
        return valor < 35.0


# ==============================================================================
# ARCHIVO 28/28: usuario_service.py
# Directorio: Homesmart_logica/servicios
# Ruta completa: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/servicios/usuario_service.py
# ==============================================================================

from typing import List, Any
from Homesmart_logica.entidades.usuario import Usuario


class UsuarioService:
    """
    Maneja al usuario/dueño y sus dispositivos.
    """

    def registrar_dispositivo(self, usuario: Usuario, dispositivo: Any) -> None:
        usuario.dispositivos.append(dispositivo)
        print(f"[USUARIO] {usuario.nombre} agregó dispositivo: {dispositivo}")

    def listar_dispositivos(self, usuario: Usuario) -> List[Any]:
        print(f"[USUARIO] Dispositivos de {usuario.nombre}:")
        for d in usuario.dispositivos:
            print(f"  - {d}")
        return list(usuario.dispositivos)



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 28
# Generado: 2025-11-05 09:42:55
################################################################################
