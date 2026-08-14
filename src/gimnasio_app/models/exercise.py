from dataclasses import dataclass


@dataclass(frozen=True)
class Exercise:
    name: str
    sets: int
    reps: str
