# +----------------------------------------------------------------------------+
# | CARDUI TECH v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2026 - 2026, CARDUITECH.COM (www.carduitech.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.carduitech.com/license/
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: February 27th, 2026
# | Last update..: February 28th, 2026
# | WhatIs.......: Product - Class
# +----------------------------------------------------------------------------++

# ------------------------- Class -------------------------
class Product:
    def __init__(self, flavor, price):
        self.flavor = flavor # string
        self.price = price # float

    def serve(self):
        total = self.price
        print(f"That will be ${total}, please\n")