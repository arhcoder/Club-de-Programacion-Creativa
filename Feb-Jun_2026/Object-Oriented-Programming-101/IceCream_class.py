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
# | WhatIs.......: IceCream - Class
# +----------------------------------------------------------------------------++

# -------------------------- Imports --------------------------
from product_class import Product

# ------------------------- Class -------------------------
class IceCream(Product):
    def __init__(self, flavor, price, scoops):
        Product.__init__(self, flavor, price)
        self.flavor = flavor # string
        self.price = price # float
        self.scoops = scoops  # int

    def serve(self, toppings=False):
        total = self.price
        print(f"This is your {self.scoops} scoop {self.flavor} ice cream.")

        if toppings:
            total += 10
            print("It includes toppings.")

        print(f"That will be ${total}, please\n")