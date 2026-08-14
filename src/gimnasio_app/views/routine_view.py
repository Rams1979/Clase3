from gimnasio_app.models import Routine


class RoutineView:
    """Presenta rutinas en consola."""

    def render_routine(self, routine: Routine) -> str:
        header = f"{routine.day.value.capitalize()}:"
        if not routine.exercises:
            return f"{header} (sin rutina cargada todavia)"
        lines = [header]
        for exercise in routine.exercises:
            lines.append(f"  - {exercise.name}: {exercise.sets}x{exercise.reps}")
        return "\n".join(lines)

    def render_week(self, routines: list[Routine]) -> str:
        return "\n".join(self.render_routine(routine) for routine in routines)
