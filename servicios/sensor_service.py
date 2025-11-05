from typing import Any

class SensorService:
    """
    Servicio para leer sensores (temperatura, humedad, movimiento, etc.)
    Las entidades de sensor deberían exponer un método .leer() o similar.
    """

    def leer_sensor(self, sensor: Any) -> float:
        if not hasattr(sensor, "leer"):
            raise AttributeError("El sensor no implementa 'leer()'.")
        valor = sensor.leer()
        print(f"[SENSOR] {sensor} → valor leído: {valor}")
        return valor

    def es_temperatura_peligrosa(self, valor: float) -> bool:
        # regla simple, la podemos mover a constantes
        return valor >= 30.0 or valor <= 5.0

    def es_humedad_baja(self, valor: float) -> bool:
        return valor < 35.0
