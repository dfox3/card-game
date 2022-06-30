from typing import List

from .card import Card

class Hand:
    def __init__(
            self,
            cards: List[Card] = None,
    ):
        if cards is None:
            cards = []
        self.cards = cards

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def print_cards(self):
        ret_str = ""
        for c, card in enumerate(self.cards):
            ret_str += f"{c+1}:\n{card.to_print()}\n"
        return ret_str
