import day03


def test_part1():
    assert day03.part1("test_day03.txt") == 357


def test_extract_max():
    assert day03.extract_max([int(c) for c in "234234234234278"]) == 434234234278
