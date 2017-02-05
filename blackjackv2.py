import random
import math
import time

# TODO: Work on method which allows the player to hit continually until they lose or choose to stay
# Work on integrating Tkinter GUI to this program. 
# Further analyze the code. See if anything can be written more efficiently.
# Need to work on player Bust.

class Player:

	def __init__(self):
		self.total = 0
		self.players_cards = []

	def getCards(self, Dealer = True):
		self.players_cards = [random.randint(2,11) for _ in range(2)]
		if Dealer == True: 
			print('The dealer drew the following cards ' + ''.join(str(self.players_cards)))
		else:
			print('You drew following cards ' + ''.join(str(self.players_cards)))
		return self.players_cards

	def playerBust(self):
		if self.total > 21:
			return True
		else:
			return False

	def playerWin(self):
		if self.total == 21:
			return True
		else:
			return False

	def getTotal(self):
			self.total = sum(self.players_cards) + self.total
			#print('Total ', self.total)
			return self.total

class Game(Player):

	def Status(self, Dealer = True):
		outcomes = ['The dealer busts', 'The dealer wins', 'The Dealer hits and draws a card', 
					'You lose', 'You win', 'Hit/Stay']
		hit_or_stay = ''
		if Dealer == True:
			outcomes = outcomes[0:3]
			if self.total <= 16:
				self.players_cards.append(random.randint(2,11))
				print(outcomes[2])
			elif random.randint(1,40) < 20 and self.total < 21:
				self.players_cards.append(random.randint(2,11))			
		else:
			outcomes = outcomes[3:]
			hit_or_stay = input((outcomes[2]))
			
		if self.playerBust() == True: 
			print(outcomes[0])
			self.total = 0
			self.players_cards = []
		elif self.playerWin() == True:
			print(outcomes[1])
			self.total = 0
			self.players_cards = []
		
		print('Cards: ' , self.players_cards , 'Total ' , self.getTotal())
		return hit_or_stay

	def hit(self, hit_or_stay):
		if hit_or_stay.lower() == 'hit':
			print('test')
			self.getTotal()
		else:
			print('fail')

# Main game loop
Gameplay = True

while Gameplay is True:
	
	print('Welcome to Dan\'s BlackJack game')
	time.sleep(2)

	# A player and dealer object/instance are created from Game class
	dan = Game()
	dealer = Game()

	# The player draws their two cards
	dan.getCards(Dealer = False)

	# The player is prompted to hit or stay
	hit_or_stay = dan.Status(Dealer = False)

	# Gets the players answer hit or stay
	dan.hit(hit_or_stay)

	print('\n' * 5)

	# The dealer draws his two cards 
	dealer.getCards(Dealer = True)

	# The dealer hits or stay 
	dealer.Status(Dealer = True)

	#Check to see who won 
	if dealer.total == dan.total:
		print('You tied')
	elif dealer.total > dan.total:
		print('You lost...')
	elif dealer.total < dan.total: 
		print('You won!')

	# Prompt the user to quit or play again
	playAgain = input('Would you like to play again? ')
	if playAgain.lower() == 'yes':
		pass
	elif playAgain.lower() == 'no' :
		print('Thanks for playing') 
		GamePlay = False
		break
		
