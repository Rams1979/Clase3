# Especificación 002: Rutina del Lunes

**Estado:** Completado
**Rama:** `001-gimnasio-app`
**Depende de:** [001-gimnasio-app](001-gimnasio-app.md)

## Resumen

Carga de la rutina de ejercicios correspondiente al día **lunes**, sobre el
esqueleto MVC definido en la especificación 001.

## Contenido de la rutina

| Ejercicio                                  | Series | Repeticiones |
|---------------------------------------------|:------:|:-------------:|
| Calentamiento en caminadora/bicicleta        | 1      | 8-10 min      |
| Sentadilla o prensa de piernas               | 3      | 10-12         |
| Press de pecho en máquina o banca            | 3      | 8-12          |
| Jalón al pecho                               | 3      | 10-12         |
| Peso muerto rumano                           | 3      | 10-12         |
| Press de hombros                             | 3      | 10-12         |
| Remo sentado                                 | 3      | 10-12         |
| Curl de bíceps                               | 2      | 10-15         |
| Extensión de tríceps                         | 2      | 10-15         |
| Abdominales                                  | 3      | 12-20         |
| Cardio suave                                 | 1      | 10-15 min     |

## Requisitos funcionales

- FR1: El sistema DEBE devolver los 11 ejercicios anteriores, en el orden
  indicado, al consultar la rutina del lunes.
- FR2: El resto de los días (martes a viernes) DEBEN permanecer sin rutina
  cargada hasta que existan sus especificaciones correspondientes.

## Diseño

Se agrega una fuente de datos semilla (`src/gimnasio_app/seed_data.py`) con
la rutina de cada día ya definida. `RoutineController` se inicializa a partir
de esa semilla en lugar de arrancar siempre vacío, manteniendo la separación
MVC: la semilla es dato, no lógica de negocio ni presentación.

## Fuera de alcance

- Rutinas de martes a viernes (specs 003-006).
- Edición/carga dinámica de rutinas por el usuario final (hoy son datos fijos
  en el código).
