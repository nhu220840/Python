# Hangman in Python
import random
from hm_wordlist import words

# dictionary of key: ()
hangman_art = {0: ( "                 ",
                    "                 ",
                    "                 "),
               1: ( "        o        ",
                    "                 ",
                    "                 "),
               2: ( "        o        ",
                    "        |        ",
                    "                 "),
               3: ( "        o        ",
                    "       /|        ",
                    "                 "),
               4: ( "        o        ",
                    "       /|\\      ",
                    "                 "),
               5: ( "        o        ",
                    "       /|\\      ",
                    "       /         "),
               6: ( "        o        ",
                    "       /|\\      ",
                    "       / \\      ")}

def display_art(wrong_guesses):
    print("*******************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*******************")

def display_hint(hint):
    for letter in hint:
        print(letter, end = " ")
    print()

def display_answer(answer):
    for letter in answer:
        print(letter, end = " ")
    print()

def main():
    wrong_guesses = 0
    guessed_letters = []
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    is_running = True

    while is_running:
        display_art(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess")
        elif guess in guessed_letters:
            print(f"{guess} is already guessed!")
        else:
            guessed_letters.append(guess)

            if guess in answer:
                for i in range(len(answer)):
                    if guess == answer[i]:
                        hint[i] = guess
            else:
                wrong_guesses += 1

            if wrong_guesses == 6:
                display_art(wrong_guesses)
                display_answer(answer)
                print("YOU LOSE!!!")
                is_running = False
            if "_" not in hint:
                display_art(wrong_guesses)
                display_answer(answer)
                print("YOU WIN!!!")
                is_running = False

if __name__ == '__main__':
    main()


