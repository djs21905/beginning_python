# Player Chooses a word <21 Chars
# If the Word is <21 chars it enters the for loop 
# If the word is >=21 the program prompts the user to enter a word of proper length. 
# The for loop checks each item in the bad_characters_list against the player_word_as_list
# If one of those items shows up in the player_word_as_list "fail" is printed
# Otherwise, the player_word_as_list is returned.

def chooseWord():
        bad_characters = '0123456789!@#/<>`~!.?'
        bad_characters_list = list(bad_characters)
        while True:
                Switch = 20
                print('Please enter a word')
                player_word = input()
                player_word_as_list = list(player_word.lower())
                if len(player_word_as_list) > 0 and len(player_word_as_list)  <= 20:
                        for char in bad_characters_list:
                                if char in player_word_as_list:
                                        print(char)
                                        print('Your word contained a prohibited character')
                                        print('')
                                        Switch = 30
                                        #I need to break out of the for loop and re renter the main loop (add break?)
                        while Switch == 20:
                                print('Did you choose the proper word?   Word = ' + player_word)
                                print('Type \"Yes\" if you did and \"No\" if you didnt')
                                right_word = input()
                                if right_word.lower() == 'Yes'.lower():
                                        return player_word_as_list
                                else:
                                        break
                else:
                        print()
                        print('Enter a word that is < 21 chars') 
    
    
def drawEmptyLines(player_word_as_list):
        for char in player_word_as_list:
                if char == ' ':
                        print('    ', end = '')
                else:
                        print('____ ', end = '')


a= chooseWord()

drawEmptyLines(a)
