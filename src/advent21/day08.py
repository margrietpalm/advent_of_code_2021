import numpy as np

from advent21.helpers import DataOpener


def load_input():
    inputs = []
    with DataOpener('day08.txt') as f:
        for line in f.readlines():
            inputs += line.split(' | ')[1].strip('\n').split(' ')
    return inputs


def run():
    # lengths of segments with unique lengths (1, 4, 7, 8)
    req_lens = [2, 4, 3, 7]
    lens = [len(item) for item in load_input()]
    return np.sum(np.isin(lens, req_lens))
