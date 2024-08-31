from random import randint
from art import logo


EASY_LEVEL = 10
HARD_LEVEL = 5


def difficulty_set():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL
    

def check_answer(guess, answer, turns):
    if guess > answer:
        print("too high")
        return turns - 1
        
    elif guess < answer:
        print("too low")
        return turns - 1
        
    else:
        return f"you got is answer was {answer}"


def play_game():

    print("welcome To The Number Guessing Game")
    print(logo)

    answer = randint(1, 100)
    
    turns = difficulty_set()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

    
play_game()        




    