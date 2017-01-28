# Dealer Class 



import random

class Dealer():

	# Static variables
	dealers_cards = [] 
	total = 0

	# Method that chooses two random integers ranging from 2 - 11 
	# The random values are then appeneded to the dealers_cards list
	# Returns a tuple containing a list of the two cards and the total of those two numbers
	def getCards(self):
		for cards in range(2):
			Dealer.dealers_cards.append(random.randint(2,11))

		print('The dealer has a ' + str(Dealer.dealers_cards[0]) + ' showing, and a hidden card.' )
		print('His total is hidden too')
		Dealer.total = Dealer.dealers_cards[0] + Dealer.dealers_cards[1]
		return Dealer.total


	# If the Dealer.total is <= 16 the dealer hits
	# A random integer in range 2-11 is drawn, appended to the dealers_card list
	# And the most recent card at index -1 in dealers_card list is added to the Dealer.total
	# If the value is greater than 16 theres a 50 percent chance the robot will Hit 
	def dealerHit(self, total):
		randomnum = random.randint(1,40)

		if Dealer.total <=16:
			Dealer.dealers_cards.append(random.randint(2,11))
			Dealer.total = Dealer.total + Dealer.dealers_cards[-1] 
			print('The Dealer Chooses to hit and draws a ' + str(Dealer.dealers_cards[-1]))
		elif randomnum < 20:
			Dealer.dealers_cards.append(random.randint(2,11))
			Dealer.total = Dealer.total + Dealer.dealers_cards[-1] 
			print('The Dealer Chooses to hit and draws an ' +  str(Dealer.dealers_cards[-1]))
		else:
			print('The Dealer Stays.')
		

		print('The dealers total was ' + str(Dealer.total))
		return Dealer.total


	# Checks to see if the dealer has busted , won or has < 21 
	# If the player busts True is returned
	# If the player wins False is returned
	# and if the players total < 21 the dealers total is returned. 
	# If the dealer busts, dealers_cards list is emptied and the total is reset to 0
	def dealerBust(self):
		if Dealer.total > 21:
			Dealer.dealers_cards = []
			Dealer.total = 0
			return True
		elif Dealer.total == 21:
			return False 
		else:
			return Dealer.total

	# Reveals the dealers second card which was hidden.
	def dealerReveal(self):
		print('The dealers hidden card was a ' + str(Dealer.dealers_cards[1]))




