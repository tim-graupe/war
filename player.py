from deck import Deck


class Player:
    def __init__(self, name, cards, in_play):
        self.name = name
        self.cards = []
        self.in_play = []

    def __str__(self):
        return f"my name is {self.name}. here are my cards: {self.cards}"
    
    # def receive_cards(self, deck, num_cards):
    #     deck.deal_cards(self.cards, num_cards)
