"""Super fun and Awesome Number Guessing Game"""

__author__ = "730676224"


def guess_a_number() -> None:
    secret = 7
    x = int(input("Guess a number: "))
    print("Your guess was", x)
    if x == secret:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is", secret)
    else:  # x > secret:
        print("Your guess was too high! The secret number is", secret)
    return None


if __name__ == "__main__":
    guess_a_number()
