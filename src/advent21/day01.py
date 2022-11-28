import numpy as np

def run() -> int:
    sequence = np.array([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
    return np.sum((sequence[1:] - sequence[0:-1]) > 0)
