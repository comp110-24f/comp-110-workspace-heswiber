from random import randint

# print(randint(1, 7))


# function definition
#          parameters\/
def sum(num1: int, num2: int) -> int:
    """return the sum of num1 and num2"""
    return num1 + num2


def cringe(num3: int, num4: int) -> int:
    """divides num3 by num4"""
    return num3 / num4


# function call
print(sum(num1=2, num2=13))  # <- arguments

print(cringe(num3=255, num4=16))
