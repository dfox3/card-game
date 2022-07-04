import pygame

from actions import (
    _confirm_map_menu_logic,
    _brawl_logic,
    _macro_logic,
    _main_menu_logic,
    _map_choice_logic,
    _menu_logic,
    _shop_logic,
    _title_logic,
)
from classes.deck import Deck
from classes.globals import BIT, MAP
from classes.player import Player
from phases import *


pygame.init()
DISPLAY_W, DISPLAY_H = MAP[1]*BIT, MAP[0]*BIT
canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
running = True
clock = pygame.time.Clock()


class Game:
    def __init__(
            self,
            starting_cards: int = 3,
    ):
        name1 = "gus"
        name2 = "betty"
        self.p1 = Player(name1)
        self.p2 = Player(name2)

        self.phase = Phases.TITLE
        self.load_phases()
        self.screen = self.PHASES[self.phase]["screen"]

        self.deck = Deck()

        for x in range(starting_cards):
            self.p1.hand.add_card(self.deck.draw())

        for x in range(starting_cards):
            self.p2.hand.add_card(self.deck.draw())

    def load_phases(self):
        self.PHASES = {
            Phases.BRAWL: {
                "action": _brawl_logic,
                "screen": Brawl(canvas, window, self.p1)
            },
            Phases.CONFIRM_MAP_MENU: {
                "action": _confirm_map_menu_logic,
                "screen": ConfirmMapMenu(canvas, window, self.p1)
            },
            Phases.MACRO: {
                "action": _macro_logic,
                "screen": Macro(canvas, window, self.p1)
            },
            Phases.MAIN_MENU: {
                "action": _main_menu_logic,
                "screen": MainMenu(canvas, window, self.p1)
            },
            Phases.MAP_CHOICE: {
                "action":_map_choice_logic,
                "screen": MapChoice(canvas, window, self.p1)
            },
            Phases.MENU: {
                "action": _menu_logic,
                "screen": Menu(canvas, window, self.p1)
            },
            Phases.SHOP: {
                "action": _shop_logic,
                "screen": Shop(canvas, window, self.p1)
            },
            Phases.TITLE: {
                "action": _title_logic,
                "screen": Title(canvas, window)
            },
        }

    def play_game(self):
        running = True
        while running:
            # better go catch it
            new_phase = self.PHASES[self.phase]["action"](
                player=self.p1,
                screen=self.PHASES[self.phase]["screen"],
            )
            if new_phase:
                self.phase = new_phase
                self.screen = self.PHASES[self.phase]["screen"]
            pygame.display.update()

game = Game()
game.play_game()
