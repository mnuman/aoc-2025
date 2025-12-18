import file_utils as fu


def read_file(fname):
    fresh_ingredients = []
    ingredients = []
    for line in fu.read_file(fname):
        if line.strip():
            if "-" in line:
                fresh_ingredients.append(tuple(map(int, line.split("-"))))
            else:
                ingredients.append(int(line))
    return fresh_ingredients, ingredients


def part1(fname):
    fresh_ingredients, ingredients = read_file(fname)
    return sum(
        1 if any(low <= ing <= high for (low, high) in fresh_ingredients) else 0
        for ing in ingredients
    )


def part2(fname):
    fresh_ingredients, _ = read_file(fname)
    merged = []
    # operate on sorted intervals to merge overlapping ones
    for current in sorted(fresh_ingredients, key=lambda x: x[0]):
        # if no overlap, add new interval
        if not merged or merged[-1][1] < current[0] - 1:
            merged.append(current)
        else:
            # merge overlapping intervals
            merged[-1] = (merged[-1][0], max(merged[-1][1], current[1]))
    total_covered = sum(high - low + 1 for (low, high) in merged)
    return total_covered


if __name__ == "__main__":
    print("Part 1:", part1("day05.txt"))
    print("Part 2:", part2("day05.txt"))
