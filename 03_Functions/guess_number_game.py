# Writing a program:  Step-by-step, create a game
import random

print("Hey! What's your name?")
name = input()

print(f"Ok {name}, I'm thinking of a number between 1 and 20.")
secretNum = random.randint(1,20)

for guessesTaken in range(1,7):
    print("Take a guess.")    
    guess = int(input())
    
    if guess < secretNum:
        print("Your guess is too low.")
    elif guess > secretNum:
        print("Your guess is too high.")
    else:
        break   # This condition is for the correct guess!

if guess == secretNum:
    print(f"Nice job {name}!  You got it in {guessesTaken} guesses.")
else:
    print(f"Nope! The answwer I was thinking of was {secretNum}.")

print(f"You took {guessesTaken} guesses.")
