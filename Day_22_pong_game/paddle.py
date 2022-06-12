from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        if position == "right":
            self.goto(350,0)
        elif position == "left":
            self.goto(-350,0)
        

    def move_up(self):
        new_y = self.ycor() + 15
        self.goto(self.xcor(), new_y)
        

    def move_down(self):
        new_y = self.ycor() - 15
        self.goto(self.xcor(), new_y)

    