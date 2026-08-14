from dataclasses import dataclass, field

from gimnasio_app.models.exercise import Exercise
from gimnasio_app.models.weekday import Weekday


@dataclass
class Routine:
    day: Weekday
    exercises: list[Exercise] = field(default_factory=list)
