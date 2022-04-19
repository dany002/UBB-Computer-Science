"""
  Start the program by running this module
"""

from functions import initial_list, remove, replace, add, filter, undo_expenses
from ui import ui_list, print_commands, print_the_sum_for_a_given_type, \
    print_the_maximum_amount_per_each_expense_type_for_an_apartment, sort_functions

from tests import tests

def run_command():
    commands = {'add': add, 'remove': remove, 'replace': replace, 'list': ui_list, 'sum': print_the_sum_for_a_given_type,
                'max': print_the_maximum_amount_per_each_expense_type_for_an_apartment, 'sort': sort_functions, 'filter': filter,
                'undo': undo_expenses}
    expenses = initial_list()
    history_of_expenses = []
    while True:
        print_commands(commands)
        command_line = input("Enter command line: ")
        if command_line == "exit":
            break
        command, list_of_commands = get_command_and_list(command_line)
        try:
            if command in ['undo']:
                undo_expenses(history_of_expenses,expenses)
            elif command in ['add', 'remove', 'replace', 'filter']:
                commands[command](history_of_expenses, expenses, *list_of_commands)
            else:
                commands[command](expenses, *list_of_commands)
        except KeyError:
            print("This option is not implemented yet!")
        except ValueError as ve:
            print("The following exception was:", ve)


def get_command_and_list(command_line):
    command_line = command_line.strip()
    position = command_line.find(' ')
    if position == -1:
        return command_line, []
    command = command_line[:position]

    list_of_commands = command_line[position:]
    list_of_commands = list_of_commands.split(' ')
    list_of_commands = [elements.strip() for elements in list_of_commands]    # now is a list
    del list_of_commands[0]    # the first element is ''
    return command, list_of_commands


if __name__ == '__main__':
    tests()
    run_command()
#TODO undo and help menu