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


def part1(fname):
    results = []
    ranges = read_data(fname)
    for lo, hi in ranges:
        results.extend(invalid(lo, hi))
    return sum(results)


if __name__ == "__main__":
    print(part1("data/day02.txt"))
