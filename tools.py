def readNonemptyString(prompt):
    """
    :param prompt: Text you want to display
    :return: input string from user
    """
    while True:
        text = input(prompt)
        copy = text.replace(" ", "").replace("/t", "")
        if len(copy) > 0:
            return text
        else:
            print("Empty text!")


def floatInput(prompt, state=""):
    """
    :param prompt: Text you want to display
    :param state:
    :state:
     -"" default any
     -"p" only positive
     -"n" only negative
    :return: negative or positive float
    """
    while True:
        try:
            if state == "p":
                output = float(input(prompt))
                if output > 0:
                    return output
                else:
                    print("Please input a positive float.")
            elif state == "n":
                output = float(input(prompt))
                if output < 0:
                    return output
                else:
                    print("Please input a negative float.")
            else:
                return float(input(prompt))
        except Exception:
            print("Only numbers!")


def intInput(prompt, state=""):
    """
    :param prompt: Text you want to display
    :param state:
     -"" default any
     -"p" only positive
     -"n" only negative
    :return: negative or positive integer
    """
    while True:
        try:
            if state == "p":
                output = int(input(prompt))
                if output > 0:
                    return output
                else:
                    print("Please input a positive integer.")
            elif state == "n":
                output = int(input(prompt))
                if output < 0:
                    return output
                else:
                    print("Please input a negative integer.")
            else:
                return int(input(prompt))
        except Exception:
            print("Only numbers!")


def binaryOption(prompt, x, y):
    """
    :param prompt: Text you want to display
    :param x: first requested value
    :param y: second requested value
    :return: only x or y will be returned
    """
    while True:
        choice = readNonemptyString(prompt).lower().replace(" ", "")
        if choice == x or choice == y:
            return choice
        else:
            print(f"Only input '{x}' or '{y}'!")


def rangeInt(prompt, x, y):
    """
    :param prompt: Text you want to display
    :param x: min range
    :param y: max range
    :return: only a number will be returned
    """
    while True:
        try:
            choice = intInput(prompt, "p")
            # print(x <= choice <= y)
            if x <= choice <= y:
                return choice
            else:
                print(f"Input an integer between {x} and {y}.\n")
        except ValueError:
            print("Only input integers.\n")
