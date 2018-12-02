"""
Advent of Code day 1 solution.

Test suite for solution of day 1.
"""
import freq


def test_input_1_part1():
    expected = 3
    stimuli = [1, 1, 1]

    result = freq.calculate_part1(stimuli)

    assert expected == result


def test_input_2_part1():
    expected = 0
    stimuli = [1, 1, -2]

    result = freq.calculate_part1(stimuli)

    assert expected == result


def test_input_3_part1():
    expected = -6
    stimuli = [-1, -2, -3]

    result = freq.calculate_part1(stimuli)

    assert expected == result


def test_input_1_part2():
    expected = 0
    stimuli = [1, -1]

    result = freq.calculate_part2(stimuli)

    assert expected == result


def test_input_2_part2():
    expected = 10
    stimuli = [3, 3, 4, -2, -4]

    result = freq.calculate_part2(stimuli)

    assert expected == result


def test_input_3_part2():
    expected = 5
    stimuli = [-6, 3, 8, 5, -6]

    result = freq.calculate_part2(stimuli)

    assert expected == result


def test_input_4_part2():
    expected = 14
    stimuli = [7, 7, -2, -7, -4]

    result = freq.calculate_part2(stimuli)

    assert expected == result
