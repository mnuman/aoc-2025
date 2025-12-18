import day06


def test_read_file():
    data, operations = day06.read_file("test_day06.txt")
    assert len(data) == 3
    assert len(operations) == 4


def test_part1():
    result = day06.part1("test_day06.txt")
    assert result == 4277556
