"""Functions for beeping, whizzing, etc."""


def whiz_bang(whiz: bool, bang: bool) -> None:
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
