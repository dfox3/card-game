import numpy as np
import random
from typing import List

from .card import Card
from .globals import PG_1

class Board:

    def __init__(
            self,
            grid: List[int] = [3,4],
            probs: List[dict] = PG_1,
    ):
        self.grid = np.reshape(np.array([ [ Space() for col in range(grid[1]) ] for row in range(grid[0]) ]), grid)
        self.probs = probs
        self.pg_positions = { p["name"]: i for i, p in enumerate(self.probs) }
        self.seed_environment = random.choice(self.probs)

    def procedural_generate_1(
            self,
    ):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                if x == 0 and y == 0:
                    self.grid[x, y].environment = self._generate_environment_from_seed()
                elif x == 0:
                    self.grid[x, y].environment = self._generate_random_environment_one_parent(x, y-1)
                elif y == 0:
                    self.grid[x, y].environment = self._generate_random_environment_one_parent(x-1, y)
                else:
                    self.grid[x, y].environment = self._generate_random_environment_two_parents([x-1, y], [x, y-1])

    def _get_prob(self, x, y):
        return self.probs[self.pg_positions[self.grid[x, y].environment]]["prob"]

    def _get_space_prob(self, x, y):
        return self.probs[self.pg_positions[self.grid[x, y].environment]]["prob"]

    def _generate_random_environment_one_parent(self, x, y):
        return self.probs[np.random.choice(np.arange(0, len(self.probs)), p=self._get_prob(x, y))]["name"]

    def _generate_random_environment_two_parents(self, p1, p2):
        p1_prob = self._get_space_prob(p1[0], p1[1])
        p2_prob = self._get_space_prob(p2[0], p2[1])
        average_prob = self._averaged_probs(p1_prob, p2_prob)
        return self.probs[np.random.choice(np.arange(0, len(self.probs)), p=average_prob)]["name"]

    def _generate_environment_from_seed(self):
        return self.probs[np.random.choice(np.arange(0, len(self.probs)), p=self.seed_environment["prob"])]["name"]

    def _averaged_probs(
            self,
            p1_prob: List[float] = [],
            p2_prob: List[float] = [],
    ):
        combined_probs = [ p1_prob[x] + p2_prob[x] for x in range(len(p1_prob)) ]
        sum_probs = sum(combined_probs)
        return [ c / sum_probs for c in combined_probs ]

    def print_board(self):
        to_print = ""
        for row in self.grid:
            for cell in row:
                to_print += f"{cell.environment}\t"
            to_print += f"\n"
        print(to_print)







class Space:

    def __init__(
            self,
            card: Card = None,
            environment: str = None,
            elevation: int = 0,
            ramp: bool = False,
    ):
        self.card = card
        self.environment = environment
        self.elevation = elevation
        self.ramp = ramp
