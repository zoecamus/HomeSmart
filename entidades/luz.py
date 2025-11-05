# python_homesmart/entidades/luz.py

from entidades.dispositivo import Dispositivo

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
