
from turtle import Screen
import snake
import time
from food import Food
# import score
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("snake and apples")
screen.tracer(0)
screen.listen()
snake = snake.Snake()
food = Food()


screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey( snake.right ,"Right")

scoreboard = Score()
game_is_on = True

#game set to be on
while game_is_on:

    screen.update()
    time.sleep(0.25)
    snake.move()

# eating food
    if snake.head.distance(food) < 15:
        food.coordinates()
        scoreboard.increase()
        snake.extend_body()
#hitting the wall

    if snake.head.xcor()< -280 or snake.head.xcor()>280 or snake.head.ycor()<-280 or snake.head.ycor()>280:
        scoreboard.game_over()
        game_is_on = False

    for segment in snake.body_snake:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
