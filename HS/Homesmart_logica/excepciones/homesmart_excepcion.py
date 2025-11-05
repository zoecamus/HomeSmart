class HomeSmartException(Exception):
    """Excepción base para todos los errores del sistema HomeSmart."""

    def __init__(self, mensaje: str, codigo: str = "ERROR 00"):
        super().__init__(mensaje)
        self.codigo = codigo
        self.mensaje = mensaje

    def __str__(self):
        return f"[{self.codigo}] {self.mensaje}"
