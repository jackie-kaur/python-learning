print("Welcome to the game of Hangman!\n" \
"In this, you will guess the letters of the secret word that only the computer knows.")

import random

word_lst = ["animal", "fridge", "bamboo", "shared", "jungle", "values"]

random_num = 0 #random.randint(0, 6)
secret_word = word_lst[random_num]
memory = {}
lives = 5
count = 0

def print_word(secret_word, memory, lives):
    for w in secret_word:
        if w in memory:
            print(w, end = '') 
        else:
            print("_ ", end = '')
    print(f", lives left: {lives}")

def same_letter_count(secret_word, letter):
    count = 0
    for w in secret_word:
        if w == letter:
            count = count + 1
    return count

while True:
    letter = input("Choose letter  ")
    if letter.lower() < "a" or letter.lower() > "z":
        print("Please choose a letter from a-z.")
        continue
    if letter in memory:
        print("Letter already used!")
    elif letter in secret_word:
        memory[letter] = True
        print_word(secret_word, memory, lives)
        count = count + same_letter_count(secret_word, letter)
    elif letter not in secret_word:
        memory[letter] = True
        print_word(secret_word, memory, lives)
        lives = lives - 1
    
    if lives == 0:
        print("Game over!")
        print(f"'{secret_word}' was the word!")
        ask = input("Do you want to play again? (y/n)  ")
        if ask == "y":
            random_num = random.randint(0, 6)
            secret_word = word_lst[random_num]
            memory = {}
            lives = 5
            count = 0
        else:
            break
    if len(secret_word) == count:
        print("YOU WON!!!")
        ask = input("Do you want to play again? (y/n)  ")
        if ask == "y":
            random_num = random.randint(0, 6)
            secret_word = word_lst[random_num]
            memory = {}
            lives = 5
            count = 0
        else:
            break