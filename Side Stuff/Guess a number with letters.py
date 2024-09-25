"""Super fun and Awesome Number Guessing Game"""

__author__ = "730676224"


def guess_a_number() -> None:
    secret = int(7)
    x = input("Guess a number: ")
    print("Your guess was " + x)
    if x.isalpha():
        print("That's not a number!")
    else:
        if int(x) == secret:
            print("You got it!")
        if int(x) < secret:
            print("Your guess was too low! The secret number is " + str(secret))
        if int(x) > secret:
            print("Your guess was too high! The secret number is " + str(secret))

    return None


guess_a_number()
