class Card:
	def __init__(self,suit,value):
		self.suit=suit
		self.value=value
	def __repr__(self):
		return f"{self.value} of {self.suit}"
class Deck:
	def __init__(self):
		suits=["Hearts", "Diamonds", "Clubs", or "Spades"]
		values=['A', '2', '3', '4', '5', '6', '7','8','9','10',"J", "Q", "K"]
		self.cards=[Card(value,suit) for suit in suits for value in values]
	def __repr__(self):
		return f"Deck of {self.count()} cards"
	def count(self):
		return len(self.cards)