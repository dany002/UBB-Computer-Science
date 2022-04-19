# Solve the problem from the third set here
"""
14. Determine the n-th element of the sequence 1,2,3,2,2,5,2,2,3,3,3,7,2,2,3,3,3,2,2,3,3,3,2,2,5,5,5,5,5,11... obtained from the sequence of
natural numbers by replacing composed numbers with their prime divisors, each divisor d being written d times,
without memorizing the elements of the sequence.
"""

def read():
    """
    It reads the value.
    :return: value - integer, the value read.
    """
    value = input("n = ")
    value = int(value)
    return value


def composite(number):
    """
    It checks if the number is composite.
    :param number: natural number
    :return: True if the number is composite and False if the number isn't composite.
    """
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return True
    return False


def solve(value):
    """
    It returns the n-th element of the given sequence
    :param value: natural number
    :return: None
    """
    i = 1
    while True:
        if composite(i) == False:
            if value == 1:
                return i
            value -= 1
        else:
            copy = i
            for d in range(2, copy // 2 + 1):
                if copy % d == 0:
                    while copy % d == 0:
                        copy //= d
                    if value <= d:
                        return d
                    value -= d
        i += 1


if __name__ == "__main__":
    n = read()
    print(solve(n))










