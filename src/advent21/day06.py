from typing import Optional
from dataclasses import dataclass


@dataclass
class Fish:
    timer: int

    def step(self):
        self.timer -= 1

    def procreate(self):
        if self.timer < 0:
            self.timer = 6
            return Fish(timer=8)


class Population:

    def __init__(self, init_ages):
        self.fish = [Fish(timer=init_age) for init_age in init_ages]

    def run(self, steps):
        for step in range(steps):
            for fish in self.fish:
                fish.step()
            self.fish += [offspring for fish in self.fish if (offspring := fish.procreate()) is not None]

    @property
    def size(self):
        return len(self.fish)


def run():
    population = Population(init_ages=[3, 4, 3, 1, 2])
    population.run(80)
    return population.size
