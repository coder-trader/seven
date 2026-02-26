from dataclasses import dataclass


@dataclass
class PositionKeeper:
    entry: float = 0.0
    quantity: int = 0
