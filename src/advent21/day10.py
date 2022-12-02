from typing import List, Optional

from advent21.helpers import DataOpener


def load_input() -> List[List[str]]:
    with DataOpener('day10.txt') as f:
        return [list(line.strip('\n')) for line in f.readlines()]


def check_line(line) -> Optional[int]:
    openers = '([{<'
    closers = ')]}>'
    passed = []
    while len(line) > 0:
        current = line.pop(0)
        if current in openers:
            passed.append(current)
        if current in closers:
            idx = closers.index(current)
            if passed[-1] == openers[idx]:
                del passed[-1]
            else:
                return current
    return None


def run():
    lines = load_input()
    score_chart = {')': 3, ']': 57, '}': 1197, '>': 25137}
    corrupt = [check_line(line) for line in lines]
    corrupt_s = ''.join([item for item in corrupt if item is not None])
    scores = [corrupt_s.count(char) * score for char, score in score_chart.items()]
    return sum(scores)
