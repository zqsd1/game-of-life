from game_of_life.matrix import is_alive, create_matrix, rebuild_matrix


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


def test_build_matrix():
    matrix = create_matrix(rows=5, columns=10)
    assert len(matrix) == 5
    assert len(matrix[0]) == 10


def test_rebuild_matrix():
    matrix = [[False, True, False], [False, True, False], [False, True, False]]
    matrix = rebuild_matrix(matrix)
    matrix = rebuild_matrix(matrix)
    assert matrix == [[0, 1, 0], [0, 1, 0], [0, 1, 0]]


def test_block_form():
    matrix = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    matrix = rebuild_matrix(matrix)
    matrix = rebuild_matrix(matrix)
    assert matrix == [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]


def test_tube_form():
    start_matrix = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    matrix = rebuild_matrix(start_matrix)
    matrix = rebuild_matrix(matrix)
    assert start_matrix == matrix


def test_long_barge_form():
    start_matrix = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    matrix = rebuild_matrix(start_matrix)
    matrix = rebuild_matrix(matrix)
    assert start_matrix == matrix
