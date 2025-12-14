class Dial:
    def __init__(self, instructions: list[str]) -> None:
        self.instructions = instructions

    def part1(self) -> int:
        self.position = 50
        self.score = 0
        for instruction in self.instructions:
            direction, steps = instruction[0], int(instruction[1:])
            self.position = (
                self.position + steps * (1 if direction == "R" else -1)
            ) % 100
            self.score += 1 if self.position == 0 else 0
        return self.score

    def part2(self) -> int:
        self.score = 0
        self.position = 50
        for instruction in self.instructions:
            direction, steps = instruction[0], int(instruction[1:])
            for _ in range(steps):
                self.position = self.position + (1 if direction == "R" else -1)
                self.score += 1 if self.position % 100 == 0 else 0
            self.position %= 100
        return self.score


def read_data(fname: str) -> list[str]:
    with open(fname, "r") as f:
        lines = [line.strip() for line in f]
    return lines


if __name__ == "__main__":
    lines = read_data("data/day01.txt")
    dial = Dial(lines)
    part1 = dial.part1()
    print(part1)
    part2 = dial.part2()
    print(part2)
