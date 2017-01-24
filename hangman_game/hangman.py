import DrawGallows
import ChooseWord


# Player chooses their word.

print('Choose your word or phrase')
print('The length of the word or phrase can not be more than 20 characters\n')
word = input()
print('\n' *200)

ChooseWord.chooseWord(word)
print('\n' *4)

DrawGallows.gallows(6)

guesses= 6
