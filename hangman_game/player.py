# Class for the player 


class Player(): 

        #Static Class variables
        guesses = 6 
        clues = 1
        guess_list = []

        def __init__(self,name): 

                self.name = name 


        def guess(self, mysteryword):
                guess = input('\nPlease choose a letter')
                if guess in Player.guess_list:
                        print('You already guessed that letter')
                elif len(guess) > 1:
                        print('You can only choose one letter at a time.')
                elif guess in mysteryword and len(guess) != 0:
                        print('Congrats '+ self.name + ' ! '+ guess + ' is in the mystery word')
                        Player.guess_list.append(guess)
                        return guess 
                else:
                        print('Sorry ' + self.name + ' ' + guess + ' is not in the mystery word') 
                        Player.guess_list.append(guess)
                        Player.guesses -= 1
                        print('You have '+ str(Player.guesses) + ' remaining')

        def printGuessList(self):
                print('           ' , Player.guess_list)
        



        
                

