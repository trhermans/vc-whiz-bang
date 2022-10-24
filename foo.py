def whiz_bang(whiz, bang):
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
    elif bang:
        print("Bang")

def beep_boop(beeps, booper):
    for i in range(beeps):
        if i % booper == 0:
            print("Boop!")
        else:
            print("Beep!")
