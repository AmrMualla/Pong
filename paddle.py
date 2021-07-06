from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("orange")
        self.shapesize(stretch_wid = 5, stretch_len=1)
        self.penup()
        self.goto(pos)

    def go_up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def go_down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)
