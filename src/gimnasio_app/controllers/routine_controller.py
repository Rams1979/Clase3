from gimnasio_app.models import Exercise, Routine, Weekday


class RoutineController:
    """Orquesta las operaciones sobre las rutinas de lunes a viernes."""

    def __init__(self) -> None:
        self._routines: dict[Weekday, Routine] = {
            day: Routine(day=day) for day in Weekday
        }

    def add_exercise(self, day: Weekday, exercise: Exercise) -> None:
        self._routines[day].exercises.append(exercise)

    def get_routine(self, day: Weekday) -> Routine:
        return self._routines[day]

    def get_week(self) -> list[Routine]:
        return [self._routines[day] for day in Weekday]
