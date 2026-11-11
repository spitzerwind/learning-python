import turtle


# screen = turtle.Screen()

class Score(turtle.Turtle):

    def __init__(self):
        super().__init__()

        self.rscore = 0
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"{self.rscore}", align="center", font=("Courier", 24, "normal"))

    def increase(self):
        self.rscore += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("Game Over",align="center",font=("Courier", 46, "normal"))