# Main BlackJack game file 

import player
import dealer
import time 


GameQuit = False 
my_dealer = dealer.Dealer()
my_player = player.Player()


print('Welcome to Dan\'s blackjack program.')
print('\n'* 3)

# Main Game Loop
while GameQuit is False:

        # The player gets cards and hits or stays
        my_player.getCards()
        print('\n' * 3) 
        my_player.hitOrStay()
               

        # Brief pause 
        time.sleep(2)
        print('\n' * 5)

        
        # The dealer gets cards and hits or stays
        if player.Player.total != 0 and player.Player.total != 21: 
                my_dealer.getCards()
                my_dealer.dealerHit()
      

        # Checks to see who won the game.
        if player.Player.total > dealer.Dealer.total or dealer.Dealer.total > 21:
                print('You beat the Dealer')
        elif player.Player.total < dealer.Dealer.total and dealer.Dealer.total <= 21:
                print('The Dealer beat you')
       


        playAgain = input('Would you like to play again? ')
        if playAgain.lower() == 'yes':
                print('\n' * 10)
                pass
        elif playAgain.lower() == 'no' :
                print('Thanks for playing') 
                GameQuit = True 
                
