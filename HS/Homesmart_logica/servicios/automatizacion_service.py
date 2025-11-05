# servicios/automatizacion_service.py

class ReglaAutomatica:
    """
    Representa una regla domótica que se ejecuta automáticamente
    cuando se cumple una condición del sistema.
    """
    def __init__(self, nombre, condicion, accion):
        self.nombre = nombre
        self.condicion = condicion  # función que devuelve True/False
        self.accion = accion        # función que se ejecuta al cumplirse

    def __str__(self):
        return f"ReglaAutomatica({self.nombre})"


class AutomatizacionService:
    """
    Servicio encargado de registrar y evaluar reglas automáticas.
    Implementa una versión simple del patrón OBSERVER/STRATEGY.
    """
    def __init__(self):
        self.reglas = []
        self.reglas_ejecutadas = set()

    def registrar_regla(self, regla: ReglaAutomatica):
        print(f"[AUTOMATIZACIÓN] Regla registrada: {regla.nombre}")
        self.reglas.append(regla)

    def evaluar_todas(self):
        for regla in self.reglas:
            try:
                if regla.condicion():
                    if regla.nombre not in self.reglas_ejecutadas:
                        print(f"[AUTOMATIZACIÓN] Regla '{regla.nombre}' disparada.")
                        regla.accion()
                        self.reglas_ejecutadas.add(regla.nombre)
                else:
                    # Si ya no se cumple, se habilita nuevamente
                    if regla.nombre in self.reglas_ejecutadas:
                        self.reglas_ejecutadas.remove(regla.nombre)
            except Exception as e:
                print(f"[ERROR AUTOMATIZACIÓN] Regla '{regla.nombre}' falló: {e}")
