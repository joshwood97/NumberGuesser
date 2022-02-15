from random import randint
from art import logo
print(logo)

EASY_TURNS = 10
HARD_TURNS =5

# Function to check if the users guess is the correct guess
# Track the number of turns and reduce by 1 if they get it wrong 
def check_answer(guess, answer, turns):
    """ Checks the answer against the guess. Returns the number of turns reminaing """
    if guess > answer:
        print("Too high. ")
        return turns -1
    elif guess < answer: 
        print("Too Low")
        return turns -1
    else:
        print(f"You got it right, the answer was {answer} ")

# Make a function for the difficulty 
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_TURNS
    elif difficulty == "hard":
        return HARD_TURNS

def game():

    print("Welcome to Josh's number guessing game")
    print("I'm thinking of a number between 0 - 100. ")

    #Generate random number
    answer = randint(1, 101)

    # for testing
    print(f"psst, the number is {answer}")

    # Make a function for the difficulty 
    turns = set_difficulty()

    # Let the user guess a number
    guess = 0
    # Repeat the guessing functionality if they get it wrong
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number. ")
        guess = int(input(" Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose. ")
            return
        elif guess != answer:
            print("Guess again. ")

game()
