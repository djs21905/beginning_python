# Player Class 


import random
import time

class Player():

	# Static variables 
	total = 0 
	players_cards = []
	

	def getCards(self):
		for cards in range(2):
			Player.players_cards.append(random.randint(2,11))
		print('The dealers shuffles the deck and hands you two cards')
		time.sleep(3)
		print('You get a ' + str(Player.players_cards[0]) + ' and a ' + str(Player.players_cards[1]))
		Player.total = Player.players_cards[0] + Player.players_cards[1]
		print('Your total is ' + str(Player.total))
		return Player.total

	def hitOrStay(self):
			while True:
				choice = input('Would you like to \"hit\"" or \"stay\"')
				if choice.lower() == 'stay':
					print('Okay, dealers turn')
					break
				elif choice.lower() == 'hit':
					Player.players_cards.append(random.randint(2,11))
					Player.total = Player.total + Player.players_cards[-1] 
					print('You drew a ' + str(Player.players_cards[-1]))
					print('Your total is ' + str(Player.total))







