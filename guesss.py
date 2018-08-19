#this is a guessing game
#the computer generates a random number between 0 and 100
#it asks a user to make a guess
#if the guess is thesame with the random number generated by the computer, it says Congratulations
#if not, it either says too high or too low, try again
import random

number = random.randint(1 , 100)
guess = 0
numOfTries = 0
while guess != number:
    guess = int(input("Please make a guess: "))
    numOfTries = numOfTries + 1

    if guess > number:
        print ("Too high, Try again ! ")
    elif guess < number:
        print ("Too low, Try again ! ")
    if guess == number:
        print ("Congratulations ! ")
print ("You got it in ", numOfTries ," guesses")
