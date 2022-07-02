from random import shuffle
from typing import List

from classes.board import Board
from classes.card import Card
from classes.deck import Deck
from classes.hand import Hand
from classes.globals import TYPES



# class Deck:
#     def __init__(self):
#         self.cards = []
#         for i in range(2, 15):
#             for j in range(4):
#                 self.cards\
#                     .append(Card(i,
#                                  j))
#         shuffle(self.cards)
#
#     def rm_card(self):
#         if len(self.cards) == 0:
#             return
#         return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.board = Board(grid=[100,100], max_x=4, max_y=5, active_x=2, active_y=3)

        self.board.procedural_generate_v2()


class Game:
    def __init__(
            self,
            starting_cards: int = 3,
    ):
        name1 = input("p1 name ")
        name2 = input("p2 name ")
        self.p1 = Player(name1)
        self.p2 = Player(name2)


        self.deck = Deck()

        for x in range(starting_cards):
            self.p1.hand.add_card(self.deck.draw())
        # print(self.p1.hand.print_cards())
        # print(self.p2.hand.print_cards())

        for x in range(starting_cards):
            self.p2.hand.add_card(self.deck.draw())
        # print(self.p1.hand.print_cards())
        # print(self.p2.hand.print_cards())

    # def wins(self, winner):
    #     w = "{} wins this round"
    #     w = w.format(winner)
    #     print(w)
    #
    # def draw(self, p1n, p1c, p2n, p2c):
    #     d = "{} drew {} {} drew {}"
    #     d = d.format(p1n,
    #                  p1c,
    #                  p2n,
    #                  p2c)
    #     print(d)

    def play_game(self):
        print("here's ya card info:")
        startup = True
        while 1 > 0:
            if startup:
                print(f"{self.p1.name}'s hand:\n"
                      f"{self.p1.hand.print_card_names()}")
                self.p1.board.print_board(short=True)
                startup = False
            # print(f"{self.p2.name}'s hand:\n"
            #       f"{self.p2.hand.print_card_names()}")
            # self.p2.board.print_board(short=True)
            m = "1 to select grid, q to quit: "
            res = input(m)
            if res == 'q':
                break
            if res == '1':
                x = int(input(f"choose x-coord (0 - {len(self.p1.board.grid)}): "))
                y = int(input(f"choose y-coord (0 - {len(self.p1.board.grid[0])}): "))
                self.p1.board.select_grid(x, y)
                self.p1.board.print_selected_board(short=True)
            else:
                print("that's not an option!")
        #     p1c = self.deck.rm_card()
        #     p2c = self.deck.rm_card()
        #     p1n = self.p1.name
        #     p2n = self.p2.name
        #     self.draw(p1n,
        #               p1c,
        #               p2n,
        #               p2c)
        #     if p1c > p2c:
        #         self.p1.wins += 1
        #         self.wins(self.p1.name)
        #     else:
        #         self.p2.wins += 1
        #         self.wins(self.p2.name)
        #
        # win = self.winner(self.p1,
        #                  self.p2)
        print(f"{card.name} has passed away.")

    # def winner(self, p1, p2):
    #     if p1.wins > p2.wins:
    #         return p1.name
    #     if p1.wins < p2.wins:
    #         return p2.name
    #     return "It was a tie!"

game = Game()
game.play_game()
