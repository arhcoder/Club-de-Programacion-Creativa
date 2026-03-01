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
# | WhatIs.......: IcePop - Class
# +----------------------------------------------------------------------------++

# -------------------------- Imports --------------------------
from product_class import Product

# ------------------------- Class -------------------------
class IcePop(Product):
    def __init__(self, flavor, price):
        super().__init__(flavor, price)
        self.flavor = flavor # string
        self.price = price # float

    def serve(self, chocolate_coat=False):
        total = self.price
        print(f"This is your {self.flavor} ice pop.")

        if chocolate_coat:
            total += 10
            print("It includes a chocolate coat")

        print(f"That will be ${total}, please\n")