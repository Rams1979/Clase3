# Especificación 005: Rutina del Jueves

**Estado:** Borrador
**Rama:** `001-gimnasio-app`
**Depende de:** [001-gimnasio-app](001-gimnasio-app.md)

## Resumen

Carga de la rutina de ejercicios correspondiente al día **jueves** (hombros
y brazos), sobre el esqueleto MVC definido en la especificación 001.

## Contenido de la rutina

| Ejercicio                        | Series | Repeticiones |
|------------------------------------|:------:|:-------------:|
| Press de hombros                    | 4      | 8-12          |
| Elevaciones laterales               | 4      | 12-15         |
| Elevaciones posteriores             | 3      | 12-15         |
| Encogimientos para trapecio         | 3      | 10-15         |
| Press de pecho en máquina           | 3      | 10-12         |
| Jalón al pecho                      | 3      | 10-12         |
| Curl de bíceps                      | 2      | 12-15         |
| Tríceps en polea                    | 2      | 12-15         |

## Requisitos funcionales

- FR1: El sistema DEBE devolver los 8 ejercicios anteriores, en el orden
  indicado, al consultar la rutina del jueves.
- FR2: Viernes, aún sin especificación propia, DEBE permanecer sin rutina
  cargada.

## Diseño

Se agrega la rutina de jueves a `WEEKLY_ROUTINES` en
`src/gimnasio_app/seed_data.py`, siguiendo el mismo mecanismo establecido en
la especificación 002.

## Fuera de alcance

- Rutina de viernes (spec 006).
