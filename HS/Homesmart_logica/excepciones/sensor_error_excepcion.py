from excepciones.homesmart_excepcion import HomeSmartException

class SensorErrorException(HomeSmartException):
    """Error lanzado cuando un sensor devuelve valores fuera de rango o falla la lectura."""

    def __init__(self, tipo_sensor: str, valor):
        super().__init__(
            mensaje=f"Error en sensor '{tipo_sensor}': valor inválido ({valor}).",
            codigo="ERROR 02"
        )
