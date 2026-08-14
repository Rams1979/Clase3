# Especificación 004: Rutina del Miércoles

**Estado:** Completado
**Rama:** `001-gimnasio-app`
**Depende de:** [001-gimnasio-app](001-gimnasio-app.md)

## Resumen

Carga de la rutina de ejercicios correspondiente al día **miércoles**
(piernas), sobre el esqueleto MVC definido en la especificación 001.

## Contenido de la rutina

| Ejercicio                  | Series | Repeticiones |
|------------------------------|:------:|:-------------:|
| Prensa de piernas             | 4      | 10-12         |
| Sentadilla                    | 3      | 8-12          |
| Peso muerto rumano             | 3      | 10-12         |
| Extensión de piernas          | 3      | 12-15         |
| Curl femoral                  | 3      | 12-15         |
| Elevación de pantorrillas     | 4      | 15-20         |
| Abdominales                   | 3      | 15-20         |

## Requisitos funcionales

- FR1: El sistema DEBE devolver los 7 ejercicios anteriores, en el orden
  indicado, al consultar la rutina del miércoles.
- FR2: El resto de los días sin especificación propia (jueves y viernes)
  DEBEN permanecer sin rutina cargada.

## Diseño

Se agrega la rutina de miércoles a `WEEKLY_ROUTINES` en
`src/gimnasio_app/seed_data.py`, siguiendo el mismo mecanismo establecido en
la especificación 002.

## Fuera de alcance

- Rutinas de jueves y viernes (specs 005-006).
