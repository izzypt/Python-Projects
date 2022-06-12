from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24,  "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.leftPaddleScore = 0
        self.rightPaddleScore = 0
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.write(str(self.leftPaddleScore) + "|" + str(self.rightPaddleScore),False, align=ALIGNMENT, font=FONT)

    def updateLeftPaddleScore(self):
        self.leftPaddleScore += 1
        self.clear()
        self.write(str(self.leftPaddleScore) + "|" + str(self.rightPaddleScore),False, align=ALIGNMENT, font=FONT)

    def updateRightPaddleScore(self):
        self.rightPaddleScore += 1
        self.clear()
        self.write(str(self.leftPaddleScore) + "|" + str(self.rightPaddleScore),False, align=ALIGNMENT, font=FONT)