def less_than_10(num: int) -> None:
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small Number")
    else:
        print("Big Number")
    print("Have a Nice day!")


less_than_10(num=5)
