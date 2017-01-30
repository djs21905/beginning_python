# Dealer Class 
import time
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
		if Dealer.total > 21:
			print('Dealer Bust')
			Dealer.total = 0 
			Dealer.dealers_cards = []

		return Dealer.total


	# If the Dealer.total is <= 16 the dealer hits
	# A random integer in range 2-11 is drawn, appended to the dealers_card list
	# And the most recent card at index -1 in dealers_card list is added to the Dealer.total
	# If the value is greater than 16 theres a 50 percent chance the robot will Hit 
	def dealerHit(self):
		while True:
			randomnum = random.randint(1,40)
			print('\n' * 2)
			if Dealer.total <=16:
				Dealer.dealers_cards.append(random.randint(2,11))
				Dealer.total = Dealer.total + Dealer.dealers_cards[-1] 
				print('The Dealer Chooses to hit and draws a(n) ' + str(Dealer.dealers_cards[-1]))
				time.sleep(2)
			if Dealer.total == 21: 
				print('The dealer hit B L A C K J A C K')
				Dealer.total = 0 
				Dealer.dealers_cards = []
				break
			if Dealer.total > 21:
				print('Dealer bust')
				print('The dealers total was ' + str(Dealer.total))
				Dealer.total = 0 
				Dealer.dealers_cards = []
				break
			elif randomnum < 20 and Dealer.total < 21 :
				Dealer.dealers_cards.append(random.randint(2,11))
				Dealer.total = Dealer.total + Dealer.dealers_cards[-1] 
				print('The Dealer Chooses to hit and draws a(n) ' +  str(Dealer.dealers_cards[-1]))
				time.sleep(2)
			else:
				print('The Dealer Stays.')

			print('The dealers hidden card was a(n) ' + str(Dealer.dealers_cards[1]))
			time.sleep(5)
			print('\n' * 3)
			print('The dealers total was ' + str(Dealer.total))
			return Dealer.total





