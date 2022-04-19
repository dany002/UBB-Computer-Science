# Solve the problem from the second set here
# 9. Consider a given natural number n. Determine the product p of all the proper factors of n.


def read():
    """
    It reads the value.
    :return: value - natural number, the value read.
    """
    value = input("n = ")
    value = int(value)
    return value


def proper_factor(value):
    """
    It computes the product of all the proper factors of n.
    :param value: natural number.
    :return: product - natural number - the product
    """
    product = 1
    for factor in range (2, value // 2 + 1 ):
        if value % factor == 0:
            product = product * factor
    return product


def solve():
    """
    It connects all the functions like reading a variable n and printing the product if it isn't 1.
    :return:
    """
    value = read()
    product = proper_factor(value)
    if product != 1:
        print("The product of all the proper factors of",value,"is",product)
    else:
        print("There aren't proper factors of the given number",value)


if __name__ == "__main__":
    solve()
