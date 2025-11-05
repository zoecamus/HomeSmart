"""
Archivo integrador generado automaticamente
Directorio: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/entidades
Fecha: 2025-11-05 09:42:55
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/entidades/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/8: camara.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/entidades/camara.py
# ================================================================================

from entidades.dispositivo import Dispositivo 

class Camara(Dispositivo):
    """
    Cámara inteligente con detección de movimiento.
    """
    def __init__(self, id_dispositivo: int, ubicacion: str):
        super().__init__(id_dispositivo, "Cámara", ubicacion)
        self.grabando = False

    def iniciar_grabacion(self):
        self.grabando = True
        print(f"[CÁMARA] Grabando en {self.ubicacion}")

    def detener_grabacion(self):
        self.grabando = False
        print(f"[CÁMARA] Grabación detenida en {self.ubicacion}")

    def __str__(self):
        estado = "GRABANDO" if self.grabando else "EN ESPERA"
        return f"Cámara (Ubicación: {self.ubicacion}, Estado: {estado})"


# ================================================================================
# ARCHIVO 3/8: dispositivo.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/entidades/dispositivo.py
# ================================================================================

class Dispositivo:
    """
    Clase base para todos los dispositivos inteligentes.
    Define atributos y comportamiento común.
    """

    def __init__(self, id_dispositivo: int, nombre: str, ubicacion: str):
        self.id = id_dispositivo
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.encendido = False

    def encender(self):
        if self.encendido:
            raise Exception(f"El dispositivo '{self.nombre}' ya está encendido.")
        self.encendido = True
        print(f"[{self.nombre.upper()}] Encendido en {self.ubicacion}")

    def apagar(self):
        if not self.encendido:
            raise Exception(f"El dispositivo '{self.nombre}' ya está apagado.")
        self.encendido = False
        print(f"[{self.nombre.upper()}] Apagado en {self.ubicacion}")

    def __str__(self):
        estado = "ENCENDIDO" if self.encendido else "APAGADO"
        return f"{self.nombre.title()} (ID: {self.id}, Ubicación: {self.ubicacion}, Estado: {estado})"


# ================================================================================
# ARCHIVO 4/8: luz.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/entidades/luz.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/8: sensor.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/entidades/sensor.py
# ================================================================================

class Sensor:
    """
    Clase base para sensores. Se especializa en temperatura, humedad, etc.
    """
    def __init__(self, id_sensor: int, tipo: str, ubicacion: str):
        self.id = id_sensor
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.valor = None

    def leer(self):
        """
        Devuelve un valor simulado (cada subclase lo redefine).
        """
        raise NotImplementedError("El método 'leer()' debe ser implementado en subclases.")

    def __str__(self):
        return f"Sensor({self.tipo}, {self.ubicacion})"


# ================================================================================
# ARCHIVO 6/8: sensor_humedad.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/entidades/sensor_humedad.py
# ================================================================================

import random
from entidades.sensor import Sensor

class SensorHumedad(Sensor):
    def __init__(self, id_sensor: int, ubicacion: str):
        super().__init__(id_sensor, "Humedad", ubicacion)

    def leer(self):
        # valor simulado entre 20% y 90%
        self.valor = round(random.uniform(20.0, 90.0), 2)
        return self.valor


# ================================================================================
# ARCHIVO 7/8: sensor_temperatura.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/entidades/sensor_temperatura.py
# ================================================================================

import random
from entidades.sensor import Sensor

class SensorTemperatura(Sensor):
    def __init__(self, id_sensor: int, ubicacion: str):
        super().__init__(id_sensor, "Temperatura", ubicacion)

    def leer(self):
        # valor simulado entre -5°C y 40°C
        self.valor = round(random.uniform(-5.0, 40.0), 2)
        return self.valor


# ================================================================================
# ARCHIVO 8/8: usuario.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/entidades/usuario.py
# ================================================================================

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


