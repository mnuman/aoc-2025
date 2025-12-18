from operator import add, mul
import day06


def test_read_file():
    data, operations = day06.read_file("test_day06.txt")
    assert len(data) == 3
    assert len(operations) == 4


def test_part1():
    result = day06.part1("test_day06.txt")
    assert result == 4277556


def test_read_file_part2():
    ops, operands = day06.read_file_part2("test_day06.txt")
    assert ops == [mul, add, mul, add]
    assert len(operands) == len(ops)
    assert operands[0] == [1, 24, 356]


def test_part2():
    result = day06.part2("test_day06.txt")
    assert result == 3263827
