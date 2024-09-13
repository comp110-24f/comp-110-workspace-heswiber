import random


def angry() -> int:
    return random.randint(0, 10)


if angry() <= 5:
    print("your mom")
