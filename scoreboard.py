from turtle import Turtle

ALIGN = "center"
FONT = ("Arial",16,"normal")

with open("data.txt", mode="r") as file:
    saved_score = int(file.read()) # convert string to int

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = saved_score
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=240)
        self.write(f"Hit 'space bar' to pause/resume the game.\n           Score: {self.score} / Highest score: {self.highest_score}"
                   ,align=ALIGN,font=FONT)

    def increase_score(self):
        self.score += 1
        self.write(f"Score: {self.score} / Highest score: {self.highest_score}", align=ALIGN, font=FONT)

    def reset_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as file:
                new_saved_score = file.write(str(self.highest_score)) #file.write() only accepts strings, so we use str(self.highest_score)
            self.clear()
            self.score = 0
            self.write(f"Score: {self.score} / Highest score: {self.highest_score}", align=ALIGN, font=FONT)
        else:
            self.clear()
            self.score = 0
            self.write(f"Score: {self.score} / Highest score: {self.highest_score}", align=ALIGN, font=FONT)
