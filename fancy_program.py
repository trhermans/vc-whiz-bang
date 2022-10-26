from foo import whiz_bang, beep_boop

def run_whiz_bang():
    whiz_bang(True, True)

def run_beep_boop():
    beep_boop(5, 13)

def run_whiz_boop():
    pass

def main():
    run_whiz_bang()
    run_beep_boop()
    run_whiz_boop()

if __name__ == "__main__":
    main()
