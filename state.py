from dataclasses import dataclass

from account_data import AccountData
from market_data import MarketData
from order_manager import OrderManager
from position_keeper import PositionKeeper


@dataclass
class State:
    position_keeper: PositionKeeper
    order_manager: OrderManager
    history: list
    price: float
    account_data = AccountData()
    MarketData = MarketData(symbol="BTC-PERPETUAL")

    def update(self):
        self.update_position()
        self.update_price()

    def update_position(self):
        postions = self.account_data.get_positions()
        self.position_keeper.entry = postions["entry"]
        self.position_keeper.quantity = postions["quantity"]

    def update_price(self):
        self.history = self.MarketData.close_history()
        self.price = self.history[-1]
