import day01


def test_part1():
    lines = day01.read_data("data/test_day01.txt")
    dial = day01.Dial(lines)
    assert dial.part1() == 3


def test_part2():
    lines = day01.read_data("data/test_day01.txt")
    dial = day01.Dial(lines)
    assert dial.part2() == 6
