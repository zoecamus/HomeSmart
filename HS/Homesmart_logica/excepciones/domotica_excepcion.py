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
