import day07


def test_read_file():
    start, all_lines = day07.read_file("test_day07.txt")
    assert start == (0, 7)
    assert len(all_lines) == 16


def test_part1():
    result = day07.part1("test_day07.txt")
    assert result == 21
