# Main BlackJack game file 

import player
import dealer 



GameQuit = False 
my_dealer = dealer.Dealer()
my_player = player.Player()

print('Welcome to Dan\'s blackjack program.')

# Main Game Loop
while GameQuit is False:
        
        my_player.getCards()
        my_player.hitOrStay()
