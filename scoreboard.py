from turtle import Turtle
ALLIGNMENT="center"
FONT=("Comic",15,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score=0
        self.penup()
        self.goto(0, 260)
        self.write(f"Score  :{self.score}",align=ALLIGNMENT,font=FONT)
        self.hideturtle()

    def renew(self):
        self.clear()
        self.score+=1
        self.write(f"Score  :{self.score}",align="center",font=("Arial",15,"normal"))

    def lose(self):
        self.clear()
        self.write(f"You lost! Your score was :{self.score}",align="center",font=("Arial",15,"normal"))

