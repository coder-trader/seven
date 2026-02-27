import requests


class AccountData:
    def __init__(self, access_token: str):
        self.base_url = "https://www.deribit.com/api/v2/private/"
        self.access_token = access_token

    def get_positions(self):
        res = {"entry": 0.0, "quantity": 0}
        # access_token = self.derbit_auth.get_token()
        response = requests.get(
            self.base_url + "get_positions",
            headers={"Authorization": f"Bearer {self.access_token}"},
            params={"currency": "BTC"},
        )
        result = response.json()["result"]
        if len(result) == 0:
            return res

        position = result[0]
        res["entry"] = position["average_price"]
        res["quantity"] = position["size"]
        return res
