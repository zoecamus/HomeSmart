"""
Archivo integrador generado automaticamente
Directorio: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/excepciones
Fecha: 2025-11-05 09:42:55
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/excepciones/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: dispositivo_inaccesible_Excepcion.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/excepciones/dispositivo_inaccesible_Excepcion.py
# ================================================================================

from excepciones.homesmart_excepcion import HomeSmartException

class DispositivoInaccesibleException(HomeSmartException):
    """Error lanzado cuando un dispositivo no responde o está fuera de línea."""

    def __init__(self, nombre_dispositivo: str):
        super().__init__(
            mensaje=f"El dispositivo '{nombre_dispositivo}' no responde o está desconectado.",
            codigo="ERROR 01"
        )


# ================================================================================
# ARCHIVO 3/6: domotica_excepcion.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/excepciones/domotica_excepcion.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/6: homesmart_excepcion.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/excepciones/homesmart_excepcion.py
# ================================================================================

class HomeSmartException(Exception):
    """Excepción base para todos los errores del sistema HomeSmart."""

    def __init__(self, mensaje: str, codigo: str = "ERROR 00"):
        super().__init__(mensaje)
        self.codigo = codigo
        self.mensaje = mensaje

    def __str__(self):
        return f"[{self.codigo}] {self.mensaje}"


# ================================================================================
# ARCHIVO 5/6: modo_no_disponible_excepcion.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/excepciones/modo_no_disponible_excepcion.py
# ================================================================================

from excepciones.homesmart_excepcion import HomeSmartException

class ModoNoDisponibleException(HomeSmartException):
    """Error lanzado cuando el modo seleccionado no está disponible."""

    def __init__(self, modo: str):
        super().__init__(
            mensaje=f"El modo '{modo}' no está disponible en este sistema.",
            codigo="ERROR 03"
        )


# ================================================================================
# ARCHIVO 6/6: sensor_error_excepcion.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/excepciones/sensor_error_excepcion.py
# ================================================================================

from excepciones.homesmart_excepcion import HomeSmartException

class SensorErrorException(HomeSmartException):
    """Error lanzado cuando un sensor devuelve valores fuera de rango o falla la lectura."""

    def __init__(self, tipo_sensor: str, valor):
        super().__init__(
            mensaje=f"Error en sensor '{tipo_sensor}': valor inválido ({valor}).",
            codigo="ERROR 02"
        )


