import file_utils as fu

LENGTH_JOLT_NUMBER = 12


def read_file(fname):
    input_lines = fu.read_file(fname)
    return [[int(c) for c in line] for line in input_lines]


def extract_max(inputs: list[int]) -> int:
    choices = 12
    start_pos = 0
    length_inputs = len(inputs)
    result = []
    while choices > 0:
        end_pos = length_inputs - choices + 1
        current_max = max(inputs[start_pos:end_pos])
        result.append(current_max)
        start_pos = inputs.index(current_max, start_pos) + 1
        choices -= 1
    return int("".join(map(str, result)))


def part1(fname):
    result = []
    for line in read_file(fname):
        first_digit = max(line[:-1])
        second_digit = max(line[line.index(first_digit) + 1 :])
        result.append(first_digit * 10 + second_digit)
    return sum(result)


def part2(fname):
    return sum([extract_max([int(c) for c in line]) for line in read_file(fname)])


if __name__ == "__main__":
    print(part1("day03.txt"))
    print(part2("day03.txt"))
