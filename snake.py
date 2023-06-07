from turtle import Turtle,Screen
import time
screen=Screen()


class Snake:
    def __init__(self):
        self.turtles=[]
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            new_turtle = Turtle("square")
            new_turtle.penup()
            new_turtle.goto(-20 * i, 0)
            new_turtle.color("white")
            self.turtles.append(new_turtle)

    def move_snake(self):
        for i in range(len(self.turtles)-1, 0, -1):
            self.turtles[i].goto(self.turtles[i - 1].pos())
        # self.turtles[0].setheading(0)
        self.turtles[0].forward(20)

    def snake_right(self):
        if self.turtles[0].heading()!=180:
            self.turtles[0].setheading(0)


    def snake_left(self):
        if self.turtles[0].heading()!=0:
            self.turtles[0].setheading(180)


    def snake_up(self):
        if self.turtles[0].heading()!=270:
            self.turtles[0].setheading(90)

    def snake_down(self):
        if self.turtles[0].heading()!=90:
            self.turtles[0].setheading(270)


    def yon(self):
        print(self.turtles[len(self.turtles)-1].heading())

    def collision_with_wall(self):
        if self.turtles[0].xcor()==-300 or self.turtles[0].xcor()==300 or self.turtles[0].ycor()==-300 or self.turtles[0].ycor()==300:
            print("Y")

    def add_tail(self,position):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.color("white")
        self.turtles.append(new_turtle)
        new_turtle.goto(position)


