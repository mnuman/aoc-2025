import file_utils as fu


def read_file(fname):
    return [tuple(map(int, line.split(","))) for line in fu.read_file(fname)]


def area(p1, p2):
    return (1 + abs(p1[0] - p2[0])) * (1 + abs(p1[1] - p2[1]))


def part1(fname):
    points = read_file(fname)
    max_area = None
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points[i + 1 :], start=i + 1):
            a = area(p1, p2)
            if max_area is None or a > max_area:
                max_area = a
    return max_area


if __name__ == "__main__":
    fname = "day09.txt"
    result = part1(fname)
    print(f"Result for {fname}: {result}")
