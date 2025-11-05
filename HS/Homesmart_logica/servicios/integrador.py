"""
Archivo integrador generado automaticamente
Directorio: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/servicios
Fecha: 2025-11-05 09:42:55
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/servicios/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: automatizacion_service.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/servicios/automatizacion_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/6: dispositivos_service.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/servicios/dispositivos_service.py
# ================================================================================


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


# ================================================================================
# ARCHIVO 4/6: registro_domotico_service.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/servicios/registro_domotico_service.py
# ================================================================================

import os
import pickle
from excepciones.domotica_excepcion import ErrorPersistenciaException

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


# ================================================================================
# ARCHIVO 5/6: sensor_service.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/servicios/sensor_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 6/6: usuario_service.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/servicios/usuario_service.py
# ================================================================================

from typing import List, Any
from entidades.usuario import Usuario


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


