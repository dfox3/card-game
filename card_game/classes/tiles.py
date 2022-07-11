import random

from PIL import Image
import pygame

from .button import Button
from .globals import BIG_BITS, BITS, Screen
from .presets.colors import Colors
from .presets.tilesets import *


class DummyScreen():
    def __init__(self, image=f"{ASSET_PATH}/{DUMMY_TILE}"):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, (0, 0))

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, bits=BITS, grey=False, dimensions=None):
        pygame.sprite.Sprite.__init__(self)
        self.dimensions = dimensions if dimensions else (bits, bits)
        self.color_image = pygame.image.load(image)
        self.grey_image = self._pil_to_surface(self._grey(image))
        self.image = pygame.transform.scale(self.color_image, self.dimensions)
        # Manual load in: self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.grey = grey
        self.original_color = grey

    def draw(self, surface):
        self._refresh()
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def _refresh(self):
        self.image = self._p_image(self.grey_image) if self.grey else self._p_image(self.color_image)

    def _p_image(self, image):
        return pygame.transform.scale(image, self.dimensions)


    def _grey(self, image_file):
        img = Image.open(image_file).convert('P', palette=Image.ADAPTIVE, colors=4).convert('L').convert("RGB")
        return img

    def _pil_to_surface(self, pil_image):
        return pygame.image.fromstring(pil_image.tobytes(), pil_image.size, pil_image.mode).convert()

