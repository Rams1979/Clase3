from gimnasio_app.controllers import RoutineController
from gimnasio_app.models import Weekday


def test_monday_has_eleven_exercises_in_order():
    controller = RoutineController()

    routine = controller.get_routine(Weekday.MONDAY)

    assert len(routine.exercises) == 11
    assert routine.exercises[0].name == "Calentamiento en caminadora/bicicleta"
    assert routine.exercises[-1].name == "Cardio suave"


def test_monday_first_strength_exercise_sets_and_reps():
    controller = RoutineController()

    routine = controller.get_routine(Weekday.MONDAY)
    sentadilla = routine.exercises[1]

    assert sentadilla.name == "Sentadilla o prensa de piernas"
    assert sentadilla.sets == 3
    assert sentadilla.reps == "10-12"


def test_days_without_spec_yet_still_empty():
    controller = RoutineController()

    for day in (Weekday.THURSDAY, Weekday.FRIDAY):
        assert controller.get_routine(day).exercises == []
