from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24,  "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.updateScore()

    def increase_score(self):
        self.score += 1

    def updateScore(self):
        self.clear()
        self.penup()
        self.goto(0,265)
        self.write(f"Score: {self.score} ", False, align=ALIGNMENT, font=FONT)

    def gameOver(self):
        self.goto(0,0)
        self.write(f"Game Over.", False, align=ALIGNMENT, font=FONT)