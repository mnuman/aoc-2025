import day02


def test_isrepeated():
    assert day02.is_repeated(1212)
    assert not day02.is_repeated(1234)
    assert not day02.is_repeated(101)


def test_invalid():
    assert day02.invalid(1200, 1230) == [1212]
    assert day02.invalid(1000, 1115) == [1010, 1111]


def test_part1():
    assert day02.part1("data/test_day02.txt") == 1227775554


def test_invalid_repeats():
    assert day02.invalid_repeats(1200, 1230) == [1212]
    assert day02.invalid_repeats(1000, 1115) == [1010, 1111]
    assert day02.invalid_repeats(1234, 1300) == []


def test_part2():
    assert day02.part2("data/test_day02.txt") == 4174379265
