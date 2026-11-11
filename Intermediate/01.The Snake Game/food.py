from turtle import Turtle
import random




class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.penup()
        self.shapesize(0.5,0.5)
        self.coordinates()

    def coordinates(self):
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.goto(x,y)
