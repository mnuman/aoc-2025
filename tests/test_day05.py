import day05


def test_read_file():
    fresh_ingredients, ingredients = day05.read_file("test_day05.txt")
    assert len(fresh_ingredients) == 4
    assert (3, 5) in fresh_ingredients
    assert len(ingredients) == 6
    assert 32 in ingredients


def test_part1():
    result = day05.part1("test_day05.txt")
    assert result == 3


def test_part2():
    result = day05.part2("test_day05.txt")
    assert result == 14
