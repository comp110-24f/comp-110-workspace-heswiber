"""Mimic Function Challenge"""

__author__ = "730676224"


def mimic(message: str) -> str:
    """Mimics the message given to the program"""
    return message


def main() -> None:
    """Prints the message given by user"""
    return print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
