# Especificación 006: Rutina del Viernes

**Estado:** Completado
**Rama:** `001-gimnasio-app`
**Depende de:** [001-gimnasio-app](001-gimnasio-app.md)

## Resumen

Carga de la rutina de ejercicios correspondiente al día **viernes** (espalda
y bíceps), sobre el esqueleto MVC definido en la especificación 001. Con
esta especificación queda completa la semana lunes-viernes.

## Contenido de la rutina

| Ejercicio                     | Series | Repeticiones |
|---------------------------------|:------:|:-------------:|
| Jalón al pecho                  | 4      | 8-12          |
| Remo sentado en polea           | 3      | 10-12         |
| Remo con mancuerna              | 3      | 10-12         |
| Jalón con agarre cerrado        | 3      | 10-12         |
| Face pulls                      | 3      | 12-15         |
| Curl de bíceps con barra        | 3      | 10-12         |
| Curl martillo                   | 3      | 10-15         |

## Requisitos funcionales

- FR1: El sistema DEBE devolver los 7 ejercicios anteriores, en el orden
  indicado, al consultar la rutina del viernes.
- FR2: Con esta especificación, los cinco días (lunes a viernes) DEBEN tener
  rutina cargada.

## Diseño

Se agrega la rutina de viernes a `WEEKLY_ROUTINES` en
`src/gimnasio_app/seed_data.py`, siguiendo el mismo mecanismo establecido en
la especificación 002.

## Fuera de alcance

- Ninguna: última rutina de la semana definida en la especificación 001.
