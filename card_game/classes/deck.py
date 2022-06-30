import random

from .card import Card
from .globals import TYPES
from .presets.cards import CARDS

class Deck:
    def __init__(
            self,
            number: int = 100,
    ):
        self.number = number
        self.current_number = number
        self.cards = self.shuffle()

    def shuffle(self):
        return [ self._make_card(random.choice(list(CARDS.values()))) for n in range(self.number) ]

    def _make_card(self, card_info):
        return Card(
            name=card_info["name"],
            hp=card_info["hp"],
            attack=card_info["attack"],
            types=[ TYPES[t] for t in card_info["types"] ]
        )

    def remove_card(self, card):
        self.cards.remove(card)
        self.current_number -= 1
        if self.current_number == 0:
            self.shuffle()

    def draw(self):
        card = self.cards[0]
        self.remove_card(card)
        return card
