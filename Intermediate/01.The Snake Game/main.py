import turtle

import time
import snake

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SnakeGame")
screen.tracer(0)
turtle.listen()

snake = snake.Snake()



game_on = True
while game_on:

    time.sleep(1 / 10)
    snake.move()
    screen.update()





screen.listen()

screen.exitonclick()
