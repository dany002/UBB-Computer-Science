# Solve the problem from the first set here
# 3. For a given natural number n find the minimal natural number m formed with the same digits. (e.g. n=3658, m=3568).


def read():
    """
    It reads the value.
    :return: value - natural number, the value read.
    """
    value = input("n=")
    value = int(value)
    return value


def solution(array):
    """
    First we check that the first digit to be a not null digit.
    It prints the number, if the frequency of the digit is 0 we dont print it. That end='' is to not print on a new line the next digit.
    :return: none
    """
    print("m=",end='')
    for i in range(10):
        if array[i] != 0 and i != 0:
            print(i,end='')
            array[i] -= 1
            break
    for i in range(10):
        while array[i] != 0:
            print(i,end='')
            array[i] -= 1

def solve():
    """
    It computes the frequency of every digit and it's placed in an array.
    :return:
    """
    array = [0]*10
    value = read()
    while value != 0:
        array[value%10] = array[value%10]+1
        value //= 10
    solution(array)


if __name__ == "__main__":
    solve()

