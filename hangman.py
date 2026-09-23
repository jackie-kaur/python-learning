print("Welcome to the game of Hangman!\n" \
"In this, you will guess the letters of the secret word that only the computer knows.")

import random

word_lst = ["animal", "fridge", "bamboo", "shared", "jungle", "values"]

random_num = random.randint(0, 6)

secret_word = word_lst[random_num]

memory = {}

lives = 5

count = 0

def print_word(secret_word, memory):
    for w in secret_word:
        if w in memory:
            print(w, end = '') 
        else:
            print("_ ", end = '')
    print("")

while True:
    letter = input("Choose letter  ")

    if letter in memory:
        print("Letter already used!")
    elif letter in secret_word:
        memory[letter] = True
        print_word(secret_word, memory)
        print(lives)
        count = count + 1
    elif letter not in secret_word:
        memory[letter] = True
        print_word(secret_word, memory)
        lives = lives - 1
        print(lives)
    
    if lives == 0:
        print("Game over!")
        print(f"'{secret_word}' was the word!")
        break

    if len(secret_word) == count:
        print("YOU WON!!!")
        break