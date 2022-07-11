import numpy as np
import random
from typing import List

from .card import Card
from .globals import ELEVATIONS, NATURAL_RAMP, PG_1, SHORT_ENV, MAX_DIMENSIONS, STARTING_ACTIVE_SPACES

class Board:

    def __init__(
            self,
            grid: List[int] = [3,4],
            probs: List[dict] = PG_1,
            max_x: int = MAX_DIMENSIONS["x"],
            max_y: int = MAX_DIMENSIONS["x"],
            active_x: int = STARTING_ACTIVE_SPACES["x"],
            active_y: int = STARTING_ACTIVE_SPACES["y"],
    ):
        self.grid = np.reshape(np.array([ [ Space() for col in range(grid[1]) ] for row in range(grid[0]) ]), grid)
        self.probs = probs
        self.pg_positions = { p["name"]: i for i, p in enumerate(self.probs) }
        self.seed_environment = random.choice(self.probs)
        self.selected_grid = None
        self.selected_spaces = []
        self.active_spaces = []
        self.max_x = max_x
        self.max_y = max_y
        self.active_x = active_x
        self.active_y = active_y
        self.select_grid()


    def select_grid(
            self,
            x: int = 0,
            y: int = 0,
    ):
        # logic to handle edges
        if x > len(self.grid) - self.max_x:
            xs = [ len(self.grid) - self.max_x + i for i in range(self.max_x) ]
            x = len(self.grid) - self.max_x
        elif x < 0:
            xs = [ i for i in range(self.max_x) ]
            x = 0
        else:
            xs = [ x + i for i in range(self.max_x) ]
        if y > len(self.grid[0]) - self.max_y:
            ys = [ len(self.grid[0]) - self.max_y + i for i in range(self.max_y) ]
            y = len(self.grid[0]) - self.max_y
        elif y < 0:
            ys = [ i for i in range(self.max_y) ]
            y = 0
        else:
            ys = [ y + i for i in range(self.max_y) ]
        # build selected grid
        grid = [self.max_x, self.max_y]
        self.selected_grid = np.reshape(np.array([ [ self.grid[xs[row], ys[col]] for col in range(grid[1]) ] for row in range(grid[0]) ]), grid)
        # build selected spaces
        self.selected_spaces = []
        for xx in xs:
            for yy in ys:
                self.selected_spaces.append([xx, yy])
        # build active part of selected grid
        self.active_spaces = []
        starting_active_x = x + (self.max_x - self.active_x) // 2
        starting_active_y = y + (self.max_y - self.active_y) // 2
        for active_x in range(self.active_x):
            for active_y in range(self.active_y):
                self.activate_space(starting_active_x + active_x, starting_active_y + active_y)

    def move_selection(self, direction):
        if direction == "left":
            self.select_grid(self.selected_spaces[0][0], self.selected_spaces[0][1] - 1)
        if direction == "right":
            self.select_grid(self.selected_spaces[0][0], self.selected_spaces[0][1] + 1)
        if direction == "up":
            self.select_grid(self.selected_spaces[0][0] - 1, self.selected_spaces[0][1])
        if direction == "down":
            self.select_grid(self.selected_spaces[0][0] + 1, self.selected_spaces[0][1])


    def get_tiles(self):
        return [ [ space.environment for space in row ] for row in self.grid ]


    def get_selected_spaces(self):
        return [ [ space for space in row ] for row in self.selected_grid ]


    def activate_space(self, x, y):
        self.active_spaces.append([x, y])

    def reorder_space(self, x, y, pos):
        self.active_spaces.insert(pos-1, self.active_spaces.pop(self.active_spaces.index([x, y])))


    def procedural_generate_v1(
            self,
    ):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                if x == 0 and y == 0:
                    self.grid[x, y].set_environment(self._generate_environment_from_seed())
                elif x == 0:
                    self.grid[x, y].set_environment(self._generate_random_environment_one_parent(x, y-1))
                elif y == 0:
                    self.grid[x, y].set_environment(self._generate_random_environment_one_parent(x-1, y))
                else:
                    self.grid[x, y].set_environment(self._generate_random_environment_multi_parents([[x-1, y], [x, y-1]]))



    def procedural_generate_v2(
            self,
    ):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                if x == 0 and y == 0:
                    self.grid[x, y].set_environment(self._generate_environment_from_seed())
                elif x == 0:
                    self.grid[x, y].set_environment(self._generate_random_environment_one_parent(x, y-1))
                elif y == 0:
                    self.grid[x, y].set_environment(self._generate_random_environment_one_parent(x-1, y))
                elif y == len(self.grid[0]) - 1:
                    self.grid[x, y].set_environment(self._generate_random_environment_multi_parents([[x-1, y], [x, y-1], [x-1, y-1]]))
                else:
                    self.grid[x, y].set_environment(self._generate_random_environment_multi_parents([[x-1, y], [x-1, y-1], [x-1, y+1]]))

    def _get_prob(self, x, y):
        return self.probs[self.pg_positions[self.grid[x, y].environment]]["prob"]

    def _get_space_prob(self, x, y):
        return self.probs[self.pg_positions[self.grid[x, y].environment]]["prob"]

    def _generate_random_environment_one_parent(self, x, y):
        return self.probs[np.random.choice(np.arange(0, len(self.probs)), p=self._get_prob(x, y))]["name"]

    def _generate_random_environment_multi_parents(self, parent_coords):
        probs_list = [ self._get_space_prob(p[0], p[1]) for p in parent_coords ]
        average_prob = self._averaged_probs(probs_list)
        return self.probs[np.random.choice(np.arange(0, len(self.probs)), p=average_prob)]["name"]

    def _generate_environment_from_seed(self):
        return self.probs[np.random.choice(np.arange(0, len(self.probs)), p=self.seed_environment["prob"])]["name"]

    def _averaged_probs(
            self,
            probs_list: List[list] = []
    ):
        combined_probs = [ sum([ p[x] for p in probs_list ]) for x in range(len(probs_list[0])) ]
        sum_probs = sum(combined_probs)
        return [ c / sum_probs for c in combined_probs ]

    def print_board(self, short=False):
        to_print = ""
        for row in self.grid:
            for cell in row:
                to_print += f"{SHORT_ENV[cell.environment]} " if short else f"{cell.environment}\t"
            to_print += f"\n"
        print(to_print)

    def print_selected_board(self, short=False):
        to_print = ""
        for x, row in enumerate(self.selected_grid):
            for y, cell in enumerate(row):
                c = f"{SHORT_ENV[cell.environment]}" if short else f"{cell.environment}"
                to_print += c + "! " if [x, y] in self.active_spaces else c + "  "

            to_print += f"\n"
        print(to_print)







class Space:

    def __init__(
            self,
            card: Card = None,
            environment: str = "water"
    ):
        self.card = card
        self.environment = None
        self.elevation = None
        self.ramp = None
        self.set_environment(environment)

    def set_environment(self, environment):
        self.environment = environment
        self.elevation = self._generate_elevation()
        self.ramp = self.set_ramp() if self.environment in NATURAL_RAMP else self.set_ramp(on=False)

    def set_ramp(self, on=True):
        self.ramp = on

    def _generate_elevation(self):
        options = ELEVATIONS[self.environment]
        index = random.randint(0, len(options) - 1)
        return options[index]

