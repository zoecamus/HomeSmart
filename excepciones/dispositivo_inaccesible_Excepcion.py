from excepciones.homesmart_excepcion import HomeSmartException

class DispositivoInaccesibleException(HomeSmartException):
    """Error lanzado cuando un dispositivo no responde o está fuera de línea."""

    def __init__(self, nombre_dispositivo: str):
        super().__init__(
            mensaje=f"El dispositivo '{nombre_dispositivo}' no responde o está desconectado.",
            codigo="ERROR 01"
        )
