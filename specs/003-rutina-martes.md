# Especificación 003: Rutina del Martes

**Estado:** Completado
**Rama:** `001-gimnasio-app`
**Depende de:** [001-gimnasio-app](001-gimnasio-app.md)

## Resumen

Carga de la rutina de ejercicios correspondiente al día **martes** (espalda
y bíceps), sobre el esqueleto MVC definido en la especificación 001.

## Contenido de la rutina

| Ejercicio                     | Series | Repeticiones |
|--------------------------------|:------:|:-------------:|
| Jalón al pecho                 | 4      | 8-12          |
| Remo sentado en polea          | 3      | 10-12         |
| Remo con mancuerna             | 3      | 10-12         |
| Pullover en polea              | 3      | 12-15         |
| Curl de bíceps con barra       | 3      | 8-12          |
| Curl martillo                  | 3      | 10-15         |

## Requisitos funcionales

- FR1: El sistema DEBE devolver los 6 ejercicios anteriores, en el orden
  indicado, al consultar la rutina del martes.
- FR2: El resto de los días sin especificación propia (miércoles a viernes)
  DEBEN permanecer sin rutina cargada.

## Diseño

Se agrega la rutina de martes a `WEEKLY_ROUTINES` en
`src/gimnasio_app/seed_data.py`, siguiendo el mismo mecanismo establecido en
la especificación 002.

## Fuera de alcance

- Rutinas de miércoles a viernes (specs 004-006).
