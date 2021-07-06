from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("orange")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)
    
    def bouncey(self):
        self.y_move *= -1
        self.move_speed *= 0.9
    
    def bouncex(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bouncex()
