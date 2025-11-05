from excepciones.modo_no_disponible_excepcion import ModoNoDisponibleException

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
