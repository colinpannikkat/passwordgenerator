def Password():
    import pyperclip
    import random
    import string
    import time

    while True:
        print("\n"*100)
        print("Press Ctrl+C to Quit.\n")
        x = 0
        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        paslength = input("How long do you want your password to be?\n")
        passwordletters = []

        try:
            while x < int(paslength):
                passwordletters.append(random.choice(s))
                password = "".join(passwordletters)
                x += 1
            print("\nYour password is {}\n".format(password))
            copy = input("Would you like to copy the password? (y/n)\n")
            if copy == "y":
                print("\nCopied!\n")
                pyperclip.copy(password)
                time.sleep(1)
        except ValueError:
            print("\nPlease enter a number!\n")
            time.sleep(1)
            continue
Password()
