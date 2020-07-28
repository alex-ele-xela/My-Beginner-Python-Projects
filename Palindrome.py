def palin(text):
    if text == '':
        return False

    text = text.replace(' ', '')
    text = text.upper()

    lst = list(text)
    revlst = lst[:]
    revlst.reverse()

    if lst == revlst:
        return True


text = input("Enter the string to check : ")

if palin(text):
    print("It is a Palindrome !")
else:
    print("It is not a Palindrome.")
