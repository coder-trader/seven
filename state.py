from dataclasses import dataclass

from order_manager import OrderManager
from position_keeper import PositionKeeper


@dataclass
class State:
    position_keeper: PositionKeeper
    order_manager: OrderManager
    history: list
    price: float
