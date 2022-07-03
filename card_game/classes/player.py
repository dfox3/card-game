from .board import Board
from.globals import MAP
from .hand import Hand

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.board = Board(grid=[MAP[0],MAP[1]], max_x=4, max_y=5, active_x=2, active_y=3)
        self.board.procedural_generate_v2()
