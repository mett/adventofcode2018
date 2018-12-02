"""
Advent of code day 2.

Test suite for day 2 solution.
"""
import checksum


def test_example_1():
    expected = (0, 0)
    stimuli = 'abcdef'

    result = checksum.count(stimuli)

    assert expected == result


def test_example_2():
    expected = (1, 1)
    stimuli = 'bababc'

    result = checksum.count(stimuli)

    assert expected == result


def test_example_3():
    expected = (1, 0)
    stimuli = 'abbcde'

    result = checksum.count(stimuli)

    assert expected == result


def test_example_4():
    expected = (0, 1)
    stimuli = 'abcccd'

    result = checksum.count(stimuli)

    assert expected == result


def test_example_5():
    expected = (1, 0)
    stimuli = 'aabcdd'

    result = checksum.count(stimuli)

    assert expected == result


def test_example_6():
    expected = (1, 0)
    stimuli = 'abcdee'

    result = checksum.count(stimuli)

    assert expected == result


def test_example_7():
    expected = (0, 1)
    stimuli = 'ababab'

    result = checksum.count(stimuli)

    assert expected == result

def test_full_example():
    expected = 12
    stimuli = ['ababab', 'abcdee', 'aabcdd', 'abbcde',
               'bababc', 'abcdef', 'abcccd']

    result = checksum.calculate(stimuli)

    assert expected == result
