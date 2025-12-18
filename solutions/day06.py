from functools import reduce
from operator import add, mul
import file_utils as fu


def read_file(fname):
    all_lines = fu.read_file(fname)
    data_lines, operation_lines = all_lines[:-1], all_lines[-1]
    data = [[int(trim(c)) for c in line.split()] for line in data_lines]
    operations = [trim(c) for c in operation_lines.split()]
    return data, operations


def read_file_part2(fname):
    all_lines = fu.read_raw_file(fname).splitlines()
    data_lines, operation_lines = all_lines[:-1], all_lines[-1]
    ops = [c for c in operation_lines if c != " "]
    col = 0
    parsed = []
    operations = []
    for op in ops:
        assert op in ("*", "+")
        operands = []
        while col < len(data_lines[0]):
            operand = "".join(data_lines[row][col] for row in range(len(data_lines)))
            col += 1
            if trim(operand):
                operands.append(int(trim(operand)))
            else:
                break
        parsed.append(operands)
        operations.append(mul if op == "*" else add)
    return operations, parsed


def trim(s):
    return s.lstrip().rstrip()


def part1(fname):
    data, operations = read_file(fname)
    result = 0
    for idx, op in enumerate(operations):
        operation = mul if op == "*" else add
        result += reduce(operation, (dataline[idx] for dataline in data))
    # Implement the logic for part 1 here
    return result


def part2(fname):
    operations, operands = read_file_part2(fname)
    result = 0
    for idx, operation in enumerate(operations):
        result += reduce(operation, operands[idx])
    return result


if __name__ == "__main__":
    fname = "day06.txt"
    print("Part 1:", part1(fname))
    print("Part 2:", part2(fname))
