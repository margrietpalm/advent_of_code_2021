import json
import importlib
import pytest
from pathlib import Path

@pytest.fixture(scope="module")
def solutions():
    with open(Path(__file__).parent.resolve().joinpath('solutions.json')) as f:
        data = json.load(f)
    return data


@pytest.mark.parametrize('day', tuple([f'day{i:02d}' for i in range(1, 26)]))
def test_day(day: int, solutions: dict):
    try:
        day_module = importlib.import_module(f'advent21.{day}')
    except ModuleNotFoundError:
        pytest.skip("not yet implemented")
    assert day_module.run() == int(solutions[day])
