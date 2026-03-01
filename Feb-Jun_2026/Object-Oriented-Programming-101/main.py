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
# | WhatIs.......: Object Oriented Programming 101 - Main
# +----------------------------------------------------------------------------++

# -------------------------- Imports --------------------------
from IceCream_class import IceCream
from IcePop_class import IcePop

# -------------------------- Objects --------------------------
PerryThePistachio = IceCream('Pistachio', 45.00,2)
MangoTango = IceCream('Mango', 37.00, 2,)
MarvelousMint = IceCream('Mint chocolate chip', 25.00,1)

PoppyBerryMix = IcePop('BerryMix', 32.00)
VanillaPop = IcePop('Vanilla', 21.00)

# ------------------------- Variables -------------------------
menu = {
    'Ice Cream': [PerryThePistachio, MangoTango, MarvelousMint],
    'Ice Pops': [PoppyBerryMix, VanillaPop]
}

# --------------------------- Code ----------------------------
PerryThePistachio.serve(toppings=True)
PoppyBerryMix.serve(chocolate_coat=True)
MarvelousMint.serve(toppings=False)
