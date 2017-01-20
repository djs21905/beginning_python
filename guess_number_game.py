# Guess the number game.
# Call the input function to allow a user to enter a number

import random

print('Hello what is your name?')
name = input()

random_number = random.randint(1,20)

print('Well '+ name + ' I am thinking of a number between 1 and 20')

try:
    print('Take a guess. You have 6 total guesses')
    for guesses in range(1,7):
        guess = int(input())
        if guess < random_number:
            print('Your guess was too low try again')
        elif guess > random_number:
            print('Your guess was too high try again')
        else:
            break # This condition is for the correct guess 
        print('You have '+ str(6-guesses)+ ' remaining ')
except:
    pass


if guess == random_number:
    print('Wow you guessed the correct number good job')
else:
    print('nope the number I was thinking of was ' + str(random_number))
