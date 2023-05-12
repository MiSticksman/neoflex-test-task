from task.zeros_mover import move_zeros


def test_move_zeros_func():
    assert move_zeros([1, 0, 1, 2, 0, 1, 3]) == [1, 1, 2, 1, 3, 0, 0]
    assert move_zeros([1, 7, 3, 0, 2, 1]) == [1, 7, 3, 2, 1, 0]
    assert move_zeros([0, 0, 8, 0, 2]) == [8, 2, 0, 0, 0]
    assert move_zeros([5, 0, 0, 3, 0, 1, 3]) == [5, 3, 1, 3, 0, 0, 0]
    assert move_zeros([1, 7, 3, 2, 1]) == [1, 7, 3, 2, 1]
    assert move_zeros([]) == []
