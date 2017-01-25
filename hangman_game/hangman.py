# This is the main Hangman Game file 
# TODO: Clean Up Code 

import DrawGallows
import ChooseWord

# Player chooses their word.
player_word = ChooseWord.mysteryWord()
print('\n' *200)

letters_used = []
guesses= 0
gameloss = True

# Variable used as an argument in the drawBoard function.  
# Switches the state of the function. 
counter = 0 

# Main Game Loop.  Iterates as long as guesses < 6.  
# After each iteration of the loop when an incorrect letter is chosen guesses = guess + 1 
while guesses < 6:
    print('\n' * 5)
    a = ChooseWord.drawBoard(player_word, letters_used, counter)
    #Checks each iteration to see if the player guessed the correct word
    if a == player_word:
        print('you guessed the correct word: ' + ''.join(player_word))
        gameloss = False
        break
    print('\nPlease enter a letter: ')
    letter_guess = input()          
    if letter_guess not in letters_used and len(letter_guess) == 1:
        if letter_guess in player_word:
            letters_used.append(letter_guess)
            print('\n' * 10)
            DrawGallows.gallows(guesses)
            print('Congrats! ' + letter_guess +' is in the mystery word')
        else:
            guesses += 1
            letters_used.append(letter_guess)
            print('\n' * 10)
            DrawGallows.gallows(guesses)
            print('Sorry....'+ letter_guess +' is not in the mystery word')
    elif len(letter_guess) > 1:
        print('You cant guess more than one letter at a time')
    else:
        print('The letter you guessed was already used')

    
    print('Letters used =', letters_used, end = '')
    print('\nYou have ' +str(6-guesses) + ' wrong guesses remaining') 
    counter +=1
    
    
# Message displayed if the player runs out of guesses
# and did not guess the correct word.
if gameloss == True:
    print('Sorry you lose the word was ' + ''.join(player_word))


    

