def Password():
    import pyperclip
    import random
    import string

    while True:
        print("Type 'quit' to Quit.\n")
        x = 0
        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        paslength = input("How long do you want your password to be?\n")
        if paslength == 'quit':
            break
        passwordletters = []
        while x < int(paslength):
            passwordletters.append(random.choice(s))
            password = "".join(passwordletters)
            x += 1
        print("Your password is {}\n".format(password))
        copy = input("Would you like to copy the password? (y/n)\n")
        if copy == "y":
            pyperclip.copy(password)
        print("\n"*100)
Password()
