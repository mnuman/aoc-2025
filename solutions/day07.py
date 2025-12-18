import file_utils as fu

SPLITTER = "^"
FREE = "."
BEAM = "|"
DEBUG = False


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


if __name__ == "__main__":
    print("Part 1:", part1("day07.txt"))
