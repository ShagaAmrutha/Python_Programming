def check_char(ch):
    if ch.isalpha():
        print("an alphabet")
    elif ch.isdigit():
        print("a digit")
    else:
        print("special char")
ch=input("enter anu char")
check_char(ch)