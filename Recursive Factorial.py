# Uses Recursion to find Factorial of a number

def fact(n):
    if n == 1:
        return 1

    return n * fact(n-1)


print(fact(int(input("Enter the number - "))))
