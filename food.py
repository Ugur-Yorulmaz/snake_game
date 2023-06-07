import random
import turtle
from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color("yellow")
        self.speed("fastest")
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        self.goto(x,y)


    def locate_food(self):
        lokma_x=random.randint(-280,280)
        lokma_y=random.randint(-280,280)
        self.goto(lokma_x,lokma_y)
