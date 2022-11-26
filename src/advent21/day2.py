import numpy as np

class Submarine:

    def __init__(self):
        self.pos = np.array([0,0], dtype=int)

    def forward(self, value: int):
        self.pos[0] += value

    def down(self, value: int):
        self.pos[1] += value

    def up(self, value: int):
        self.pos[1] -= value


def run_program(submarine: Submarine, programm: list[str]):
    for step in programm:
        action, value = step.split(' ')
        getattr(submarine, action)(int(value))


def run():
    programm = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    sub = Submarine()
    run_program(sub, programm)
    return np.prod(sub.pos)