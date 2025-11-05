class Sujeto:
    """El objeto que notifica a los observadores."""

    def __init__(self):
        self._observadores = []

    def agregar_observador(self, observador):
        self._observadores.append(observador)

    def notificar(self, mensaje: str):
        for obs in self._observadores:
            obs.actualizar(mensaje)


class Observador:
    """Interfaz base de los observadores."""
    def actualizar(self, mensaje: str):
        raise NotImplementedError


# Ejemplo de un observador concreto:
class NotificadorApp(Observador):
    """Simula la app móvil del usuario."""

    def actualizar(self, mensaje: str):
        print(f"[📱 APP] Notificación: {mensaje}")
