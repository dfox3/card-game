import sys

import pygame

from classes.board import Board
from classes.deck import Deck
from classes.hand import Hand
from classes.tiles import TileMap, TileSelector


################################# LOAD UP A BASIC WINDOW AND CLOCK #################################
MAP = [40, 50]

pygame.init()
DISPLAY_W, DISPLAY_H = MAP[1]*16, MAP[0]*16
canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
running = True
clock = pygame.time.Clock()




class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.board = Board(grid=[MAP[0],MAP[1]], max_x=4, max_y=5, active_x=2, active_y=3)

        self.board.procedural_generate_v2()


class Game:
    def __init__(
            self,
            starting_cards: int = 3,
    ):
        name1 = "gus"
        name2 = "betty"
        self.p1 = Player(name1)
        self.p2 = Player(name2)

        #################################### LOAD THE LEVEL #######################################

        self.map = TileMap(self.p1.board.get_tiles())
        self.p1.board.select_grid()
        print(self.p1.board.selected_spaces)
        self.selector = TileSelector(self.p1.board.selected_spaces)
        self.active_selector = TileSelector(self.p1.board.active_spaces)
        print(len(self.p1.board.get_tiles()))
        print(len(self.p1.board.get_tiles()[0]))
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

                canvas.fill((0, 0, 0))  # Fills the entire screen with light blue
                self.map.draw_map(canvas)
                self.selector.draw(canvas, pygame.Color(255,225,255,20), border=True)
                self.active_selector.draw(canvas, pygame.Color(255,0,255,100))
                window.blit(canvas, (0, 0))

                pygame.display.update()
            #     print(f"{self.p1.name}'s hand:\n"
            #           f"{self.p1.hand.print_card_names()}")
            #     self.p1.board.print_board(short=True)
                startup = False
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

                    if event.key == pygame.K_LEFT:
                        self.p1.board.move_selection("left")
                    if event.key == pygame.K_RIGHT:
                        self.p1.board.move_selection("right")
                    if event.key == pygame.K_UP:
                        self.p1.board.move_selection("up")
                    if event.key == pygame.K_DOWN:
                        self.p1.board.move_selection("down")
                canvas.fill((0, 0, 0))  # Fills the entire screen with light blue
                self.map.draw_map(canvas)
                self.selector = TileSelector(self.p1.board.selected_spaces)
                self.active_selector = TileSelector(self.p1.board.active_spaces)
                self.selector.draw(canvas, pygame.Color(255,225,255,20), border=True)
                self.active_selector.draw(canvas, pygame.Color(255,0,255,100))
                window.blit(canvas, (0, 0))
                pygame.display.update()

                    #window.blit(canvas, (0, 0))
            # # print(f"{self.p2.name}'s hand:\n"
            # #       f"{self.p2.hand.print_card_names()}")
            # # self.p2.board.print_board(short=True)
            # m = "1 to select grid, q to quit: "
            # res = input(m)
            # if res == 'q':
            #     break
            # if res == '1':
            #     x = int(input(f"choose x-coord (0 - {len(self.p1.board.grid)}): "))
            #     y = int(input(f"choose y-coord (0 - {len(self.p1.board.grid[0])}): "))
            #     self.p1.board.select_grid(x, y)
            #     self.p1.board.print_selected_board(short=True)
            # else:
            #     print("that's not an option!")

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
        # print(f"{card.name} has passed away.")

    # def winner(self, p1, p2):
    #     if p1.wins > p2.wins:
    #         return p1.name
    #     if p1.wins < p2.wins:
    #         return p2.name
    #     return "It was a tie!"

game = Game()
game.play_game()
