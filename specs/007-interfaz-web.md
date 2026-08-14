# Especificación 007: Interfaz Web

**Estado:** Completado
**Rama:** `001-gimnasio-app`
**Depende de:** [001-gimnasio-app](001-gimnasio-app.md), specs 002-006

## Resumen

Agregar una interfaz web como alternativa a la interfaz de consola (CLI)
existente, para visualizar la semana de rutinas (lunes a viernes) en el
navegador.

## Requisitos funcionales

- FR1: El sistema DEBE exponer una página web que muestre los 5 días
  (lunes a viernes) con su rutina completa (ejercicio, series,
  repeticiones).
- FR2: Un día sin rutina cargada DEBE mostrarse indicando que no tiene
  rutina, igual que en la vista CLI.
- FR3: La interfaz web NO DEBE reimplementar reglas de negocio: DEBE
  reutilizar `RoutineController` tal cual, sin duplicar lógica.

## Requisitos no funcionales

- NFR1: Se mantiene el patrón MVC: la web es una **Vista** nueva
  (`views/web_view.py` + plantillas), no reemplaza ni modifica el
  controlador ni los modelos existentes.
- NFR2: La dependencia web se gestiona con `uv` (`uv add`).
- NFR3: La vista CLI (`gimnasio-app`) DEBE seguir funcionando sin cambios.

## Diseño

- Framework: **Flask** (liviano, agregado vía `uv add flask`).
- `src/gimnasio_app/views/web_view.py`: crea la app Flask
  (`create_app()`), define la ruta `/` que llama a
  `RoutineController().get_week()` y renderiza una plantilla Jinja2.
- Plantilla `templates/week.html` dentro de `views/templates/`: recorre los
  días y ejercicios recibidos (sin lógica de negocio en la plantilla).
- Nuevo script de entrada `gimnasio-app-web` en `pyproject.toml`, que
  levanta el servidor de desarrollo Flask.

## Fuera de alcance

- Edición de rutinas desde la web (por ahora es solo lectura).
- Autenticación, despliegue en producción, HTTPS.
- Diseño visual avanzado (se usa un CSS mínimo).

## Cómo probarla

```
uv run gimnasio-app-web
```

Luego abrir `http://localhost:5000/` en el navegador.
