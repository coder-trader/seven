import os

import requests
from dotenv import load_dotenv

from deribit_auth import DeribitAuth


class AccountData:
    def __init__(self):
        self.key = ""
        self.secret = ""
        load_dotenv()
        self.get_load_api_key()
        self.base_url = "https://www.deribit.com/api/v2/private/"
        self.derbit_auth = DeribitAuth(client_id=self.key, client_secret=self.secret)

    def get_load_api_key(self):
        self.key = os.getenv("KEY")
        self.secret = os.getenv("SECRET")

    def get_positions(self):
        res = {"entry": 0.0, "quantity": 0}
        access_token = self.derbit_auth.get_token()
        response = requests.get(
            self.base_url + "get_positions",
            headers={"Authorization": f"Bearer {access_token}"},
            params={"currency": "BTC"},
        )
        result = response.json()["result"]
        if len(result) == 0:
            return res

        position = result[0]
        res["entry"] = position["average_price"]
        res["quantity"] = position["size"]
        return res


if __name__ == "__main__":
    account_data = AccountData()
    positions = account_data.get_positions()
    print(positions)
