#Generates n Fibonacci Sequence Numbers

def fib_gen(num):
    a = 0
    b = 1

    for i in range(num):
        yield a
        a, b = b, a+b


for i in fib_gen(20):
    print(i)
