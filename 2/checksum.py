"""
Solver for Advent of Code day 2.

String checksum calculator.
"""
import jellyfish
import difflib


def count(candidate: str) -> tuple:
    """
    counts if there are any double or triple occurances of a char in the given string.
    returns a tuple of if there are any doubles or triples.
    """
    doubles = 0
    triples = 0
    for char in candidate:
        if doubles == 0 and candidate.count(char) == 2:
            doubles = 1
        elif triples == 0 and candidate.count(char) == 3:
            triples = 1

        if doubles == 1 and triples == 1:
            return (1,1)
    return (doubles, triples)


def calculate(data: list) -> int:
    """
    Given a list of strings, calculates a checksum.
    """
    doubles = 0
    triples = 0
    for string in data:
        (dub, trip) = count(string)
        doubles += dub
        triples += trip
    return doubles * triples


def calc2(data: list) -> str:
    """
    mash the strings
    """
    data = [s for s in data]
    (s1, s2) = find_pair(data)
    s = ''
    for part in difflib.ndiff(s1, s2):
        if '+' not in part and '-' not in part:
            s += part.strip()
    return s


def find_pair(data: list) -> tuple:
    """
    Given a list of strings, returns two that match except for one char.
    """
    for idx, line in enumerate(data):
        for line2 in data[(idx+1):]:
            if jellyfish.levenshtein_distance(line, line2) == 1:
                return (line, line2)
        

if __name__ == '__main__':
    with open('input.txt', 'r') as infile:
        print(calc2(infile))
