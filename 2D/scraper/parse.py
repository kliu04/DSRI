import sys
import pyperclip


def parse(raw: str) -> str:
    """Parses an equation from Katie's website
    (https://people.math.carleton.ca/~cingalls/studentProjects/Katie's%20Site/html/All%20Curves.html)
    into a format suitable for Macaulay2"""
    formatted = ""

    for index, char in enumerate(raw):
        if index > 0 and char.isnumeric() and raw[index - 1].isalpha():
            formatted += "^"
            formatted += char
        elif index > 0 and char.isalpha() and raw[index - 1].isnumeric():
            formatted += "*"
            formatted += char
        elif index > 0 and char.isalpha() and raw[index - 1].isalpha():
            formatted += "*"
            formatted += char
        else:
            formatted += char

    # set constants
    formatted = formatted.replace("a", "101")
    formatted = formatted.replace("b", "97")

    return formatted


def main():
    formatted = parse(sys.argv[1])
    print(formatted)
    pyperclip.copy(formatted)


if __name__ == "__main__":
    main()
