import enum
import sys
sys.path.append('..')

import pygame

from classes.presets.colors import Colors
from classes.tiles import DummyScreen, MacroScreen, TileMap, TileSelector, TitleScreen

class Phases(enum.Enum):
    BRAWL = "brawl"
    CONFIRM_MAP_MENU = "confirm_map_menu"
    MACRO = "macro"
    MAIN_MENU = "main_menu"
    MAP_CHOICE = "map_choice"
    MENU = "menu"
    SHOP = "shop"
    TITLE = "title"


class Brawl:
    def __init__(self, canvas, window, player):
        self.canvas = canvas
        self.window = window
        self.player = player

        self.dummy = DummyScreen()

    def draw(self):
        self.canvas.fill((0, 0, 0))
        self.dummy.draw(self.canvas)
        self.window.blit(self.canvas, (0, 0))


class ConfirmMapMenu:
    def __init__(self, canvas, window, player):
        self.canvas = canvas
        self.window = window
        self.player = player

        self.dummy = DummyScreen()

    def draw(self):
        self.canvas.fill((0, 0, 0))
        self.dummy.draw(self.canvas)
        self.window.blit(self.canvas, (0, 0))


class Macro:
    def __init__(self, canvas, window, player):
        self.canvas = canvas
        self.window = window
        self.player = player

        self.macro = MacroScreen(
            self.player.board.get_selected_spaces(),
            self.player.board.selected_spaces,
            self.player.board.active_spaces,
            scale=.85
        )

    def draw(self):
        self.canvas.fill((0, 0, 0))
        self.macro.draw(self.canvas)
        self.window.blit(self.canvas, (0, 0))



class MainMenu:
    def __init__(self, canvas, window, player):
        self.canvas = canvas
        self.window = window
        self.player = player

        self.dummy = DummyScreen()

    def draw(self):
        self.canvas.fill((0, 0, 0))
        self.dummy.draw(self.canvas)
        self.window.blit(self.canvas, (0, 0))

class MapChoice:
    def __init__(self, canvas, window, player):
        self.canvas = canvas
        self.window = window
        self.player = player

        self.map = TileMap(self.player.board.get_tiles())
        self.player.board.select_grid()
        self.selector = TileSelector(self.player.board.selected_spaces)
        self.active_selector = TileSelector(self.player.board.active_spaces)

    def draw(self):
        self.canvas.fill((0, 0, 0))  # Fills the entire screen with light blue
        self.map.draw(self.canvas)
        self.selector = TileSelector(self.player.board.selected_spaces)
        self.active_selector = TileSelector(self.player.board.active_spaces)
        self.selector.draw(self.canvas, pygame.Color(Colors.WHITE + (20,)), border=True)
        self.active_selector.draw(self.canvas, pygame.Color(Colors.PINK))
        self.window.blit(self.canvas, (0, 0))


class Menu:
    def __init__(self, canvas, window, player):
        self.canvas = canvas
        self.window = window
        self.player = player

        self.dummy = DummyScreen()

    def draw(self):
        self.canvas.fill((0, 0, 0))
        self.dummy.draw(self.canvas)
        self.window.blit(self.canvas, (0, 0))


class Shop:
    def __init__(self, canvas, window, player):
        self.canvas = canvas
        self.window = window
        self.player = player

        self.dummy = DummyScreen()

    def draw(self):
        self.canvas.fill((0, 0, 0))
        self.dummy.draw(self.canvas)
        self.window.blit(self.canvas, (0, 0))


class Title:
    def __init__(self, canvas, window):
        self.canvas = canvas
        self.window = window
        self.title = TitleScreen()

    def draw(self):
        self.canvas.fill((0, 0, 0))
        self.title.draw(self.canvas)
        self.window.blit(self.canvas, (0, 0))
