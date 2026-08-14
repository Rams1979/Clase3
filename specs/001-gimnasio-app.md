# Especificación 001: Aplicación de Gimnasio — Rutinas Semanales (Lunes a Viernes)

**Estado:** Completado
**Rama:** `001-gimnasio-app`

## Resumen

Aplicación para registrar y consultar rutinas de gimnasio organizadas por día de
la semana. El usuario irá cargando la rutina de cada día (lunes, martes,
miércoles, jueves, viernes) de forma incremental, en especificaciones
posteriores. Esta primera especificación define únicamente el esqueleto de la
aplicación (arquitectura y estructura), sin contenido de rutinas todavía.

## Contexto / Motivación

El usuario quiere adoptar Spec-Driven Development: cada nueva funcionalidad
(por ejemplo, "la rutina del lunes") se documenta primero como especificación
en `specs/` antes de implementarse.

## Requisitos funcionales

- FR1: El sistema DEBE soportar exactamente 5 días: lunes, martes, miércoles,
  jueves, viernes.
- FR2: El sistema NO DEBE permitir registrar ni consultar rutinas para sábado
  o domingo (rechazar con un error claro si se intenta).
- FR3: El sistema DEBE permitir asociar una rutina (lista de ejercicios) a
  cada día de la semana de forma independiente.
- FR4: El sistema DEBE permitir consultar la rutina de un día específico.
- FR5: El sistema DEBE permitir listar todos los días con su rutina actual
  (vacía si aún no fue cargada).
- FR6: Cada ejercicio de una rutina DEBE tener al menos: nombre, series y
  repeticiones (u otra unidad de medida, ej. tiempo).

## Requisitos no funcionales

- NFR1: El código DEBE seguir el patrón de arquitectura MVC (Modelo-Vista-
  Controlador).
- NFR2: La gestión de dependencias y del entorno Python DEBE hacerse con
  `uv`.
- NFR3: El proyecto DEBE quedar preparado para agregar pruebas automatizadas
  más adelante (estructura compatible con `pytest`).

## Fuera de alcance (por ahora)

- Contenido real de las rutinas de cada día (se hará en specs posteriores,
  una por día).
- Persistencia en base de datos o archivo (se define cuando haga falta).
- Interfaz web o gráfica (se arranca con interfaz de línea de comandos).
- Autenticación / multiusuario.

## Arquitectura

Patrón **MVC**:

- **Modelo** (`src/gimnasio_app/models/`): entidades del dominio —
  `Weekday` (enum restringido a lunes–viernes), `Exercise`, `Routine`.
- **Vista** (`src/gimnasio_app/views/`): presentación de datos al usuario
  (por ahora, salida de consola).
- **Controlador** (`src/gimnasio_app/controllers/`): orquesta las
  operaciones (agregar rutina a un día, consultar rutina, listar semana),
  validando las reglas de negocio (ej. FR2).

Gestión de librerías y entorno con **uv** (`pyproject.toml` + `uv.lock`).

## Estructura de carpetas

```
specs/
  001-gimnasio-app.md
src/gimnasio_app/
  __init__.py
  models/
    weekday.py
    exercise.py
    routine.py
  views/
    routine_view.py
  controllers/
    routine_controller.py
pyproject.toml
```

## Supuestos

- Interfaz inicial de consola (CLI); se puede migrar a web más adelante si
  se pide.
- Almacenamiento en memoria por ahora (se define persistencia cuando el
  usuario lo indique).

## Próximos pasos

- Especificaciones 002–006: rutina de lunes, martes, miércoles, jueves y
  viernes respectivamente.
