
"""
    You have 2 matrices I and II. I is yours, II is for the bot. The matrices look like this:
       1  2  3  4  5  6  7  8  9  10
    A  0  0  0  0  0  0  0  0  0  0
    B  0  0  x  0  0  0  0  0  0  0
    C  x  x  x  x  x  0  0  0  0  0
    D  0  0  x  0  0  0  0  0  0  0
    E  0  x  x  x  0  0  x  0  0  0
    F  0  0  0  0  0  0  x  0  x  0
    G  0  0  0  0  0  x  x  x  x  0
    H  0  0  0  0  0  0  x  0  x  0
    I  0  0  0  0  0  0  x  0  0  0
    J  0  0  0  0  0  0  0  0  0  0

    with 1 are the planes, in the example you have only 2 planes. if i choose for example B3 and G6, the matrix will become:
       1  2  3  4  5  6  7  8  9  10
    A  0  0  0  0  0  0  0  0  0  0
    B  0  0  1  0  0  0  0  0  0  0
    C  1  1  1  1  1  0  0  0  0  0
    D  0  0  1  0  0  0  0  0  0  0
    E  0  1  1  1  0  0  1  0  0  0
    F  0  0  0  0  0  0  1  0  1  0
    G  0  0  0  0  0  1  1  1  1  0
    H  0  0  0  0  0  0  1  0  1  0
    I  0  0  0  0  0  0  1  0  0  0
    J  0  0  0  0  0  0  0  0  0  0

    So if u've guessed that element will become y and if u guessed the cabin all the plane will be x for ex, if u choose B3 and H7

       1  2  3  4  5  6  7  8  9  10
    A  0  0  0  0  0  0  0  0  0  0
    B  0  0  x  0  0  0  0  0  0  0
    C  x  x  x  x  x  0  0  0  0  0
    D  0  0  x  0  0  0  0  0  0  0
    E  0  x  x  x  0  0  1  0  0  0
    F  0  0  0  0  0  0  1  0  1  0
    G  0  0  0  0  0  1  1  1  1  0
    H  0  0  0  0  0  0  y  0  1  0
    I  0  0  0  0  0  0  1  0  0  0
    J  0  0  0  0  0  0  0  0  0  0

    Example of planes with left cabin:
       1  2  3  4  5  6  7  8  9  10
    A  0  x  0  0  0  0  0  0  0  0
    B  0  x  0  x  0  0  0  0  0  0
    C  x  x  x  x  0  0  0  0  0  0
    D  0  x  0  x  0  0  0  0  0  0
    E  0  x  0  0  0  0  x  0  0  0
    F  0  0  0  0  0  0  x  0  x  0
    G  0  0  0  0  0  x  x  x  x  0
    H  0  0  0  0  0  0  x  0  x  0
    I  0  0  0  0  0  0  x  0  0  0
    J  0  0  0  0  0  0  0  0  0  0

    Example of planes with right cabin:

       1  2  3  4  5  6  7  8  9  10
    A  0  0  0  x  0  0  0  0  0  0
    B  0  x  0  x  0  0  0  0  0  0
    C  0  x  x  x  x  0  0  0  0  0
    D  0  x  0  x  0  0  0  0  0  0
    E  0  0  0  x  0  0  0  x  0  0
    F  0  0  0  0  0  x  0  x  0  0
    G  0  0  0  0  0  x  x  x  x  0
    H  0  0  0  0  0  x  0  x  0  0
    I  0  0  0  0  0  0  0  x  0  0
    J  0  0  0  0  0  0  0  0  0  0

    Example of planes with up cabin:
       1  2  3  4  5  6  7  8  9  10
    A  0  0  0  0  0  0  0  0  0  0
    B  0  0  x  0  0  0  0  0  0  0
    C  x  x  x  x  x  0  0  0  0  0
    D  0  0  x  0  0  0  0  0  0  0
    E  0  x  x  x  0  0  x  0  0  0
    F  0  0  0  0  x  x  x  x  x  0
    G  0  0  0  0  0  0  x  0  0  0
    H  0  0  0  0  0  x  x  x  0  0
    I  0  0  0  0  0  0  0  0  0  0
    J  0  0  0  0  0  0  0  0  0  0

    Example of planes with down cabin:
       1  2  3  4  5  6  7  8  9  10
    A  0  0  0  0  0  0  0  0  0  0
    B  0  x  x  x  0  0  0  0  0  0
    C  0  0  x  0  0  0  0  0  0  0
    D  x  x  x  x  x  0  0  0  0  0
    E  0  0  x  0  0  0  0  0  0  0
    F  0  0  0  0  0  x  x  x  0  0
    G  0  0  0  0  0  0  x  0  0  0
    H  0  0  0  0  x  x  x  x  x  0
    I  0  0  0  0  0  0  x  0  0  0
    J  0  0  0  0  0  0  0  0  0  0




"""