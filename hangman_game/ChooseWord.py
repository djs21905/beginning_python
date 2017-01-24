#Function that allows the player to choose a word.
#Must make all incoming letters set to lowercase
#Cannot contain numbers or special characters
#If everything above is met, empty lines are drawn for the number of chars in word

#TODO prevent bad characters from being used.

def chooseWord():
    while True:
        print('Please enter a word')
        player_word = input()
        bad_characters = '0123456789!@#/<>`~!.?'
        bad_characters_list = list(bad_characters)
        player_word_as_list = list(player_word.lower())
        for item in player_word_as_list:
                if len(player_word_as_list) <=20 and item not in bad_characters_list:
                    print(item)
                else:
                    print('failure')
                    break
        
 

    
    


chooseWord()

#print(a)

