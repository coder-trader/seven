from order import Order
from trader import Trader


def test_trader(access_token):
    trdr = Trader(access_token)
    order = Order(
        symbol="BTC-PERPETUAL",
        quantity=10,
        price=0,
        side="buy",
        type="market",
    )
    trdr.send_market_order(order)
