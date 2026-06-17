import random
import hangman_words

lives = 6

import hangman_art
print (hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:


    print(f"****************************<???>/{lives}LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print (f"You have already guessed {guess}")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)




    if guess not in chosen_word:
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************\n The word was {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])
