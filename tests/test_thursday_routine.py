from gimnasio_app.controllers import RoutineController
from gimnasio_app.models import Weekday


def test_thursday_has_eight_exercises_in_order():
    controller = RoutineController()

    routine = controller.get_routine(Weekday.THURSDAY)

    assert len(routine.exercises) == 8
    assert routine.exercises[0].name == "Press de hombros"
    assert routine.exercises[-1].name == "Triceps en polea"


def test_thursday_first_exercise_sets_and_reps():
    controller = RoutineController()

    press = controller.get_routine(Weekday.THURSDAY).exercises[0]

    assert press.sets == 4
    assert press.reps == "8-12"
