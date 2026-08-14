from enum import Enum


class Weekday(Enum):
    """Días soportados por la app: solo de lunes a viernes."""

    MONDAY = "lunes"
    TUESDAY = "martes"
    WEDNESDAY = "miercoles"
    THURSDAY = "jueves"
    FRIDAY = "viernes"
