from FiniteAutomata import FiniteAutomata
from service import *
from utils import *


def print_menu():
    print("0. exit")
    print("1. Read finite automata")
    print("2. States")
    print("3. Alphabet")
    print("4. Transitions")
    print("5. Check sequence")
    print("Your choice: ", end="")


def main():
    fa = FiniteAutomata(list(), list(), list(), list(), list())

    while True:
        print_menu()
        try:
            option = int(input())
        except ValueError as e:
            print("The chosen option is not correct. Please try again.")
            continue

        if option == 0:
            break
        elif option == 1:
            #fa.read_automata("fa.txt")
            fa.read_automata("integer_numbers.txt")
            # fa.read_automata("idk.txt")
        elif option == 2:
            states(fa)
        elif option == 3:
            alphabet(fa)
        elif option == 4:
            transitions(fa)
        elif option == 5:
            check_seq(fa)
        else:
            print("The chosen option is not correct. Please try again.")


main()
