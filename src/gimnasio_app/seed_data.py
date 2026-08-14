from gimnasio_app.models import Exercise, Weekday

WEEKLY_ROUTINES: dict[Weekday, list[Exercise]] = {
    Weekday.MONDAY: [
        Exercise(name="Calentamiento en caminadora/bicicleta", sets=1, reps="8-10 min"),
        Exercise(name="Sentadilla o prensa de piernas", sets=3, reps="10-12"),
        Exercise(name="Press de pecho en maquina o banca", sets=3, reps="8-12"),
        Exercise(name="Jalon al pecho", sets=3, reps="10-12"),
        Exercise(name="Peso muerto rumano", sets=3, reps="10-12"),
        Exercise(name="Press de hombros", sets=3, reps="10-12"),
        Exercise(name="Remo sentado", sets=3, reps="10-12"),
        Exercise(name="Curl de biceps", sets=2, reps="10-15"),
        Exercise(name="Extension de triceps", sets=2, reps="10-15"),
        Exercise(name="Abdominales", sets=3, reps="12-20"),
        Exercise(name="Cardio suave", sets=1, reps="10-15 min"),
    ],
    Weekday.TUESDAY: [],
    Weekday.WEDNESDAY: [],
    Weekday.THURSDAY: [],
    Weekday.FRIDAY: [],
}
