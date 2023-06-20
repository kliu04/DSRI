import sys
import pyperclip


def main():
    raw = sys.argv[1]
    # raw = "x6+y6+3x4y2-3x4+3x2y4-3y4+21x2y2+3x2+3y2-1"
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

    print(formatted)
    pyperclip.copy(formatted)


if __name__ == "__main__":
    main()
