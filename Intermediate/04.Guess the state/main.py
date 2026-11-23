import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
tutorial = turtle.Turtle()
tutorial.shape(image)
data = pandas.read_csv("50_states.csv")
not_guessed = []

correct_guesses= []


while len(correct_guesses) < 50:
    answer = screen.textinput(f"{len(correct_guesses)}/50 States correct","make a guess:")

    for guess in data["state"]:
        if answer.title() == guess:
            if  guess in correct_guesses:
                pass
            else:
                correct_guesses.append(guess)
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                var = (data[data["state"] == guess])

                t.goto(var["x"].item(),var["y"].item())
                t.write(guess)
        else:
            pass
    if answer.title() == "Exit":

        for state in data["state"]:
            if state not in correct_guesses:
                not_guessed.append(state)

        break
ref = turtle.Turtle()

print(correct_guesses)
score = len(correct_guesses)
print(f" your score is : {score}")

ref.penup()
ref.goto(0,0)
ref.hideturtle()
ref.write(f"your score is : {score} click to exit",font=("Arial",24,"bold"),align="center")
# new_data = pandas.DataFrame(not_guessed)
pandas.DataFrame(not_guessed).to_csv("not_guessed.csv")

screen.exitonclick()
