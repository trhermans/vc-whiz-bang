"""Functions for beeping, whizzing, etc."""


from math import sqrt


def whiz_bang(whiz: bool = True, bang: bool = False) -> None:
    """
    If whiz is true then print "Whiz"
    If bang is true then print "Bang
    If both are true print "WhizBang!"

    :param whiz: boolean variable seeing if the program should whiz
    :param bang: boolean variable seeing if the program should bang
    :return: None
    """
    if whiz:
        print("Whiz")
    if bang:
        print("Bang")


def beep_boop(beeps: int, booper: int) -> None:
    """
    Print a sequence of beeps of boops.

    :param beeps: int giving total number of strings to print
    :param booper: int that when current iterate evenly divides by booper print boop
    :return: None
    """

    for i in range(beeps):
        if i % booper == 0:
            print("Boop!")
        else:
            print("Beep!")


def sum_int_and_str(int_val: int, str_val: str = "3") -> int:
    """
    Sum up an integer and an integer in a string.

    :param int_val: integer to add to sum
    :param str_val: string to add to sum
    :return: sum of the two inputs
    """
    return int_val + int(str_val)

def positive_list(list_in: list) -> list:
    """
    Return a list only containing the positive elements of the input list.

    :param list_in: input list of numbers
    :return: list of only positive numbers
    """
    assert isinstance(list_in, list), "list_in must be of type list"
    return [i for i in list_in if i > 0]

def split_list(to_split: list) -> tuple[list, list]:
    """
    Split a list in half and return the two list halves.

    :param to_split: list to split in half
    :return: tuple containing two lists
    """
    split_idx = int(len(to_split)/2)
    return to_split[:split_idx], to_split[split_idx:]

def hello(greeting: str) -> None:
    """
    Say hello followed by a greeting.

    :param greeting: string to print
    :return: None
    """
    print("Hello", greeting)

def take_sqrt(x : float) -> float:
    """
    Take a sqrt of input number x

    :param x: positive float
    :return: sqrt of x
    """
    assert x >= 0, "X must be positive"
    return sqrt(x)

def scale_smaller(x: float, s: float) -> float:
    """
    Take x an make it smaller by the scale value s

    :param x: number to make smaller
    :param s: scale value between 0 and 1
    :return: scaled version of x
    """
    assert 0 < s < 1, "Scalar s must be between 0 and 1"
    return x*s

class Student:

    def __init__(self, name, major="Undecalared"):
        self.name = name
        self.major = major

    def intro(self):
        print("Hey I'm", self.name, "and I study", self.major)

class CompStudent(Student):

    def intro(self):
        print("Hey I'm", self.name, "and my favorite class by far is COMP 1020!")
