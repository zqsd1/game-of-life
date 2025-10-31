from GameOfLife.terminal import is_alive
import pytest


@pytest.fixture
def set_default():
    alive = 1
    dead = 0
    return alive, dead


def test_is_dead():
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert not is_alive(1, 1, matrix)
    matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    assert not is_alive(1, 1, matrix)
    matrix = [[1, 1, 1], [0, 1, 1], [1, 0, 1]]
    assert not is_alive(1, 1, matrix)


def test_is_alive():
    matrix = [[0, 1, 0], [0, 0, 1], [0, 0, 1]]
    assert is_alive(1, 1, matrix)
    matrix = [[0, 1, 0], [0, 1, 1], [0, 0, 1]]
    assert is_alive(1, 1, matrix)
