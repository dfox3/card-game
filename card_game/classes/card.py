from typing import List

from .exceptions import CardTypeException
from .presets import TYPES
from .type import Type


class Card:

    def __init__(
            self,
            name: str = "dummy",
            attack: int = 0,
            hp: int = 0,
            types: List[Type] = [],
            skills: list = [],
            game_state: str = "Out",
            round_state: str = "Alive",
            board_position: int = -1,
            priority: int = -1,
    ):
        self.name = name
        self.attack = attack
        self.hp = hp
        self.max_hp = hp
        if self._validate_types(types):
            self.types = types
        self.skills = skills
        self.game_state = game_state
        self.round_state = round_state
        self.board_position = board_position
        self.priority = priority

    def _validate_types(
            self,
            types
    ):
        for type in types:
            if type.name not in TYPES:
                raise CardTypeException("Type name is not in valid TYPES - check presets.py")
        return True


    def hurt(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            self.round_state = "Dead"


    def heal(self, heal_val: int):
        self.hp = self.max_hp if self.hp + heal_val > self.max_hp else self.hp + heal_val


