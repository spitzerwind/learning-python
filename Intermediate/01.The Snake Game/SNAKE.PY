
from turtle import Turtle

up = 90
down = 270
left = 180
right = 0



initialbody_coordinates = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.body_snake = []
        self.create_snake()
        self.head = self.body_snake[0]

    def create_snake(self):

        for j in initialbody_coordinates:
            snaky = Turtle("square")
            snaky.color("white")
            snaky.penup()
            snaky.goto(j)
            self.body_snake.append(snaky)



    def move(self):

        for r in range(len(self.body_snake)-1,0,-1):
            new_x = self.body_snake[r-1].xcor()
            new_y = self.body_snake[r-1].ycor()
            self.body_snake[r].goto(new_x,new_y)
        self.body_snake[0].forward(20)


    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)




