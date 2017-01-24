import DrawGallows
import ChooseWord


# Player chooses their word.
player_word = ChooseWord.chooseWord()
print('\n' *200)

#The gallows is drawn
print('\n' * 5)

# The player board is drawn
ChooseWord.drawEmptyLines(player_word)

letters_used = []
guesses= 0
while guesses < 6:
    print('\nPlease enter a letter: ')
    letter_guess = input()
    if letter_guess not in letters_used:
        if len(letter_guess) == 1:
            if letter_guess in player_word:
                print('Congrats! ' + letter_guess +' is in the mystery word')
                letters_used.append(letter_guess)
                print('Letters used =', letters_used, end = '')
            else:
                print('Sorry....'+ letter_guess +' is not in the mystery word')
                guesses += 1
                letters_used.append(letter_guess)
                print('Letters used =', letters_used, end = '')
                print('\n' * 10)
                DrawGallows.gallows(guesses)
                print('\n' * 5)
                ChooseWord.drawEmptyLines(player_word)

print('Sorry you lose the word was ' + ''.join(player_word))

    
#find a way to replace the empty slots with correct guesses
