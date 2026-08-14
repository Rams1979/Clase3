from gimnasio_app.controllers import RoutineController
from gimnasio_app.models import Weekday


def test_friday_has_seven_exercises_in_order():
    controller = RoutineController()

    routine = controller.get_routine(Weekday.FRIDAY)

    assert len(routine.exercises) == 7
    assert routine.exercises[0].name == "Jalon al pecho"
    assert routine.exercises[-1].name == "Curl martillo"


def test_friday_first_exercise_sets_and_reps():
    controller = RoutineController()

    jalon = controller.get_routine(Weekday.FRIDAY).exercises[0]

    assert jalon.sets == 4
    assert jalon.reps == "8-12"
