"""
Advent of code day 1 solution.

Given a list of integers, calculates the end frequency.
"""
def calculate_part1(steps: list) -> int():
    """
    Calculates the final frequency by accounting for each frequency step in steps.

    steps = list(int)
    """
    return sum(steps)


def calculate_part2(steps: list) -> int():
    """
    Returns the first frequency step that is reached twice.
    """
    freq_history = set()
    freq = 0
    while True:
        for step in steps:
            freq_history.add(freq)
            freq += step
            if freq in freq_history:
                return freq



if __name__ == '__main__':
    steps = []
    with open('input.txt', 'r') as instructions:
        for line in instructions:
            steps.append(int(line))

    print(calculate_part1(steps))
    print(calculate_part2(steps))
