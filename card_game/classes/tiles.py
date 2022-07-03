import random

import pygame

from .presets.tilesets import ASSET_PATH, BOARD_TILES, DUMMY_TILE, TITLE_TILE


class DummyScreen():
    def __init__(self, image=f"{ASSET_PATH}/{DUMMY_TILE}"):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, (0, 0))

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        # Manual load in: self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class TileMap():
    def __init__(self, tiles, tileset=BOARD_TILES):
        self.tile_size = 16
        self.start_x, self.start_y = 0, 0
        self.tileset = tileset
        self.tiles = self.load_tiles(tiles)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()

    def draw(self, surface):
        surface.blit(self.map_surface, (0, 0))

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)

    def load_tiles(self, tiles):
        ret_tiles = []
        for y, row in enumerate(tiles):
            for x, tile in enumerate(row):
               ret_tiles.append(Tile(f"{ASSET_PATH}/{random.choice(self.tileset[tile])}", x * self.tile_size, y * self.tile_size))
            # Store the size of the tile map
        print("tiles")
        self.map_w, self.map_h = len(tiles[0]) * self.tile_size, len(tiles) * self.tile_size
        print(self.map_w)
        print(self.map_h)
        return ret_tiles


class TileSelector():
    def __init__(self, selected_grid, tile_size=16):
        self.selected_grid = selected_grid
        self.tile_size = tile_size

    def draw(self, surface, color, border=False):
        # fill rect
        x_fill = (self.selected_grid[0][1] * self.tile_size)
        y_fill = (self.selected_grid[0][0] * self.tile_size)
        w_fill = ((self.selected_grid[-1][1] - self.selected_grid[0][1] + 1) * self.tile_size)
        h_fill = ((self.selected_grid[-1][0] - self.selected_grid[0][0] + 1) * self.tile_size)
        fill = pygame.Rect(x_fill, y_fill, w_fill, h_fill)
        self.draw_rect_alpha(surface, (255,255,255,20), fill)

        for cell in self.selected_grid:
            x_out = cell[1] * self.tile_size
            y_out = cell[0] * self.tile_size
            x_in = cell[1] * self.tile_size + 1
            y_in = cell[0] * self.tile_size + 1
            selected_tile_out = pygame.Rect(x_out, y_out, self.tile_size, self.tile_size)
            selected_tile_in = pygame.Rect(x_in, y_in, self.tile_size - 1 - 1, self.tile_size - 1 - 1)
            self.draw_rect_alpha(surface, (255,255,255,100), selected_tile_out, width=1)
            self.draw_rect_alpha(surface, color, selected_tile_in, width=1)
        # border for all cells
        if border:
            x_border = (self.selected_grid[0][1] * self.tile_size) - 1
            y_border = (self.selected_grid[0][0] * self.tile_size) - 1
            w_border = ((self.selected_grid[-1][1] - self.selected_grid[0][1] + 1) * self.tile_size) + 1 + 1
            h_border = ((self.selected_grid[-1][0] - self.selected_grid[0][0] + 1) * self.tile_size) + 1 + 1
            border = pygame.Rect(x_border, y_border, w_border, h_border)
            self.draw_rect_alpha(surface, (255,255,255), border, width=1)
            x_border = (self.selected_grid[0][1] * self.tile_size) - 1 - 2
            y_border = (self.selected_grid[0][0] * self.tile_size) - 1 - 2
            w_border = ((self.selected_grid[-1][1] - self.selected_grid[0][1] + 1) * self.tile_size) + 1 + 1 + 2 + 2
            h_border = ((self.selected_grid[-1][0] - self.selected_grid[0][0] + 1) * self.tile_size) + 1 + 1 + 2 + 2
            border = pygame.Rect(x_border, y_border, w_border, h_border)
            self.draw_rect_alpha(surface, (0,0,0), border, width=2)

    def draw_rect_alpha(self, surface, color, rect, width=None):
        shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        if width:
            pygame.draw.rect(shape_surf, color, shape_surf.get_rect(), width)
        else:
            pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
        surface.blit(shape_surf, rect)

class TitleScreen():
    def __init__(self, image=f"{ASSET_PATH}/{TITLE_TILE}"):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, (0, 0))

