"""While Loops Challenge Question"""

__author__ = "730676224"


def num_instances(phrase: str, search_char: str) -> int:
    count = 0
    index = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count = count + 1
        index = index + 1
    return count
