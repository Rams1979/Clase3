# Especificación 008: Fondo Oscuro

**Estado:** Completado
**Rama:** `008-fondo-oscuro`
**Depende de:** [007-interfaz-web](007-interfaz-web.md)

## Resumen

La interfaz web de la aplicación debe usar un tema de fondo oscuro.

## Requisitos funcionales

- FR1: La página web (`/`) DEBE mostrarse con fondo oscuro y texto claro por
  defecto (no depende de la preferencia del sistema operativo del usuario).
- FR2: Las tarjetas de cada día y las tablas de ejercicios DEBEN mantener
  buen contraste y ser legibles sobre el fondo oscuro.
- FR3: El estado "sin rutina cargada todavía" DEBE seguir siendo
  distinguible visualmente (texto atenuado) sobre el fondo oscuro.

## Requisitos no funcionales

- NFR1: El cambio se implementa únicamente en la Vista web
  (`views/static/style.css`), sin tocar modelos ni controladores.
- NFR2: La vista CLI (`gimnasio-app`) no se ve afectada — no tiene concepto
  de "tema".

## Fuera de alcance

- Selector de tema claro/oscuro (toggle) — por ahora el fondo oscuro es fijo.
- Modo claro alternativo.

## Cómo probarla

```
uv run gimnasio-app-web
```

Abrir `http://localhost:5000/` y verificar que el fondo es oscuro.
