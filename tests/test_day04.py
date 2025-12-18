import day04


def test_read_file():
    paper_rolls = day04.read_file("test_day04.txt")
    for r in [(0, 2), (0, 3), (0, 5), (9, 0), (9, 8)]:
        assert r in paper_rolls


def test_part1():
    assert day04.part1("test_day04.txt") == 13