class MacroTile(Tile):

    def check_for_input(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def change_color(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.grey = False
        else:
            self.grey = self.original_color

# WIP
class CardTile(Tile):
    def __init__(self, image, x, y, bits=BITS, highlighted=False, highlighted_img=None, grey=False, dimensions=None):
        self.highlighted = highlighted
        self.original_highlight = highlighted
        self.img = image
        self.highlighted_img = highlighted_img
        self.h_img = self.highlighted_img if (self.highlighted_img and self.highlighted) else self.img
        print(self.h_img)
        super().__init__(self.h_img, x, y, bits=bits, grey=grey, dimensions=dimensions)


    def check_for_input(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def change_color(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.highlighted = True
        else:
            self.highlighted = self.original_highlight


    def _refresh(self):
        print(self.h_img)
        self.image = self._p_image(pygame.image.load(self.h_img))



class TileMap():
    def __init__(self, tiles, tileset=BOARD_TILES):
        self.tile_size = BITS
        self.start_x, self.start_y = 0, 0
        self.tileset = tileset
        self.tiles = self.load_tiles(tiles)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        #self.map_surface.set_colorkey(Colors.DARK_RED)
        self.map_surface.fill(Colors.GREEN)
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
                tile_type = TYPES[tile]
                if PRIORITY[tile_type] > 1:
                    # build lower trans layers
                    layer_type = "grass"
                    lowest = self.tileset["water"]["water-0-water-1-water-2-water-3"][0]
                    ret_tiles.append(Tile(f"{ASSET_PATH}/{lowest}", x * self.tile_size, y * self.tile_size))
                    while layer_type != tile_type:
                        if layer_type not in EXEMPT:
                            tile_paths = self._get_tiles_from_neighbors(tiles, x, y, current_tile_type=layer_type, lower_layer=True)
                            if tile_paths:
                                index = random.randint(0, len(tile_paths) - 1)
                                ret_tiles.append(
                                    Tile(f"{ASSET_PATH}/{tile_paths[index]}", x * self.tile_size, y * self.tile_size))
                            layer_type = NEXT_LAYER[layer_type]
                if tile_type in EXEMPT:
                    index = random.randint(0, len(self.tileset[tile])-1)
                    ret_tiles.append(Tile(f"{ASSET_PATH}/{self.tileset[tile][index]}", x * self.tile_size, y * self.tile_size))
                    # Store the size of the tile map
                else:
                    tile_paths = self._get_tiles_from_neighbors(tiles, x, y)
                    index = random.randint(0, len(tile_paths)-1)
                    ret_tiles.append(Tile(f"{ASSET_PATH}/{tile_paths[index]}", x * self.tile_size,y * self.tile_size))
        self.map_w, self.map_h = len(tiles[0]) * self.tile_size, len(tiles) * self.tile_size
        return ret_tiles

    def _get_tiles_from_neighbors(self, tiles, x, y, current_tile_type=None, lower_layer=False):
        tile_key = ""
        if not current_tile_type:
            current_tile_type = TYPES[tiles[y][x]]
        bools = [y == 0, x == len(tiles[0]) - 1, y == len(tiles) - 1, x == 0]
        xy_adjust = [(-1,0), (0,1), (1,0), (0,-1)]

        if current_tile_type != "trans":
            for i, b in enumerate(bools):
                if b:
                    tile_key += f"{current_tile_type}-{i}-"
                else:
                    neighbor_type = TYPES[tiles[y+xy_adjust[i][0]][x+xy_adjust[i][1]]]
                    if PRIORITY[neighbor_type] < PRIORITY[current_tile_type]:
                        if neighbor_type == "water":
                            tile_key += f"water-{i}-"
                        else:
                            tile_key += f"trans-{i}-"
                    elif lower_layer and neighbor_type == "trans" and current_tile_type != "grass":
                        tile_key += f"trans-{i}-"
                    else:
                        tile_key += f"{current_tile_type}-{i}-"

            tile_key = tile_key[:-1]
        elif lower_layer:
            return None
        else:
            tile_key = "trans-0-trans-1-trans-2-trans-3"
        if lower_layer:
            if current_tile_type not in tile_key:
                return None
            else:
                return self.tileset[current_tile_type][tile_key]
        else:
            try:
                return self.tileset[tiles[y][x]][tile_key]
            except:
                import pdb
                pdb.set_trace()


class MacroScreen():
    def __init__(self, spaces, selected_spaces, active_spaces, tileset=BIG_BOARD_TILES, scale=None):
        TOTAL_ELEVATIONS = 3

        self.mouse = pygame.mouse
        self.total_elevations = TOTAL_ELEVATIONS
        self.spaces = spaces
        self.tile_size = int(BIG_BITS * scale if scale else BIG_BITS)
        self.margin = int((scale * self.tile_size) / 3 if scale else self.tile_size / 3)
        self.sub_margin = int((self.margin / TOTAL_ELEVATIONS) / 1.25)
        self.start_x, self.start_y = 0, 0
        self.tileset = tileset
        self.local_coordinates = self._coordinate_localizer(selected_spaces)
        self.active_spaces = self._localize_active_spaces(active_spaces)
        self.tiles = self.load_tiles(
            [ [ space.environment for space in row ] for row in self.spaces ],
            [ [ space.elevation for space in row ] for row in self.spaces ],
        )
        self.map_surface = pygame.Surface((Screen.WIDTH, Screen.HEIGHT))
        #self.map_surface.set_colorkey(Colors.DARK_RED)
        self.load_map()


    def draw(self, surface):
        self.load_map()
        #center_rect = self.map_surface.get_rect(center=(Screen.WIDTH // 2, Screen.HEIGHT // 2 - 100))
        surface.blit(self.map_surface, (0,0))

    def load_map(self):
        self.map_surface.fill(Colors.PURPLE)
        mouse_pos = self.check_mouse()
        for tile in self.tiles:
            if type(tile) in [ MacroTile, CardTile ]:
                tile.change_color(mouse_pos)
            tile.draw(self.map_surface)

    def load_tiles(self, tiles, elevations):
        ret_tiles = []
        for y, row in enumerate(tiles):
            for x, tile in enumerate(row):
                ret_tiles += self._load_tile_elevations(elevations, x, y)
                is_grey = False if f"{y},{x}" in self.active_spaces else True
                ret_tiles.append(
                    MacroTile(
                        f"{ASSET_PATH}/{self.tileset[tile]}",
                        self.margin + (x * self.margin) + (x * self.tile_size),
                        self.margin + (y * self.margin) + (y * self.tile_size) + \
                        (self.sub_margin * (self.total_elevations - elevations[y][x])),
                        bits=self.tile_size,
                        grey=is_grey
                    )
                )
        board_w = self.margin + (len(tiles[0]) * self.margin) + (len(tiles[0]) * self.tile_size)
        board_h = self.margin + (len(tiles) * self.margin) + (len(tiles) * self.tile_size)
        ret_tiles += self._load_deck(y=board_h)
        self.map_w, self.map_h = board_w, board_h + self.margin + self.tile_size*2
        return ret_tiles

    def _load_tile_elevations(self, elevations, x, y):
        ret_list = []
        elevation = elevations[y][x]
        for e in range(elevation):
            ret_list.append(
                Tile(
                    f"{ASSET_PATH}/board/big_board/25percent_shade.png",
                    self.margin + (x * self.margin) + (x * self.tile_size),
                    self.margin + (y * self.margin) + (y * self.tile_size) + (self.sub_margin * (self.total_elevations - e)),
                    bits=self.tile_size
                )
            )
        return ret_list


    def _load_deck(self, deck=None, y=0):
        ret_list = []
        deck = deck if deck else ["missingno" for i in range(6)]
        for i, card in enumerate(deck):
            ret_list.append(CardTile(
                f"{ASSET_PATH}/cards/templates/basic_card.png",
                self.margin + (i * self.margin / 2) + (i * self.tile_size),
                self.margin + y,
                highlighted=False,
                highlighted_img=f"{ASSET_PATH}/cards/templates/selected_card.png",
                dimensions=(self.tile_size, int(self.tile_size * 1.5)),

            ))
            ret_list.append(Tile(
                f"{ASSET_PATH}/cards/sprites/{card}.png",
                self.margin + (i * self.margin / 2) + (i * self.tile_size) + (self.tile_size / 2) - (BITS / 2),
                self.margin + y + (self.tile_size / 2) - (BITS / 2),
                dimensions=(BITS, BITS),

            ))
        return ret_list

    def _coordinate_localizer(self, selected_spaces):
        xs = []
        ys = []
        ret_dict = {"x": {}, "y": {}}

        for s in selected_spaces:
            xs.append(s[0])
            ys.append(s[1])
        for x in range(max(xs) - min(xs)):
            ret_dict["x"][min(xs) + x] = x
        for y in range(max(ys) - min(ys)):
            ret_dict["y"][min(ys) + y] = y
        return ret_dict

    def _localize_active_spaces(self, active_spaces):
        return { f"{self.local_coordinates['x'][a[0]]},{self.local_coordinates['y'][a[1]]}" for a in active_spaces }


    def check_mouse(self):
        return self.mouse.get_pos()



class TileSelector():
    def __init__(self, selected_grid, tile_size=BITS):
        self.selected_grid = selected_grid
        self.tile_size = tile_size

    def draw(self, surface, color, border=False):
        # fill rect
        x_fill = (self.selected_grid[0][1] * self.tile_size)
        y_fill = (self.selected_grid[0][0] * self.tile_size)
        w_fill = ((self.selected_grid[-1][1] - self.selected_grid[0][1] + 1) * self.tile_size)
        h_fill = ((self.selected_grid[-1][0] - self.selected_grid[0][0] + 1) * self.tile_size)
        fill = pygame.Rect(x_fill, y_fill, w_fill, h_fill)
        self.draw_rect_alpha(surface, Colors.WHITE + (20,), fill)

        for cell in self.selected_grid:
            x_out = cell[1] * self.tile_size
            y_out = cell[0] * self.tile_size
            x_in = cell[1] * self.tile_size + 1
            y_in = cell[0] * self.tile_size + 1
            selected_tile_out = pygame.Rect(x_out, y_out, self.tile_size, self.tile_size)
            selected_tile_in = pygame.Rect(x_in, y_in, self.tile_size - 1 - 1, self.tile_size - 1 - 1)
            self.draw_rect_alpha(surface, Colors.WHITE + (100,), selected_tile_out, width=1)
            self.draw_rect_alpha(surface, color, selected_tile_in, width=1)
        # border for all cells
        if border:
            x_border = (self.selected_grid[0][1] * self.tile_size) - 1
            y_border = (self.selected_grid[0][0] * self.tile_size) - 1
            w_border = ((self.selected_grid[-1][1] - self.selected_grid[0][1] + 1) * self.tile_size) + 1 + 1
            h_border = ((self.selected_grid[-1][0] - self.selected_grid[0][0] + 1) * self.tile_size) + 1 + 1
            border = pygame.Rect(x_border, y_border, w_border, h_border)
            self.draw_rect_alpha(surface, Colors.WHITE, border, width=1)
            x_border = (self.selected_grid[0][1] * self.tile_size) - 1 - 2
            y_border = (self.selected_grid[0][0] * self.tile_size) - 1 - 2
            w_border = ((self.selected_grid[-1][1] - self.selected_grid[0][1] + 1) * self.tile_size) + 1 + 1 + 2 + 2
            h_border = ((self.selected_grid[-1][0] - self.selected_grid[0][0] + 1) * self.tile_size) + 1 + 1 + 2 + 2
            border = pygame.Rect(x_border, y_border, w_border, h_border)
            self.draw_rect_alpha(surface, Colors.BLACK, border, width=2)

    def draw_rect_alpha(self, surface, color, rect, width=None):
        shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        if width:
            pygame.draw.rect(shape_surf, color, shape_surf.get_rect(), width)
        else:
            pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
        surface.blit(shape_surf, rect)

class TitleScreen():
    def __init__(self, image=f"{ASSET_PATH}/{TITLE_TILE}"):
        self.image = pygame.transform.scale(pygame.image.load(image), (Screen.WIDTH, Screen.HEIGHT))
        self.rect = self.image.get_rect()
        self.mouse = pygame.mouse
        self.start_button = Button(
            image=None,
            pos=(Screen.WIDTH // 2, Screen.HEIGHT // 2 + 100),
            text_input="Start",
            font=_get_font(30),
            base_color=Colors.WHITE,
            hovering_color=Colors.GREEN
        )
        self.quit_button = Button(
            image=None,
            pos=(Screen.WIDTH // 2, Screen.HEIGHT // 2 + 150),
            text_input="Quit",
            font=_get_font(20),
            base_color=Colors.WHITE,
            hovering_color=Colors.RED
        )

    def draw(self, surface):
        surface.blit(self.image, (0, 0))
        mouse_pos = self.check_mouse()
        title_text = _get_font(45).render("Fantastic FOLLIES!!!", True, "White")
        title_rect = title_text.get_rect(center=(Screen.WIDTH // 2, Screen.HEIGHT // 2 - 100))
        surface.blit(title_text, title_rect)
        self.start_button.change_color(mouse_pos)
        self.start_button.update(surface)
        self.quit_button.change_color(mouse_pos)
        self.quit_button.update(surface)

    def check_mouse(self):
        return self.mouse.get_pos()



def _get_font(size):
    return pygame.font.Font("classes/assets/font.ttf", size)
