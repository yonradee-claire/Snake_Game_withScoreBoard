from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #the turtle is 20*20. So, 0.5 means 10. Now our turtle is 10*10
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(x=random.randint(-280,280),y=random.randint(-280, 280))