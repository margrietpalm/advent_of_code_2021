import numpy as np
import pathlib

from advent21.helpers import DataOpener


class Card:

    def __init__(self, grid: np.ndarray):
        self.grid = grid
        self.result = np.zeros_like(grid, dtype=int)
        self.winner = False

    def __repr__(self):
        return str(self.grid)

    def cross(self, number):
        self.result[self.grid == number] = 1
        if self._is_winner():
            self.winner = True

    def _is_winner(self) -> bool:
        return np.any(np.sum(self.result, axis=0) == self.grid.shape[0]) or \
               np.any(np.sum(self.result, axis=1) == self.grid.shape[1])


class Bingo:

    def __init__(self, cards: list[Card]):
        self.cards = cards
        self.finished = False
        self.winners = []
        self.winning_number = None

    def draw(self, number):
        for card in self.cards:
            card.cross(number)
        self._update_winners()
        if self.finished:
            self.winning_number = number

    def _update_winners(self):
        self.winners = [card for card in self.cards if card.winner]
        if len(self.winners) > 0:
            self.finished = True


def get_cards():
    with DataOpener('day4_boards.txt') as f:
        text = f.read()
        blocks = text.split('\n\n')
    return [Card(np.reshape(np.fromstring(block, sep=" ", dtype=int), newshape=(5, 5))) for block in blocks]


def run():
    cards = get_cards()
    game = Bingo(cards)
    numbers = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
    for number in numbers:
        game.draw(number)
        if game.finished:
            break
    try:
        assert game.finished
    except AssertionError:
        raise Exception('Wrong answer')
    try:
        assert len(game.winners) == 1
    except AssertionError:
        raise Exception('Wrong answer')
    winner = game.winners[0]
    return game.winning_number * np.sum(winner.grid[winner.result == 0])

