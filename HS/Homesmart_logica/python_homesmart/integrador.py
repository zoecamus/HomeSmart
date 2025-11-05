"""
Archivo integrador generado automaticamente
Directorio: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/python_homesmart
Fecha: 2025-11-05 09:42:55
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/python_homesmart/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: constantes.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/Homesmart_logica/python_homesmart/constantes.py
# ================================================================================

# MODOS DE FUNCIONAMIENTO (Strategy)
MODO_ECOLOGICO = "Ecológico"
MODO_SEGURIDAD = "Seguridad Nocturna"
MODO_NORMAL = "Normal"

MODOS_DISPONIBLES = [MODO_ECOLOGICO, MODO_SEGURIDAD, MODO_NORMAL]

# CONFIGURACIÓN DE DISPOSITIVOS
CONFIG_DISPOSITIVOS = {
    "luz": {
        "consumo": 0.06,  # kWh por minuto
        "ubicaciones": ["Living", "Dormitorio", "Cocina"]
    },
    "camara": {
        "consumo": 0.12,
        "ubicaciones": ["Entrada", "Garaje"]
    },
}

# UMBRALES DE SENSORES
SENSOR_TEMPERATURA_UMBRAL = {
    "min": 18,  # °C
    "max": 26
}

SENSOR_HUMEDAD_UMBRAL = {
    "min": 30,  # %
    "max": 70
}

# ALERTAS DEL SISTEMA
ALERTA_MOVIMIENTO = "Movimiento detectado"
ALERTA_TEMPERATURA = "Temperatura fuera de rango"
ALERTA_HUMEDAD = "Humedad fuera de rango"

# DATOS DEL HOGAR (para simular en la salida)
HOGAR_INFO = {
    "propietario": "Zoe Camus",
    "ubicacion": "Mendoza, Argentina",
    "superficie": 120.0,  # m²
    "dispositivos": 5,
}


