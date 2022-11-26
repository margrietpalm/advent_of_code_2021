import abc
import numpy as np
from typing import Tuple, List
from advent21.helpers import DataOpener


class Line(abc.ABC):

    def __init__(self, start: np.ndarray, stop: np.ndarray):
        assert start.shape == (2,)
        assert stop.shape == (2,)
        self.start = start
        self.stop = stop

    def __repr__(self) -> str:
        return f'Line from {self.start} to {self.stop}'

    @abc.abstractmethod
    def get_points(self) -> np.ndarray:
        ...


class HorizontalLine(Line):

    def get_points(self) -> np.ndarray:
        left = np.min([self.start[0], self.stop[0]])
        right = np.max([self.start[0], self.stop[0]])
        return np.array([[x, self.start[1]] for x in np.arange(left, right + 1)])


class VerticalLine(Line):

    def get_points(self) -> np.ndarray:
        top = np.min([self.start[1], self.stop[1]])
        bottom = np.max([self.start[1], self.stop[1]])
        return np.array([[self.start[0], y] for y in np.arange(top, bottom + 1)])


class Ocean:

    def __init__(self, size: Tuple[int, int]):
        self.map = np.zeros(shape=size, dtype=int)

    def project_line(self, line: Line):
        idx = line.get_points()
        self.map[idx[:, 0], idx[:, 1]] += 1


def load_lines() -> List[Line]:
    with DataOpener('day5_lines.txt') as f:
        lines: List[Line] = []
        for line in f.readlines():
            pt1, pt2 = (np.fromstring(item, sep=',', dtype=int) for item in line.strip('\n').split(' -> '))
            if pt1[1] == pt2[1]:
                lines.append(HorizontalLine(pt1, pt2))
            elif pt1[0] == pt2[0]:
                lines.append(VerticalLine(pt1, pt2))
        return lines


def run():
    lines = load_lines()
    ocean = Ocean(size=(10, 10))
    for line in lines:
        ocean.project_line(line)
    return np.bincount(ocean.map.flatten())[2]
