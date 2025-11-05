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
