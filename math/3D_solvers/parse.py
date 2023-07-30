import sys
import pyperclip


def parse(raw: str) -> str:
    """Parses an equation copied as plaintext into a format suitable for Macaulay2"""
    formatted = ""

    for index, char in enumerate(raw):
        # x5 -> x^5
        if index > 0 and char.isnumeric() and raw[index - 1].isalpha():
            formatted += "^"
            formatted += char
        # 5x -> 5*x
        elif index > 0 and char.isalpha() and raw[index - 1].isnumeric():
            formatted += "*"
            formatted += char
        # xy -> x*y
        elif index > 0 and char.isalpha() and raw[index - 1].isalpha():
            formatted += "*"
            formatted += char
        # )( -> )*(
        elif index > 0 and char == "(" and raw[index - 1] == ")":
            formatted += "*"
            formatted += char
        # 5( -> 5*(
        elif index > 0 and char == "(" and raw[index - 1].isnumeric():
            formatted += "*"
            formatted += char
        # )5 -> )^5
        elif index > 0 and char.isnumeric() and raw[index - 1] == ")":
            formatted += "^"
            formatted += char
        else:
            formatted += char

    # set constants
    formatted = formatted.replace("a", "101")
    formatted = formatted.replace("b", "97")
    formatted = formatted.replace("c", "103")

    return formatted


def main():
    formatted = parse(sys.argv[1])
    print(formatted)
    pyperclip.copy(formatted)


if __name__ == "__main__":
    main()
