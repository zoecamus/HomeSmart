"""
Archivo integrador generado automaticamente
Directorio: /home/zoe/Diseño de sistemas /HomeSmart/HS
Fecha: 2025-11-05 09:42:55
Total de archivos integrados: 1
"""

# ================================================================================
# ARCHIVO 1/1: main.py
# Ruta: /home/zoe/Diseño de sistemas /HomeSmart/HS/main.py
# ================================================================================

import time
import random
from datetime import datetime

# === IMPORTS DE ENTIDADES ===
from HS.entidades.usuario import Usuario
from HS.entidades.luz import Luz
from HS.entidades.camara import Camara
from HS.entidades.sensor_humedad import SensorHumedad
from HS.entidades.sensor_temperatura import SensorTemperatura

# === IMPORTS DE SERVICIOS ===
from HS.servicios.dispositivos_service import DispositivoService
from HS.servicios.sensor_service import SensorService
from HS.servicios.usuario_service import UsuarioService
from HS.servicios.automatizacion_service import AutomatizacionService, ReglaAutomatica
from HS.servicios.registro_domotico_service import RegistroDomoticoService

# === IMPORTS DE EXCEPCIONES ===
from HS.excepciones.domotica_excepcion import DomoticaException


# === CONFIGURACIÓN DE DISPOSITIVOS ===
CONFIG_DISPOSITIVOS = {
    "luces": 3,
    "camaras": 2,
    "sensores_temperatura": 1,
    "sensores_humedad": 1
}

# ======================================================================
#                 SISTEMA DOMÓTICO INTELIGENTE - HOMESMART
# ======================================================================

print("=" * 70)
print("      SISTEMA DOMÓTICO INTELIGENTE - HOMESMART (Proyecto Final)")
print("=" * 70)

try:
    # ------------------------------------------------------------------
    # INICIALIZACIÓN DE USUARIO Y SERVICIOS
    # ------------------------------------------------------------------
    usuario = Usuario("Zoe Camus")

    disp_service = DispositivoService()
    sensor_service = SensorService()
    user_service = UsuarioService()
    auto_service = AutomatizacionService()
    registro_service = RegistroDomoticoService()

    print("\n[INICIO] Servicios inicializados correctamente.")
    print(f"[USUARIO] Bienvenida, {usuario.nombre}.\n")

    # ------------------------------------------------------------------
    # CREACIÓN DE DISPOSITIVOS DESDE CONFIGURACIÓN
    # ------------------------------------------------------------------
    print("Creando dispositivos inteligentes...\n")

    luces = [Luz(i + 1, f"Ambiente {i + 1}") for i in range(CONFIG_DISPOSITIVOS["luces"])]
    camaras = [Camara(i + 1, f"Sector {i + 1}") for i in range(CONFIG_DISPOSITIVOS["camaras"])]
    sensores_temp = [SensorTemperatura(1, "Sala Principal")]
    sensores_hum = [SensorHumedad(2, "Cocina")]

    for d in luces + camaras + sensores_temp + sensores_hum:
        user_service.registrar_dispositivo(usuario, d)

    usuario.listar_dispositivos()

    # ------------------------------------------------------------------
    # DEMOSTRACIÓN DE LECTURA DE SENSORES
    # ------------------------------------------------------------------
    print("\n--- Lectura de Sensores ---")
    temp = sensor_service.leer_sensor(sensores_temp[0])
    hum = sensor_service.leer_sensor(sensores_hum[0])

    if sensor_service.es_temperatura_peligrosa(temp):
        print(f"[ALERTA] Temperatura fuera de rango: {temp}°C")
    else:
        print(f"[OK] Temperatura normal: {temp}°C")

    if sensor_service.es_humedad_baja(hum):
        print(f"[ALERTA] Humedad baja: {hum}%")
    else:
        print(f"[OK] Humedad estable: {hum}%")

    # ------------------------------------------------------------------
    # DEMOSTRACIÓN DE AUTOMATIZACIONES (PATRÓN OBSERVER)
    # ------------------------------------------------------------------
    print("\n--- Reglas Automáticas ---")
    aire = Luz(99, "Aire Acondicionado", intensidad=100)

    regla_temp = ReglaAutomatica(
        "Encender Aire por Calor",
        condicion=lambda: sensores_temp[0].leer() > 28,
        accion=lambda: disp_service.encender(aire)
    )

    regla_hum = ReglaAutomatica(
        "Apagar Aire por Humedad Alta",
        condicion=lambda: sensores_hum[0].leer() > 70,
        accion=lambda: disp_service.apagar(aire)
    )

    auto_service.registrar_regla(regla_temp)
    auto_service.registrar_regla(regla_hum)

    print("[SIMULACIÓN] Evaluando reglas automáticas (5 ciclos)...")
    for _ in range(5):
        auto_service.evaluar_todas()
        time.sleep(0.8)

    # ------------------------------------------------------------------
    # GUARDAR ESTADO DEL SISTEMA
    # ------------------------------------------------------------------
    print("\n--- Guardando estado del sistema ---")
    estado_casa = {
        "usuario": usuario.nombre,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "dispositivos": [str(d) for d in usuario.dispositivos] + [str(aire)]
    }

    registro_service.persistir(usuario.nombre, estado_casa)
    print("[OK] Estado del hogar guardado exitosamente.")

    # ------------------------------------------------------------------
    # MOSTRAR RESUMEN FINAL
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("                   EJEMPLO COMPLETADO EXITOSAMENTE")
    print("=" * 70)
    print(" [OK] SINGLETON   - Gestor único de dispositivos")
    print(" [OK] FACTORY     - Creación de sensores y luces")
    print(" [OK] OBSERVER    - Reglas automáticas ejecutadas")
    print(" [OK] STRATEGY    - Evaluación de condiciones ambientales")
    print(" [OK] PERSISTENCIA - Estado del sistema guardado correctamente")
    print("=" * 70)

except DomoticaException as e:
    print(f"[ERROR DOMÓTICO] {e}")

except Exception as ex:
    print(f"[ERROR CRÍTICO] {ex}")

finally:
    print("\n[FIN DEL PROGRAMA] Ejecución finalizada.")


