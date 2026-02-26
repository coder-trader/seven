from dataclasses import dataclass

import requests


@dataclass
class DeribitAuth:
    client_id: str
    client_secret: str

    def get_auth_headers(self):
        return {"Authorization": f"Basic {self.client_id}:{self.client_secret}"}

    def get_token(self):
        url = "https://www.deribit.com/api/v2/public/auth"

        payload = {
            "jsonrpc": "2.0",
            "id": 9929,
            "method": "public/auth",
            "params": {
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            },
        }
        headers = {"Content-Type": "application/json"}

        response = requests.post(url, json=payload, headers=headers)

        return response.json()["result"]["access_token"]


if __name__ == "__main__":
    import os

    from dotenv import load_dotenv

    load_dotenv()

    client_id = os.getenv("KEY")
    client_secret = os.getenv("SECRET")
    if not client_id or not client_secret:
        raise ValueError("Client ID and Secret must be set in environment variables.")
    auth = DeribitAuth(client_id=client_id, client_secret=client_secret)
    token_response = auth.get_token()
