from collections import defaultdict
import file_utils as fu

SPLITTER = "^"
FREE = "."
BEAM = "|"
DEBUG = True


def read_file(fname):
    all_lines = [[c for c in line] for line in fu.read_file(fname)]
    start = [(0, col) for col, val in enumerate(all_lines[0]) if val == "S"][0]
    return start, all_lines


def part1(fname):
    start, all_lines = read_file(fname)
    splits = 0
    row, col = start
    all_lines[row][col] = "|"
    row += 1
    while row < len(all_lines):
        for col in range(len(all_lines[row])):
            if all_lines[row][col] == SPLITTER and all_lines[row - 1][col] == BEAM:
                splits += 1
                if all_lines[row][col - 1] == FREE:
                    all_lines[row][col - 1] = BEAM
                if all_lines[row][col + 1] == FREE:
                    all_lines[row][col + 1] = BEAM
            elif all_lines[row][col] == FREE and all_lines[row - 1][col] == BEAM:
                all_lines[row][col] = BEAM
        if DEBUG:
            print(f"\nAfter processing row {row}: splits={splits}")
            print("\n".join("".join(line) for line in all_lines))
        row += 1
    return splits


def part2(fname):
    start, grid = read_file(fname)
    rows = len(grid)
    cols = len(grid[0])
    r0, c0 = start

    from collections import defaultdict

    counts = defaultdict(int)
    counts[c0] = 1

    for r in range(r0 + 1, rows):
        new_counts = defaultdict(int)
        for c, cnt in list(counts.items()):
            if cnt == 0:
                continue
            # ensure column in range
            if c < 0 or c >= cols:
                continue
            ch = grid[r][c]
            if ch == SPLITTER:
                # split to left and right positions in this same row if free
                if c - 1 >= 0 and grid[r][c - 1] == FREE:
                    new_counts[c - 1] += cnt
                if c + 1 < cols and grid[r][c + 1] == FREE:
                    new_counts[c + 1] += cnt
            elif ch == FREE:
                new_counts[c] += cnt
            # other characters (S, etc.) are ignored for movement
        counts = new_counts

    return sum(counts.values())


if __name__ == "__main__":
    print("Part 1:", part1("day07.txt"))
    print("Part 2:", part2("day07.txt"))
