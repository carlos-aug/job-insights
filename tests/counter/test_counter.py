from src.pre_built.counter import count_ocurrences


def test_counter():
    path = 'data/jobs.csv'
    word = 'Python'
    assert count_ocurrences(path, word) == 1639
