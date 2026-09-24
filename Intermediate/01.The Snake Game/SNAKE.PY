blocks = []

turtle_pos = [(0, 0), (-20, 0), (-40, 0)]
from turtle import Screen,Turtle
screen = Screen()
class Snake:
    def __init__(self):

        for coordinates in turtle_pos:
            newblock = Turtle()
            newblock.color("red")
            newblock.shape("square")
            newblock.penup()
            blocks.append(newblock)
            newblock.goto(coordinates)



    def move(self):
        for blocky in range(len(blocks)-1,0,-1):
                new_x =  blocks[blocky-1].xcor()
                new_y = blocks[blocky-1].ycor()
                blocks[blocky].goto(new_x,new_y)
        blocks[0].forward(20)

