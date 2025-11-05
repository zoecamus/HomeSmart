🏠 HomeSmart – Sistema Domótico Inteligente

Proyecto Final – Diseño de Sistemas 2025

## Descripción General

HomeSmart es una aplicación de domótica inteligente que permite administrar y automatizar los dispositivos de un hogar: luces, cámaras y sensores de temperatura y humedad.
El sistema integra los principales patrones de diseño (Singleton, Factory, Observer y Strategy) para demostrar una arquitectura modular, mantenible y extensible, similar a la del proyecto Forestal pero aplicada al dominio del hogar inteligente.

## Arquitectura General

El sistema sigue una arquitectura en capas:
HomeSmart/
├── entidades/                 # Modelos del dominio
│   ├── dispositivo.py
│   ├── luz.py
│   ├── camara.py
│   ├── sensor.py
│   ├── sensor_temperatura.py
│   ├── sensor_humedad.py
│   └── usuario.py
│
├── servicios/                 # Lógica de negocio
│   ├── automatizacion_service.py
│   ├── registro_domotico_service.py
│   ├── luz_service.py
│   ├── camara_service.py
│   └── sensor_service.py
│
├── patrones/                  # Implementación de patrones
│   ├── singleton.py
│   ├── factory.py
│   ├── observer.py
│   └── strategy.py
│
├── excepciones/               # Excepciones personalizadas
│   ├── domotica_excepcion.py
│   ├── homesmart_excepcion.py
│   ├── sensor_error_excepcion.py
│   └── dispositivo_inaccesible_Excepcion.py   
│   └── modo_no_disponible_excepcion.py
│
├── data/                      # Estado persistido del sistema
│   └── Zoe Camus.dat
│
└── main.py                    # Simulación principal


## Patrones de Diseño Implementados
1. Singleton

    Clase: GestorDispositivos

    Función: Centraliza todos los dispositivos y garantiza una única instancia global.

    Ejemplo en salida:
    [INICIO] Servicios inicializados correctamente.
    [OK] Todos los servicios comparten la misma instancia del Registry

2. Factory Method

    Clase: FactoryDispositivos

    Función: Crea los objetos de tipo Luz, Cámara y Sensor sin exponer la lógica interna de instanciación.

    Ejemplo:
    [USUARIO] Zoe Camus agregó dispositivo: Luz (Ubicación: Ambiente 1)
    [USUARIO] Zoe Camus agregó dispositivo: Cámara (Ubicación: Sector 2)


3. Observer

    Clase: AutomatizacionService y ReglaAutomatica

    Función: Implementa reglas automáticas que se ejecutan al cumplirse condiciones monitoreadas por sensores.

    Ejemplo:
    [AUTOMATIZACIÓN] Regla 'Encender Aire por Calor' disparada.
    [AUTOMATIZACIÓN] Regla 'Apagar Aire por Humedad Alta' disparada.


4. Strategy

    Clase: SensorTemperatura, SensorHumedad

    Función: Cada sensor aplica una estrategia de lectura y validación diferente.

    Ejemplo:
    [SENSOR] Sensor(Temperatura, Sala Principal) → valor leído: 24.59
    [ALERTA] Humedad baja: 34.07%

5. Persistencia

    Clase: RegistroDomoticoService

    Función: Guarda el estado del sistema (dispositivos, sensores y automatizaciones) en un archivo .dat.

    Ejemplo:
    [PERSISTENCIA] Estado domótico guardado en data/Zoe Camus.dat
    [OK] Estado del hogar guardado exitosamente.


##  Principios de Diseño Aplicados (SOLID)
Principio	Aplicación
S – Responsabilidad Única	Cada entidad (Luz, Cámara, Sensor) se encarga de un único comportamiento.
O – Abierto/Cerrado	Se pueden agregar nuevos dispositivos sin modificar las clases existentes (Factory + Strategy).
L – Sustitución de Liskov	Las subclases de Sensor o Dispositivo pueden reemplazar a la base sin romper el código.
I – Segregación de Interfaces	Cada dispositivo implementa solo los métodos que necesita.
D – Inversión de Dependencia	Los servicios reciben dependencias, no las crean (inyectadas en main.py).

## Simulacion del Sistema (salida esperada)

======================================================================
      SISTEMA DOMÓTICO INTELIGENTE - HOMESMART (Proyecto Final)
======================================================================

[INICIO] Servicios inicializados correctamente.
[USUARIO] Bienvenida, Zoe Camus.

Creando dispositivos inteligentes...
[USUARIO] Zoe Camus agregó dispositivo: Luz (Ubicación: Ambiente 1, Intensidad: 100%, Estado: APAGADA)
[USUARIO] Zoe Camus agregó dispositivo: Cámara (Ubicación: Sector 1, Estado: EN ESPERA)
[USUARIO] Zoe Camus agregó dispositivo: Sensor(Temperatura, Sala Principal)
[USUARIO] Zoe Camus agregó dispositivo: Sensor(Humedad, Cocina)

--- Lectura de Sensores ---
[SENSOR] Sensor(Temperatura, Sala Principal) → valor leído: 24.59
[SENSOR] Sensor(Humedad, Cocina) → valor leído: 34.07
[OK] Temperatura normal: 24.59°C
[ALERTA] Humedad baja: 34.07%

--- Reglas Automáticas ---
[AUTOMATIZACIÓN] Regla registrada: Encender Aire por Calor
[AUTOMATIZACIÓN] Regla registrada: Apagar Aire por Humedad Alta
[SIMULACIÓN] Evaluando reglas automáticas (5 ciclos)...
[AUTOMATIZACIÓN] Regla 'Encender Aire por Calor' disparada.
[LUZ] Encendido en Aire Acondicionado
[AUTOMATIZACIÓN] Regla 'Apagar Aire por Humedad Alta' disparada.
[LUZ] Apagado en Aire Acondicionado

--- Guardando estado del sistema ---
[PERSISTENCIA] Estado domótico guardado en data/Zoe Camus.dat
[OK] Estado del hogar guardado exitosamente.

======================================================================
                   EJEMPLO COMPLETADO EXITOSAMENTE
======================================================================
 [OK] SINGLETON   - Gestor único de dispositivos
 [OK] FACTORY     - Creación de sensores y luces
 [OK] OBSERVER    - Reglas automáticas ejecutadas
 [OK] STRATEGY    - Evaluación de condiciones ambientales
 [OK] PERSISTENCIA - Estado del sistema guardado correctamente
======================================================================

## Cómo Ejecutar el Proyecto

Python 3.10 o superior

Ejecución = python3 main.py
