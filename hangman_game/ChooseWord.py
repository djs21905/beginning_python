# Defines the function mysteryWord which allows the player to choose a hangman word
# The word must be no longer than 20 characters and greater than 0 
# The word can not contain any characters from the bad_characters_list
# TODO: Streamline the code. Make it more readable and efficient if possible. 

def mysteryWord():
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
    
# Defines the function drawBoard which prints a hangman board 
# Iterates through the player_word_as_list and print a ____ for each character 
# If the character is an empty space an empty space is printed   
# COMPLETED 01/24/17

def drawBoard(player_word_as_list,guess_list,counter):
        empty_line_object = '_ '
        space_object = ''
        blank_list = []
        if counter == 0: 
                for item in player_word_as_list:
                        if item != ' ':
                                blank_list.append(empty_line_object)
                        else:   
                                blank_list.append('  ')
                print (''.join(blank_list))
        else:
        # I want the first part to happen once in the beginning and the second part to happen the rest
                for item in player_word_as_list:
                        if item != ' ':
                                blank_list.append(empty_line_object)
                        else:   
                                blank_list.append('  ')
                for x in guess_list:
                        if x in player_word_as_list:
                                a = player_word_as_list.index(x)
                                blank_list[a] = x
                print (''.join(blank_list))
                                


                        

                 
                           



