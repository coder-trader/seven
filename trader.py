from dataclasses import dataclass
from uuid import uuid4

import requests

from order import Order


@dataclass
class Trader:
    auth_token: str

    def send_market_order(self, order: Order):
        side = "buy" if order.side == "buy" else "sell"
        url = f"https://www.deribit.com/api/v2/private/{side}"
        id = str(uuid4())
        label = f"market-{id[:8]}"

        payload = {
            "jsonrpc": "2.0",
            "id": 5275,
            "method": f"private/{side}",
            "params": {
                "instrument_name": order.symbol,
                "amount": order.quantity,
                "type": "market",
                "label": label,
            },
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth_token}",
        }

        response = requests.post(url, json=payload, headers=headers)

        print(response.text)
