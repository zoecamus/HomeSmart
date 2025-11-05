from excepciones.homesmart_excepcion import HomeSmartException

class ModoNoDisponibleException(HomeSmartException):
    """Error lanzado cuando el modo seleccionado no está disponible."""

    def __init__(self, modo: str):
        super().__init__(
            mensaje=f"El modo '{modo}' no está disponible en este sistema.",
            codigo="ERROR 03"
        )
