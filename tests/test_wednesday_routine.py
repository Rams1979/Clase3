from gimnasio_app.controllers import RoutineController
from gimnasio_app.models import Weekday


def test_wednesday_has_seven_exercises_in_order():
    controller = RoutineController()

    routine = controller.get_routine(Weekday.WEDNESDAY)

    assert len(routine.exercises) == 7
    assert routine.exercises[0].name == "Prensa de piernas"
    assert routine.exercises[-1].name == "Abdominales"


def test_wednesday_first_exercise_sets_and_reps():
    controller = RoutineController()

    prensa = controller.get_routine(Weekday.WEDNESDAY).exercises[0]

    assert prensa.sets == 4
    assert prensa.reps == "10-12"
