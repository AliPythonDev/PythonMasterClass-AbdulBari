#Q1) Guess the Number between 1 - 10
#User is prompted to enter a number. If the user guesses wrong then the prompt appears again( larger or smaller ) until the guess is correct, on successful guess, user will get a “correct answer!" message, and the program will exit.)
import random
n = random.randint(1,10)
guess = 0
while guess != n:
    guess = int(input("Guess a Number: "))
    if guess < n:
        print("It is Smaller Number.")
    elif guess > n:
        print("It is Greater Number.")
    else:
        print("Congratulations! It's a Correct Answer.")