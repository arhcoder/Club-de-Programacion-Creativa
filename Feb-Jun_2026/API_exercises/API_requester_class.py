# +----------------------------------------------------------------------------+
# | CARDUI TECH v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2026 - 2026, CARDUITECH.COM (www.carduitech.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.carduitech.com/license/
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: March 16th, 2026
# | Last update..: March 16th, 2026
# | WhatIs.......: API Requester - Class
# +----------------------------------------------------------------------------++

# ------------ Resources / Documentation involved -------------
# Requests library documentation: https://requests.readthedocs.io/en/latest/user/quickstart/
# URL Decoder/Encoder: https://meyerweb.com/eric/tools/dencoder/

# ------------------------- Libraries -------------------------
import requests

# ------------------------- Class -------------------------
class API_Requester:
    def __init__(self, endpoint, parameters, api_key=""):
        self.endpoint = endpoint
        self.parameters = parameters
        self.api_key = api_key

    def fetch_data(self, method="GET", show_url=False, show_status_code=False, show_json=False):
        response = requests.get(self.endpoint, params=self.parameters)

        if show_url:
            print(f"Sent URL: {response.url}")

        if show_status_code:
            print(f"Status code: {response.status_code}")

        if show_json:
            print("Response: ") # Separate prints for easier response copy/paste
            print(response.json())

        return response.json()