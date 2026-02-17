# +----------------------------------------------------------------------------+
# | CARDUI TECH v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2026 - 2026, CARDUITECH.COM (www.carduitech.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.carduitech.com/license/
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: January 23rd, 2022
# | Last update..: February 8th, 2026
# | WhatIs.......: Blackjack Game - Main
# +----------------------------------------------------------------------------++
# ------------------------- Instructions -----------------------
# TODO:

# ------------ Resources / Documentation involved -------------
# HOW TO PLAY BLACKJACK: https://sites.math.duke.edu/~rtd/MEC/prob/blackjack.html

# ------------------------- Libraries -------------------------
import random

# -------------------------- Imports --------------------------
from art import logo
from art import bye

# ------------------------- Functions -------------------------
def want_to_play(user_1_cards, user_1_score, user_2_cards, user_2_score):
    right_answer = False

    while right_answer == False:
        user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

        if user_choice == 'y':
            # clear()

            # User stuff
            user_1_cards *= 0
            user_1_score[0] = '0'

            # Computer stuff
            user_2_cards *= 0
            user_2_score[0] = '0'

            Blackjack()
            right_answer = True

        elif user_choice == 'n':
            print(bye)
            right_answer = True

        else:
            print("   Pleace type 'y' or 'n': ")


def get_new_card(player, player_cards, player_score):
    # print(f"\n{player}")
    random_choice = random.randint(0, 12)
    player_cards.append(cards[random_choice])

    # print(f"new_card = {cards[random_choice]}")
    score = 0
    for card in player_cards:
        score += int(card)

    player_score[0] = score


def print_player_scores():
    print(f"  Your cards: {user_cards}, current score: {str(user_score[0])}")
    # print(f"  Computer's first card: {computer_cards[0]}                        DELETE: Computer's cards: {computer_cards}, current score: {str(computer_score[0])}")
    print(
        f"  Computer's first card: {computer_cards[0]}")
    # print(f"  Computer's first card: {computer_cards[0]}")


def game_over():
    print(f"  Your final hand: {user_cards}, final score: {str(user_score[0])}")
    print(f"  Computer's final hand: {computer_cards}, final score: {str(computer_score[0])}")


def newCard_or_Pass():
    right_answer = False

    while right_answer == False:

        user_choice = input("** Type 'y' to get another card, type 'n' to pass: ")

        if user_choice == 'y':
            get_new_card(player='user', player_cards=user_cards, player_score=user_score)
            print_player_scores()

            # ADD RULES HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if 21 < int(user_score[0]):
                game_over()
                print("\nYou have scored higher than 21. You lose :( \n")
                want_to_play(user_1_cards=user_cards, user_1_score=user_score, user_2_cards=computer_cards,
                             user_2_score=computer_score)

            elif (11 and 10 in user_cards) and (10 and 11 not in computer_cards):
                game_over()
                print("\nCongratulations! You have got a blackjack. You win! :D \n")
                want_to_play(user_1_cards=user_cards, user_1_score=user_score, user_2_cards=computer_cards,
                             user_2_score=computer_score)

            right_answer = True

        elif user_choice == 'n':
            while int(computer_score[0]) < 16:
                get_new_card(player='computer', player_cards=computer_cards, player_score=computer_score)

            print_player_scores()

            # ADD RULES HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            if (10 and 11) in computer_cards:
                game_over()
                print("\nYou lose. Computer has got a blackjack. 86\n")
                want_to_play(user_1_cards=user_cards, user_1_score=user_score, user_2_cards=computer_cards,
                             user_2_score=computer_score)

            elif (11 and 10 in user_cards) and (10 and 11 not in computer_cards):
                game_over()
                print("\nCongratulations! You have got a blackjack. You win! :D \n")
                want_to_play(user_1_cards=user_cards, user_1_score=user_score, user_2_cards=computer_cards,
                             user_2_score=computer_score)

            elif int(computer_score[0]) < int(user_score[0]):
                game_over()
                print("\nCongratulations! Your score is higher than the computer's. You win! :D \n")
                want_to_play(user_1_cards=user_cards, user_1_score=user_score, user_2_cards=computer_cards,
                             user_2_score=computer_score)

            elif int(user_score[0]) < int(computer_score[0]):
                game_over()
                print("\n Your score is less than the computer's. You loose :( \n")
                want_to_play(user_1_cards=user_cards, user_1_score=user_score, user_2_cards=computer_cards,
                             user_2_score=computer_score)

            elif int(computer_score[0]) == int(user_score[0]):
                game_over()
                print("\n Your score is equal to the computer's. I don't know what to do :| \n")
                want_to_play(user_1_cards=user_cards, user_1_score=user_score, user_2_cards=computer_cards,
                             user_2_score=computer_score)

            else:
                game_over()
                print("\n Ugh. This is an unexpected situation... \n")
                want_to_play(user_1_cards=user_cards, user_1_score=user_score, user_2_cards=computer_cards,
                             user_2_score=computer_score)

            right_answer = True

        else:
            print("   Pleace type 'y' or 'n': ")


def Blackjack():
    print(logo)

    get_new_card(player='computer', player_cards=computer_cards, player_score=computer_score)
    get_new_card(player='user', player_cards=user_cards, player_score=user_score)
    get_new_card(player='computer', player_cards=computer_cards, player_score=computer_score)
    get_new_card(player='user', player_cards=user_cards, player_score=user_score)

    if (10 and 11) in computer_cards:
        game_over()
        print("\nYou lose. Computer has got a blackjack.\n")
        want_to_play(user_1_cards=user_cards, user_1_score=user_score, user_2_cards=computer_cards,
                     user_2_score=computer_score)

    elif (11 and 10 in user_cards) and (10 and 11 not in computer_cards):
        game_over()
        print("\nCongratulations! You have got a blackjack. You win! :D \n")
        want_to_play(user_1_cards=user_cards, user_1_score=user_score, user_2_cards=computer_cards,
                     user_2_score=computer_score)

    else:
        print_player_scores()

        game_is_over = False

        while game_is_over == False:

            if int(user_score[0]) == 21:
                print("\nCongratulations! You win :D \n")
                game_over()
                game_is_over = True

            elif 21 < int(user_score[0]):
                print("\nYou went over 21. You lose :(\n")
                game_over()
                game_is_over = True

            else:
                newCard_or_Pass()

        if game_is_over == True:
            print("The game is over. Thanks for playing.")

# ------------------------- Variables -------------------------
# User stuff
user_cards = []
user_score = ['0']

# Computer stuff
computer_cards = []
computer_score = ['0']

# Game Stuff
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# --------------------------- Code ----------------------------
want_to_play(user_1_cards=user_cards, user_1_score=user_score, user_2_cards=computer_cards, user_2_score=computer_score)
