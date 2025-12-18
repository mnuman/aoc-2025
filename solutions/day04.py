import file_utils as fu


def read_file(fname) -> set[tuple[int, int]]:
    grid_positions = set()
    input_lines = fu.read_file(fname)
    for r, row in enumerate(input_lines):
        for c, val in enumerate(row):
            if val == "@":
                grid_positions.add((r, c))
    return grid_positions


def count_neighbours(positions: set[tuple[int, int]], pos: tuple[int, int]) -> int:
    r, c = pos
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    return sum([1 if (r + dr, c + dc) in positions else 0 for dr, dc in deltas])


def part1(fname) -> int:
    positions = read_file(fname)
    return sum([1 for pos in positions if count_neighbours(positions, pos) < 4])


def part2(fname) -> int:
    positions = read_file(fname)
    removed = 0
    while True:
        to_remove = {pos for pos in positions if count_neighbours(positions, pos) < 4}
        if not to_remove:
            break
        positions.difference_update(to_remove)
        removed += len(to_remove)
    return removed


if __name__ == "__main__":
    print(f"Part 1: {part1("day04.txt")}")
    print(f"Part 2: {part2("day04.txt")}")
