"""
  User interface module
"""
from domain import get_apartment, get_amount, get_types
from functions import sort_expenses_by_number_of_apartment, sum_of_all_expenses_for_an_apartment, remove_whitespaces_in_list_of_commands,\
    sum_for_a_given_type, maximum_amount_per_each_expense_type_for_a_given_apartment, sort_ascending_by_total_amount_of_expenses,\
    sort_ascending_by_amount_for_each_type


def print_all_expenses (expenses):
    for index in range(len(expenses)):
        print("Number of apartment:", get_apartment(expenses[index]), ", amount:", get_amount(expenses[index]), ", type:", get_types(expenses[index]), sep='')


def print_all_expenses_for_an_apartment(expenses, number_of_apartment):
    for index in range(len(expenses)):
        if int(get_apartment(expenses[index])) == int(number_of_apartment):
            print("Number of apartment:", get_apartment(expenses[index]), ", amount:", get_amount(expenses[index]), ", type:", get_types(expenses[index]), sep='')


def ui_list(expenses, *list_of_commands):
    """
    It prints all the dictionary if the given instruction is "list"
    It prints all expenses for a given apartment if the given instruction is "list <apartment>"
    It prints all apartments having total expenses "</=/>" than an amount ( instruction is: list [ < | = | > ] <amount> )
    :param expenses: list
    :param *list_of_commands: tuple
    :return: none
    """
    list_of_commands = remove_whitespaces_in_list_of_commands(list(list_of_commands))    # convert from tuple to list
    if len(list_of_commands) != 0:
        if list_of_commands[0] == "help":
            raise ValueError("Input help: 'list' or 'list <apartment>' 'list [ < | = | > ] <amount>'")

    if len(list_of_commands) == 0:
        print_all_expenses(expenses)
        return

    if len(list_of_commands) == 1:
        number_of_apartment = list_of_commands[0]
        print_all_expenses_for_an_apartment(expenses, number_of_apartment)
        return

    sorted_list_of_expenses = sort_expenses_by_number_of_apartment(expenses)    # it sorts the old dictionary by number of apartments in an ascending order and now it's a list
    given_amount = int(list_of_commands[1])

    for index in range(len(sorted_list_of_expenses)):
        if index != len(sorted_list_of_expenses)-1:
            next_list_of_expenses = sorted_list_of_expenses[index+1]
        else:
            next_list_of_expenses = sorted_list_of_expenses[index]
        if (get_apartment(sorted_list_of_expenses[index]) != get_apartment(next_list_of_expenses) and index < len(sorted_list_of_expenses))\
            or index == (len(sorted_list_of_expenses)-1):
            sum_for_an_apartment = sum_of_all_expenses_for_an_apartment(expenses, get_apartment(sorted_list_of_expenses[index]))
            if list_of_commands[0] == "<":
                if sum_for_an_apartment < given_amount:
                    print(get_apartment(sorted_list_of_expenses[index]))

            elif list_of_commands[0] == "=":
                if sum_for_an_apartment == given_amount:
                    print(get_apartment(sorted_list_of_expenses[index]))
            else:
                if sum_for_an_apartment > given_amount:
                    print(get_apartment(sorted_list_of_expenses[index]))
    return




def print_commands(commands):
    """
    It prints all the commands ( add, remove, replace, list, exit )
    :param commands: dictionary
    :return: none
    """
    print("Please choose one from the following commands: ")
    print(*list(commands.keys()), 'exit', sep='\n')
    print("If you need help, type '<command> help'.")


def print_the_sum_for_a_given_type(expenses, *list_of_commands):
    list_of_commands = remove_whitespaces_in_list_of_commands(list(list_of_commands))
    if list_of_commands[0] == "help":
        raise ValueError("Input help: 'sum <type>'")
    total_amount = sum_for_a_given_type(expenses, *list_of_commands)
    print("The total amount for the expenses having type",list_of_commands[0],"is:", total_amount)


def print_the_maximum_amount_per_each_expense_type_for_an_apartment(expenses, *list_of_commands):
    list_of_commands = remove_whitespaces_in_list_of_commands(list(list_of_commands))
    if list_of_commands[0] == "help":
        raise ValueError("Input help: 'max <apartment>'")
    list_with_the_maximum_amount = maximum_amount_per_each_expense_type_for_a_given_apartment(expenses, *list_of_commands)


    for index in range(len(list_with_the_maximum_amount)):
        print("The maximum amount for the apartment ", list_of_commands[0], " for ", get_types(list_with_the_maximum_amount[index]),
              " is: ", get_amount(list_with_the_maximum_amount[index]), sep='')

def print_the_list_of_apartments_sorted_ascending_by_total_amount_of_expenses(expenses):
    expenses = sort_ascending_by_total_amount_of_expenses(expenses)
    print("The list of apartments sorted ascending by total amount of expenses is:")
    for index in range(len(expenses)):
        print(get_apartment(expenses[index]), end=' ')
    print('\n')

def print_the_total_amount_for_each_type_ascending_by_amount_of_money(expenses):
    expenses = sort_ascending_by_amount_for_each_type(expenses)
    print("The total amount of expenses for each type, sorted ascending by amount of money is: ")
    for index in range(len(expenses)):
        print("The total amount for", get_types(expenses[index]), "is:", get_amount(expenses[index]))

def sort_functions(expenses, *list_of_commands):
    list_of_commands = remove_whitespaces_in_list_of_commands(list(list_of_commands))
    if list_of_commands[0] == "help":
        raise ValueError("Input help: 'sort apartment' or 'sort type'")
    if len(list_of_commands) != 1 or (list_of_commands[0] != "apartment" and list_of_commands[0] != "type"):
        raise ValueError("Invalid input: you have to choose between sort apartment or sort type.")
    if list_of_commands[0] == "apartment":
        print_the_list_of_apartments_sorted_ascending_by_total_amount_of_expenses(expenses)
    else:
        print_the_total_amount_for_each_type_ascending_by_amount_of_money(expenses)
    return
