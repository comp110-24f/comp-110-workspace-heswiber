"""Chardle, totally not a wordle ripoff..."""

__author__ = "730676224"


def input_word() -> str:
    # function for defining the input word, makes sure it is only 5 letters
    chosen_word = input("Enter a 5-character word:")
    if len(chosen_word) != 5:
        # instead of an if statement for if the length was 5, an if statment for if
        # length wasnt 5 works better cause you can isolate failed attemps
        print("Error: Word must contain 5 characters.")
        exit()
        # stops the program when bad input is given
    # print(chosen_word)
    return chosen_word


def input_letter() -> str:
    # function for defining the input letter, makes sure it is only one character
    chosen_letter = input("Enter a single character: ")
    if len(chosen_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
        # stops program when bad input is given
    # print(chosen_letter)
    return chosen_letter


def contains_char(chosen_word: str, chosen_letter: str) -> None:
    number_matching = 0
    print("Searching for", chosen_letter, "in", chosen_word)
    # manually going through each letter because dont know how to loop

    if chosen_word[0] == chosen_letter:
        print(chosen_letter, "found at index", 0)
        number_matching = number_matching + 1
        # doing number_matching+1 makes it so if a letter is matching, count increases
        # increasing [num] by one steps though each letter of the chosen_word
    if chosen_word[1] == chosen_letter:
        print(chosen_letter, "found at index", 1)
        number_matching = number_matching + 1
    if chosen_word[2] == chosen_letter:
        print(chosen_letter, "found at index", 2)
        number_matching = number_matching + 1
    if chosen_word[3] == chosen_letter:
        print(chosen_letter, "found at index", 3)
        number_matching = number_matching + 1
    if chosen_word[4] == chosen_letter:
        print(chosen_letter, "found at index", 4)
        number_matching = number_matching + 1

    if number_matching == 0:
        print("No instances of", chosen_letter, "found in", chosen_word)
        # if there is none of the chosen letter in the word this is printed

    elif number_matching == 1:
        print("1 instance of", chosen_letter, "found in", chosen_word)
        # if there is only one of the chose letter in the word this is printed
    else:
        print(number_matching, "instances of", chosen_letter, "found in", chosen_word)
        # if there are more than one of the chosen letter in the word, this is printed


def main() -> None:
    contains_char(chosen_word=input_word(), chosen_letter=input_letter())


# the function that takes everything previously created and uses it in one function
# makes it so you dont have to set everything to something to run the program,
# can just input the input values and it should run

if __name__ == "__main__":
    main()
