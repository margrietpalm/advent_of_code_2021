import numpy as np

from advent21.helpers import DataOpener


def load_input() -> np.ndarray:
    data = []
    with DataOpener('day09.txt') as f:
        for line in f.readlines():
            data.append([int(char) for char in line.strip('\n')])
    return np.array(data)


def run():
    map = load_input()
    # check left and right
    pad_col = np.ones((map.shape[0], 1), dtype=bool)
    lower_than_left = (map[:, 1:] - map[:, 0:-1]) < 0
    lower_than_right = (map[:, 0:-1] - map[:, 1:]) < 0
    combined_left_right = np.column_stack((pad_col, lower_than_left)) & np.column_stack((lower_than_right, pad_col))
    # check top and bottom
    pad_row = np.ones((1, map.shape[1]), dtype=bool)
    lower_than_upper = (map[1:, :] - map[0:-1, :]) < 0
    lower_than_lower = (map[0:-1, :] - map[1:, :]) < 0
    combined_upper_lower = np.row_stack((pad_row, lower_than_upper)) & np.row_stack((lower_than_lower, pad_row))
    # combine all
    minimum_map = combined_left_right & combined_upper_lower
    return np.sum(map[minimum_map] + 1)
