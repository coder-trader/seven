from dataclasses import dataclass


@dataclass
class Order:
    price: float
    quantity: int
    side: str  # "buy" or "sell"
    type: str  # "market" or "limit"
    symbol: str
