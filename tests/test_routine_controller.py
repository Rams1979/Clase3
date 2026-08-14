from gimnasio_app.controllers import RoutineController
from gimnasio_app.models import Exercise, Weekday


def test_week_has_only_five_weekdays():
    controller = RoutineController()
    week = controller.get_week()
    assert [routine.day for routine in week] == list(Weekday)
    assert len(week) == 5


def test_new_day_starts_without_exercises():
    controller = RoutineController()
    assert controller.get_routine(Weekday.MONDAY).exercises == []


def test_add_exercise_to_a_day():
    controller = RoutineController()
    controller.add_exercise(Weekday.MONDAY, Exercise(name="Sentadillas", sets=4, reps="10"))

    routine = controller.get_routine(Weekday.MONDAY)

    assert len(routine.exercises) == 1
    assert routine.exercises[0].name == "Sentadillas"
