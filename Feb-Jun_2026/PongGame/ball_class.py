from turtle import Turtle
from scoreboard_class import Scoreboard
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("SlateBlue2")
        self.shape("circle")
        self.penup()
        # self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        # self.speed("slow")
        # self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10

    def move(self, direction):
        # self.stop()
        if direction == 'right':
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)
        elif direction == 'left':
            new_x = self.xcor() - self.x_move
            new_y = self.ycor() - self.y_move
            self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
