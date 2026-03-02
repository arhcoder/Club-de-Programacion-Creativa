from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, direction):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.speed("fastest")
        self.right(90)
        if direction == 'left':
            self.goto(-350, 0)
        elif direction == 'right':
            self.goto(350, 0)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

        #self.backward(20)
        self.stop()

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

        #self.forward(20)
        self.stop()

    def stop(self):
        if 260 < self.ycor():
            self.forward(25)

        elif self.ycor() < -260:
            self.backward(25)