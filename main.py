from deck import Deck
from player import Player
from card import Card
from in_play_card import In_Play_Card

deuce = Player("deuce", [], [])
tim = Player("tim", [], [])


class Game():
    def __init__(self, players, game_over):
        self.player = []
        game_over = False
    def test():
        print('ho')

    def start_game():
        if len(tim.cards) == 0 and len(deuce.cards) == 0:
            cards = Deck()
            cards.create_deck()
            deck = cards.shuffle()
            def deal_cards():
                for i in range(26):
                    deuce.cards.append(deck.pop())
                    tim.cards.append(deck.pop())
            deal_cards()
    start_game()

    def test():
        print(deuce)
        print(tim)
    test()




    def draw_cards():
            input('hit enter to continue')
            deuce.in_play.append(deuce.cards.pop())
            tim.in_play.append(tim.cards.pop())
            # deuce_card = In_Play_Card(deuce.in_play[-1].suit, deuce.in_play[-1].value)
            # print(deuce_card)
            print(deuce.in_play[-1].value)
            print(tim.in_play[-1].value)
            if deuce.in_play[-1].value > tim.in_play[-1].value:
                deuce.cards.extend(tim.in_play)
                deuce.cards.extend(deuce.in_play)
                tim.in_play.clear()
                deuce.in_play.clear()
                print("deuce won!")
            elif tim.in_play[-1].value > deuce.in_play[-1].value:
                tim.cards.extend(deuce.in_play) 
                tim.cards.extend(tim.in_play)
                deuce.in_play.clear()
                tim.in_play.clear()
                print("tim won!")   
    draw_cards()        

    def game_over():
        return len(tim.cards) == 0 or len(deuce.cards) == 0

    while not game_over():
        draw_cards()
