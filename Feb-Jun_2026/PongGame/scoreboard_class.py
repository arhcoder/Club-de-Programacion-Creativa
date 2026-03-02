from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 50, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.LEFTscore = 0
        self.RIGHTscore = 0
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.sety(230)
        self.pencolor("white")
        self.write(f"{self.LEFTscore} | {self.RIGHTscore}", align=ALIGNMENT, font=FONT)

    def new_point(self, side):
        self.clear()
        if side == 'LEFT':
            self.LEFTscore += 1
        elif side == 'RIGHT':
            self.RIGHTscore += 1
        self.write(f"{self.LEFTscore} | {self.RIGHTscore}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

