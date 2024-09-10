import random
from card import Card
class Deck:
    def __init__(self):
        self.suits = ['♠', '♥', '♣', '♠']
        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.deck = []

    def create_deck(self):
        for i in self.suits:
                for j in self.values:
                    self.deck.append(Card(i, j))
        return self.deck
    
    def shuffle(self):
         random.shuffle(self.deck)
         return self.deck
    
    # def deal_cards(self, receiving_deck, num_cards):
    #     for i in range(num_cards):
    #         if self.deck:
    #             receiving_deck.append(self.deck.pop())

# p1 = Deck()
# p1.create_deck()
# deck = p1.shuffle()
# print(deck)