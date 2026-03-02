# +----------------------------------------------------------------------------+
# | CARDUI TECH v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2026 - 2026, CARDUITECH.COM (www.carduitech.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.carduitech.com/license/
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: June 25th, 2022
# | Last update..: March 2nd, 2026
# | WhatIs.......: PongGame - Class
# +----------------------------------------------------------------------------++
# ------------------------- Libraries -------------------------
import random
from turtle import Screen

# -------------------------- Imports --------------------------
from paddle_class import Paddle
from ball_class import Ball
from scoreboard_class import Scoreboard

# -------------------------- Objects --------------------------
screen = Screen()

paddle_L = Paddle(direction='left')
paddle_R = Paddle(direction='right')
ball = Ball()
scoreboard = Scoreboard()

# ------------------------- Variables -------------------------
start_direction = random.choice(['left', 'right'])

# --------------------------- SetUp ---------------------------
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.listen()
screen.onkey(paddle_R.up, "Up")
screen.onkey(paddle_R.down, "Down")
screen.onkey(paddle_L.up, "a")
screen.onkey(paddle_L.down, "z")

# --------------------------- Code ----------------------------
game_is_on = True
while game_is_on:
    screen.update()
    ball.move(direction=start_direction)

    # Detect collision with the wall (Top and bottom walls)
    if 280 < ball.ycor() or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with both paddles
    if (ball.distance(paddle_R) < 50 and 320 < ball.xcor()) or (ball.distance(paddle_L) < 50 and ball.xcor() < -320):
        print("I hit the paddle")
        ball.bounce_x()

    # Detect if the ball went off the board's edge
    if ball.xcor() < -380 or 380 < ball.xcor():
        if ball.xcor() < -380:
            scoreboard.new_point('RIGHT')
        elif 380 < ball.xcor():
            scoreboard.new_point('LEFT')

        ball.hideturtle()
        ball.home()

        ball.showturtle()
        if start_direction == 'left':
            start_direction = 'right'
        elif start_direction == 'right':
            start_direction = 'left'

screen.exitonclick()
