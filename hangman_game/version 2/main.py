import board
import player
import wordchoice
import DrawGallows
import time

# Loop Switches 
gameQuit = False
pickWord = True
drawFirstBoard = True 
guessLetter = True
playAgain = False


print(''' 
 _                                            
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  

         -Welcome to H A N G M A N by Dan- 

        ''')



# Main game loop
while gameQuit is False:
        
        # Prompts the player to enter their name
        time.sleep(3)
        player_name = input('What is your name?')

        
        # Loop for choosing a word
        while pickWord is True:
                time.sleep(3)
                word = input('Please choose a word or common phrase: ')
                my_word = wordchoice.MysteryWord(word)
                
                if my_word.valid() is True:
                        print('Your word is ' + my_word.word)
                        time.sleep(5)
                        break
                else:
                        print('Invalid word. Try again')
                pickWord = False

        

        # Loop for drawing the 1st game board
        while drawFirstBoard is True:
                my_board = board.Board(len(my_word.word))
                my_player = player.Player(player_name)
                my_board.drawBoard(my_word.indexOfSpaces())
                drawFirstBoard = False 


        # Loop for guessing letters in the mystery word
        while guessLetter is True:
                if board.Board.board == list(my_word.word):
                         print('You guessed the correct word: '+my_word.word)
                         guessLetter = False
                         playAgain = True
                         break
                                      
                if player.Player.guesses == 0:
                         print('You lose the world was: ' + my_word.word)
                         guessLetter = False
                         playAgain = True
                         break
                                         
                guess = my_player.guess(my_word.word)
                time.sleep(5)
                print('\n'*300)
                my_board.updateBoard(my_word.word, guess)
                my_player.printGuessList()
                DrawGallows.gallows(6 - player.Player.guesses)
               
                               

        # Loop that prompts user to play again or quit 
        while playAgain is True:
                play = input ('Would you like to play again \'Y\' or \'N\'')
                
                if play.lower() == 'n':
                        quit()
                        
                elif play.lower() == 'y':
                        print('Replay is not handled yet. Need to find a way to reset all objects')
                        time.sleep(5)
                        quit()
               


