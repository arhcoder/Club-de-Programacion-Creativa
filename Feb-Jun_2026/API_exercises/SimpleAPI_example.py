# +----------------------------------------------------------------------------+
# | CARDUI TECH v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2026 - 2026, CARDUITECH.COM (www.carduitech.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.carduitech.com/license/
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: March 11th, 2026
# | Last update..: March 16th, 2026
# | WhatIs.......: Dog API (API connections exercise)  - Main
# +----------------------------------------------------------------------------++

# ------------ Resources / Documentation involved -------------
# Dog API Documentation: https://dogapi.dog/docs/api-v2
# Requests library documentation: https://requests.readthedocs.io/en/latest/user/quickstart/
# URL Decoder/Encoder: https://meyerweb.com/eric/tools/dencoder/

# ------------------------- Libraries -------------------------
import requests

# ------------------------- Variables -------------------------
DogAPI_endpoint = "https://dogapi.dog/api/v2/facts"

parameters = {
     "limit": "3"
}

# --------------------------- Code ----------------------------
response = requests.get(DogAPI_endpoint, params=parameters)

# Get sent URL
print(response.url)

# Get status code
print(response.status_code)

# Get headers
print(response.headers)

# Get response encoding
print(response.headers)
# print(response.headers['content-type'])

# Get response plain text
print(response.text)

# Get the actual data
print(response.json())
