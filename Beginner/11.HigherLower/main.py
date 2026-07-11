from random import choices

import art
import game_data
import random









a_random = random.randint(0, 49)
score = 0


game_ovr = False
while not game_ovr:

    print(art.logo)

    b_random = random.randint(0, 49)
    # b_random = random.choices(game_data.data())

    versusA = (game_data.data[a_random]['name'] + ", a " + game_data.data[a_random]['description'] + ", from " +
               game_data.data[a_random]['country'])
    versusB = (game_data.data[b_random]['name'] + ", a " + game_data.data[b_random]['description'] + ", from " +
               game_data.data[b_random]['country'])
    folA = int(game_data.data[a_random]['follower_count'])
    folB = int(game_data.data[b_random]['follower_count'])
    # print(f"You're right! Current score {score}")
    print(f"Compare A: {versusA}")
    print(art.vs)
    print(f"Against B: {versusB}")


    user_answer = str(input("Who has more followers? Type 'A' or 'B': ")).lower()

    if folA > folB:
        correct_answer = "a"
    else:
        correct_answer = "b"



    if user_answer == correct_answer:
        score = score + 1
        print("\n"*20)
        print(f"You're right! Current score {score}")
        a_random = b_random
    elif user_answer != correct_answer:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_ovr = True










