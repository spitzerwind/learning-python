rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

listo = ["Rock","Paper","Scissor"]

computer = random.randint(a=0 , b=2)
# print (listo[computer])
computer_plays = listo[computer]


User_play = input("""please pick from 'r','p','s' respectively""")
user_play = User_play.capitalize()



if computer_plays == "Rock":
    print(""" Computer's choice:\n""")
    print(rock+"\n")
    if user_play == "R":
        print("your play :" + rock + "\n")
        print("draw")
    elif user_play == "S":
        print("your play :" + scissors + "\n")
        print("you lost")
    elif user_play == "P":
        print("your play :" + paper + "\n")
        print("you won")


elif computer_plays == "Paper":
    print(""" Computer's choice:\n """)
    print(paper + "\n")
    if user_play == "R":
        print("your play :" + rock + "\n")
        print("you lost")
    elif user_play == "S":
        print("your play :" + scissors + "\n")
        print("you won")
    elif user_play == "P":
        print("your play :" + paper + "\n")
        print("draw")


else:
    print(""" Computer's choice:\n""")
    print(scissors + "\n")
    if user_play == "R":
        print("your play :" + rock + "\n")
        print("you win")
    elif user_play == "S":
        print("your play :" + scissors + "\n")
        print("draw")
    elif user_play == "P":
        print("your play :" + paper + "\n")
        print("you lost")
      
