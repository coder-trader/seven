from dataclasses import dataclass
from datetime import datetime

import requests


@dataclass
class MarketData:
    symbol: str
    base_url: str = "https://www.deribit.com/api/v2/public/"

    def get_candles(self):
        window_min = 60
        end_timestamp = int(datetime.now().timestamp() * 1000)
        start_timestamp = end_timestamp - window_min * 60 * 1000
        response = requests.get(
            self.base_url + "get_tradingview_chart_data",
            params={
                "instrument_name": self.symbol,
                "resolution": "1",
                "start_timestamp": start_timestamp,
                "end_timestamp": end_timestamp,
            },
        )
        return response.json()["result"]

    def close_history(self):
        return self.get_candles()["close"]


if __name__ == "__main__":
    market_data = MarketData(symbol="BTC-PERPETUAL")
    # candles = market_data.get_candles()
    # print(candles)
    close_history = market_data.close_history()
    print(close_history)
