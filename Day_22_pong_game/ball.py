from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_movement = 10
        self.y_movement = 10

    def move(self):
        x_cor = self.position()[0]
        y_cor = self.position()[1]
        self.goto(x_cor + self.x_movement , y_cor + self.y_movement)

    def bounce(self):
        self.y_movement *= -1

    def hitback(self):
        self.x_movement *= -1