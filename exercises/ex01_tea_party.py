"""Tea Party Logistics Calculator"""

__author__ = "730676224"


def main_planner(guests: int) -> None:
    """How many guests are attending the tea party and displaying the data"""

    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))

    # Needed to convert the functions into str so
    # that they could be added to the print string.
    # Might be a tad overcrowded but it works


def tea_bags(people: int) -> int:
    """How many teabags are needed for the party based on people attending"""
    return people * 2

    # Since each person will be drinking 2 tea, then simple multiplication by 2 will do


def treats(people: int) -> int:
    """How many sweat treats the guests will need based on attendence"""
    return int(tea_bags(people=people) * 1.5)

    # Had to make the people parameter of the tea_bag function
    # equal to the people parameter of the treats function.
    # And then had to multiply that by 1.5, and turn it into an int


def cost(tea_count: int, treat_count: int) -> float:
    """How much the tea party is going to cost, tea bag = $.50 and a treat = $.75"""
    return float((tea_count * 0.50) + (treat_count * 0.75))

    # Since the parameters are defined, whatever number/function is
    # in the area is either tea_count or treat_count; cost(tea_count, treat_count).
    # Price of tea is $.50, all we needed to do is multiply the total tea by 0.50.
    # Price of treats is $.75, all we needed to do was multiply the total treats by .75.


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
