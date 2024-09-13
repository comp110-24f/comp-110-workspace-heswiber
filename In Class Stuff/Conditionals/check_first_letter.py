def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "Match!"
    else:
        return "No Match!"


print(check_first_letter(word="Happy", letter="H"))
