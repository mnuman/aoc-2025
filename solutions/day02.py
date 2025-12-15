import re

# repeat pattern: a number starting with non-zero digit followed by any number of digits
# repeating at least one (so two occurrences) and the repeats fit the string exactly.
PATTERN = re.compile(r"^([1-9]\d*)\1+$")


def read_data(fname: str):
    with open(fname, "r") as f:
        input_line = f.readlines()
    return [
        (lo, hi)
        for pair in input_line[0].split(",")
        for lo, hi in [map(int, pair.split("-"))]
    ]


def is_repeated(n: int) -> bool:
    s = str(n)
    l = len(s)
    return l % 2 == 0 and s[: l // 2] == s[l // 2 :]


def invalid(lo, hi):
    return [num for num in range(lo, hi + 1) if is_repeated(num)]


def invalid_repeats(lo, hi):
    return [num for num in range(lo, hi + 1) if PATTERN.match(str(num))]


def part1(fname):
    results = []
    ranges = read_data(fname)
    for lo, hi in ranges:
        results.extend(invalid(lo, hi))
    return sum(results)


def part2(fname):
    results = []
    ranges = read_data(fname)
    for lo, hi in ranges:
        results.extend(invalid_repeats(lo, hi))
    return sum(results)


if __name__ == "__main__":
    print(part1("data/day02.txt"))
    print(part2("data/day02.txt"))
