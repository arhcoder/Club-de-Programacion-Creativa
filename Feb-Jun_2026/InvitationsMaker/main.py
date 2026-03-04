# +----------------------------------------------------------------------------+
# | CARDUI TECH v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2026 - 2026, CARDUITECH.COM (www.carduitech.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.carduitech.com/license/
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: July 26th, 2022
# | Last update..: March 4th, 2026
# | WhatIs.......: Invitations Maker - Main
# +----------------------------------------------------------------------------++

# --------------------------- Code ----------------------------
with open("Input/Names/invited_names.txt") as invites:
    invitesNames = invites.readlines()
    counter = 0
    for item in invitesNames:
        newItem = item.strip('\n')
        invitesNames[counter] = newItem
        counter += 1

counter = 0
for item in invitesNames:
    with open("Input/Letters/starting_letter.txt") as originalLetter:
        originalTemplate = originalLetter.read()
        inviteTemplate = originalTemplate.replace("[name]", f"{invitesNames[counter]}")

    with open(f"Output/ReadyToSend/letter_to_{invitesNames[counter]}.txt", mode="w") as newLetter:
        newLetter.write(f"{inviteTemplate}")

    counter += 1



