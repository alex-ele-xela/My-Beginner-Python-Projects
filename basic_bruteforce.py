'''
This is a very basic Bruteforcer which guesses the entered password
It tells the number of comparisons and amount of time taken
'''


import time
import sys

password = sys.argv[1]
counter = 0
trial_password = []


def bruteforce(length=1):
    global trial_password
    trial_password = ['a' for x in range(length)]
    for i in range(length-1, -1, -1):
        flag = pre_checker(trial_password, i, length-1)
        if flag:
            return(time.time(), True)

    return bruteforce(length+1)


def pre_checker(trial, current, index):
    if current != index:
        for i in range(97, 123):
            trial[current] = chr(i)
            if pre_checker(trial, current+1, index):
                return True
    else:
        return end_checker(trial, index)


def end_checker(trial, index):
    global counter
    for i in range(97, 123):
        trial[index] = chr(i)
        counter += 1
        if "".join(trial) == password:
            return True

    return False


def main():
    global start
    start = time.time()
    stop, flag = bruteforce()

    if flag:
        print(
            f"Password is bruteforced successfully in {stop-start} seconds, after making {counter} comparisons.")
    else:
        print(
            f"Could not bruteforce password even after {counter} comparisons.")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        string = "".join(trial_password)
        stop = time.time()
        print(f"Bruteforcing terminated at {string}, in {stop-start} seconds")
