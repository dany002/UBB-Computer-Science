def states(fa):
    initial_states = fa.q0
    print()
    print("Initial states:")
    for state in initial_states:
        print(state)

    final_states = fa.F
    print()
    print("Final states:")
    for state in final_states:
        print(state)

    all_states = fa.Q
    print()
    print("All the states:")
    for state in all_states:
        print(state)
    print()


def alphabet(fa):
    alph = fa.E
    print("\nAlphabet:")
    for letter in alph:
        print(letter)
    print()


def transitions(fa):
    trans = fa.S
    print("Transitions:")
    for t in trans:
        print(str(t))
    print()


def check_seq(fa):
    print("Enter the sequence you want to check:")
    seq = input()
    print(fa.check_sequence(seq, fa, fa.q0))
