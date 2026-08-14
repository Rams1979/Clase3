from gimnasio_app.models import Exercise, Routine, Weekday
from gimnasio_app.seed_data import WEEKLY_ROUTINES


class RoutineController:
    """Orquesta las operaciones sobre las rutinas de lunes a viernes."""

    def __init__(self, seed: dict[Weekday, list[Exercise]] | None = None) -> None:
        seed = WEEKLY_ROUTINES if seed is None else seed
        self._routines: dict[Weekday, Routine] = {
            day: Routine(day=day, exercises=list(seed.get(day, [])))
            for day in Weekday
        }

    def add_exercise(self, day: Weekday, exercise: Exercise) -> None:
        self._routines[day].exercises.append(exercise)

    def get_routine(self, day: Weekday) -> Routine:
        return self._routines[day]

    def get_week(self) -> list[Routine]:
        return [self._routines[day] for day in Weekday]
