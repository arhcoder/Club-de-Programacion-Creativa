# +----------------------------------------------------------------------------+
# | CARDUI TECH v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2026 - 2026, CARDUITECH.COM (www.carduitech.com)
# | Gaddiel Pedroza <pedrozagaddiel57@gmail.com>
# | Released under the MIT license
# | www.carduitech.com/license/
# +----------------------------------------------------------------------------+
# | Author.......: Gaddiel Pedroza <pedrozagaddiel57@gmail.com>
# | First release: March 4th, 2026
# | Last update..: March 4th, 2026
# | WhatIs.......: Invitations Maker - Main
# +----------------------------------------------------------------------------++

# --------------------------- Code ----------------------------
invitation = """Hola bro, usted ha sido sido cordialmente invitad@ a la boda de ENA y Coral!
Espero que puedas venir :D
El código de vestimenta es formal rojo y blanco.
Sera el dia 32 de febrero en el parque Heroes.
No faltes!!!!!!!!!!
Atte.
Ariadna, la organizadora del evento"""

try:
 with open("CRUD Invitations/1_guests.txt") as guestList:
    contents = guestList.read()
    guests = contents.split("\n")
    for guest in guests:
        s = invitation.replace("bro", guest)
        with open(f"CRUD Invitations/{guest}.txt", mode="x") as file:
            file.write(s)

except FileNotFoundError:
 print("You misspelt the file's name or is in another location")
