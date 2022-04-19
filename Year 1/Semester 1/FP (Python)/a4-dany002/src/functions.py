"""
  Program functionalities module
"""
from domain import get_apartment, get_types, get_amount, create_expenses, set_amount
from copy import copy

def check_type(types):
    """
    It checks if the given type is one from the predefined categories: from one of the predefined categories water, heating, electricity, gas and other
    :param types: string
    :return: True or False
    """
    types = types.lower()
    if types == "water" or types == "heating" or types == "electricity" or types == "gas" or types == "other":
        return True
    return False


def add_expenses(expenses, apartment, amount, types):
    """
    It adds to the expenses list the apartment, amount and the types
    :param expenses: list
    :param apartment: positive integer
    :param amount: positive integer
    :param types: string
    :return: none
    """
    person = create_expenses(apartment, amount, types)
    expenses.append(person)
    return

def sort_expenses_by_number_of_apartment(expenses):
    """
    It sorts the expenses list by the number of apartment.
    :param expenses: list
    :return: the expenses list sorted by number of apartment.
    """
    return sorted(expenses, key=lambda x: int(x['number_of_apartment']))


def sort_expenses_by_type(expenses):
    """
    It sorts the expenses list by type.
    :param expenses: list
    :return: the expenses list sorted by type
    """
    return sorted(expenses, key=lambda x: x['type'])


def find_apartment(expenses, number_of_apartment):
    """
    It checks if the given apartment is in the expenses.
    :param expenses: list
    :param number_of_apartment: positive integer
    :return: False or True
    """
    for index in range(len(expenses)):
        if get_apartment(expenses[index]) == number_of_apartment:
            return True
    return False


def sum_of_all_expenses_for_an_apartment(expenses, number_of_apartment):
    """
    It computes the sum of all expenses for a given apartment.
    :param expenses: list
    :param number_of_apartment: string
    :return: the sum
    """
    number_of_apartment = int(number_of_apartment)
    sum = 0
    for index in range(len(expenses)):
        element_from_dictionary = expenses[index]
        if int(get_apartment(element_from_dictionary)) == number_of_apartment:
            sum += int(get_amount(element_from_dictionary))
    return sum


def remove_whitespaces_in_list_of_commands(list_of_commands):
    """
    It removes multiply empty spaces from string list
    :param list_of_commands: list
    :return: new_list which is the old list but without whitespaces anymore.
    """
    new_list = []
    for element in list_of_commands:
        if element.strip():
            new_list.append(element)
    return new_list


def sum_for_a_given_type(expenses, *list_of_commands):
    """
    It computes the sum for a given type from the given list.
    :param expenses: list
    :param list_of_commands: tuple read from keyboard
    :return: sum
    """
    list_of_commands = remove_whitespaces_in_list_of_commands(list(list_of_commands))
    if len(list_of_commands) != 1:
        raise ValueError("Invalid input: You need to insert 1 argument: <type>")
    if check_type(list_of_commands[0]) == False:
        raise ValueError("Invalid input: you have to choose the type from one of the predefined categories: water, heating, electricity, gas and other.")
    given_type = list_of_commands[0]
    sum = 0
    for index in range(len(expenses)):
        if get_types(expenses[index]) == given_type:
            sum += int(get_amount(expenses[index]))
    return sum


def maximum_amount_per_each_expense_type_for_a_given_apartment(expenses, *list_of_commands):
    """
    It computes the maximum amount per each expense type from the given list for a given apartment.
    :param expenses: list
    :param *list_of_commands: tuple read from the keyboard
    return: new_list_with_the_maximum_amount_per_each_expense which is a list of dictionaries and it looks like this:
                                    [{'type': one from predefined categories, 'amount': maximum amount per that type}]
    """
    list_of_commands = remove_whitespaces_in_list_of_commands(list(list_of_commands))
    if len(list_of_commands) != 1:
        raise ValueError("Invalid input: you need to insert 1 argument: <apartment>")
    if list_of_commands[0].isdigit() == False:
        raise ValueError("Invalid input: you have to choose a positive integer for the number of apartment.")
    number_of_apartment = int(list_of_commands[0])
    if find_apartment(expenses,number_of_apartment) == False:
        raise ValueError("Invalid input: the given number of apartment is not found so the maximum for each expense type is 0")
    expenses = sort_expenses_by_number_of_apartment(list(expenses))
    new_list_with_the_maximum_amount_per_each_expense = [{'type': 'gas', 'amount': 0}, {'type': 'water', 'amount' : 0},
                                                         {'type': 'heating', 'amount' : 0}, {'type': 'other', 'amount' : 0 },
                                                         {'type': 'electricity', 'amount' : 0}]
    for index in range(len(expenses)):
        if int(get_apartment(expenses[index])) == int(number_of_apartment):
            for index_for_the_maximum_amount in range(len(new_list_with_the_maximum_amount_per_each_expense)):
                if get_types(expenses[index]) == get_types(new_list_with_the_maximum_amount_per_each_expense[index_for_the_maximum_amount]) and \
                        int(get_amount(expenses[index])) > int(get_amount(new_list_with_the_maximum_amount_per_each_expense[index_for_the_maximum_amount])):
                    set_amount(new_list_with_the_maximum_amount_per_each_expense[index_for_the_maximum_amount], int(get_amount(expenses[index])))
    return new_list_with_the_maximum_amount_per_each_expense




def sort_ascending_by_total_amount_of_expenses(expenses):
    """
    New_expense_with_the_total_amount_of_expenses_per_apartment is a list with dictionaries that looks like this:
    { number of apartment: unique, amount: the sum of all expenses for the apartment , type: all }
    :param expenses: list
    :return: new_expense_with_the_total_amount_of_expenses_per_apartment sorted ascending by amount.
    """
    expenses = sort_expenses_by_number_of_apartment(list(expenses))
    new_expense_with_the_total_amount_of_expenses_per_apartment = []
    for index in range(len(expenses) - 1):
        if int(get_apartment(expenses[index])) != int(get_apartment(expenses[index+1])):
            expense_total_amount = create_expenses(get_apartment(expenses[index]),
                                                   sum_of_all_expenses_for_an_apartment(expenses, get_apartment(expenses[index])),"all")
            new_expense_with_the_total_amount_of_expenses_per_apartment.append(expense_total_amount)
    if find_apartment(new_expense_with_the_total_amount_of_expenses_per_apartment, int(get_apartment(expenses[len(expenses)-1]))) == False: # we add the last apartment
        expense_total_amount = create_expenses(get_apartment(expenses[len(expenses)-1]), sum_of_all_expenses_for_an_apartment(expenses, get_apartment(expenses[len(expenses)-1])),
                                               "all")
        new_expense_with_the_total_amount_of_expenses_per_apartment.append(expense_total_amount)

    return sorted(new_expense_with_the_total_amount_of_expenses_per_apartment, key=lambda x: int(x['amount']))



def sort_ascending_by_amount_for_each_type(expenses):
    """
    It sorts ascdending by amount for each type from the given list. The new created list looks like this:
    [{'id': unique, from 1 to 5, 'amount': sum for the given type, 'type' one from the predefined type}]
    :param expenses: list
    :return: new_list_with_the_total_amount_for_each_type list, sorted ascending by amount.
    """
    new_list_with_the_total_amount_for_each_type = []
    expense_total_amount_for_a_given_type = create_expenses(1, sum_for_a_given_type(expenses, "gas"), "gas")
    new_list_with_the_total_amount_for_each_type.append(expense_total_amount_for_a_given_type)
    expense_total_amount_for_a_given_type = create_expenses(2, sum_for_a_given_type(expenses, "other"), "other")
    new_list_with_the_total_amount_for_each_type.append(expense_total_amount_for_a_given_type)
    expense_total_amount_for_a_given_type = create_expenses(3, sum_for_a_given_type(expenses, "water"), "water")
    new_list_with_the_total_amount_for_each_type.append(expense_total_amount_for_a_given_type)
    expense_total_amount_for_a_given_type = create_expenses(4, sum_for_a_given_type(expenses, "electricity"), "electricity")
    new_list_with_the_total_amount_for_each_type.append(expense_total_amount_for_a_given_type)
    expense_total_amount_for_a_given_type = create_expenses(5, sum_for_a_given_type(expenses, "heating"), "heating")
    new_list_with_the_total_amount_for_each_type.append(expense_total_amount_for_a_given_type)
    return sorted(new_list_with_the_total_amount_for_each_type, key=lambda x: int(x['amount']))


def add(history_of_expenses, expenses, *list_of_commands):
    """
    It checks if the input is correct ( add <number of apartment> <type> <amount> ) and if it is, the function will add the input in expenses by using function add_expenses
    :param expenses: list
    :param *list_of_commands: a tuple read from keyboard.
    :return: none
    """
    list_of_commands = remove_whitespaces_in_list_of_commands(list(list_of_commands))
    if list_of_commands[0] == "help":
        raise ValueError("Input help: 'add <apartment> <type> <amount>'")
    if len(list_of_commands) != 3:
        raise ValueError("Invalid input: you need to insert 3 arguments: <number of apartment> <type> <amount>.")
    number_of_apartment = list_of_commands[0]
    types = list_of_commands[1]
    amount = list_of_commands[2]
    if check_type(types) == False:
        raise ValueError("Invalid input: you have to choose the type from one of the predefined categories: water, heating, electricity, gas and other.")
    if number_of_apartment.isdigit() == False:
        raise ValueError("Invalid input: you have to choose a positive integer for the number of apartment.")
    if amount.isdigit() == False:
        raise ValueError("Invalid input: you have to choose a positive integer for amount.")
    history_of_expenses.append(copy(expenses))
    add_expenses(expenses, number_of_apartment, amount, types)
    return


def undo_expenses(history_of_expenses, expenses):
    """
    It undo the last operation taken.
    :param history_of_expenses: list
    :param expenses: list
    :return: none
    """
    if len(history_of_expenses) == 0:
        raise ValueError("You can't undo anymore!")
    expenses[:] = history_of_expenses[-1] # copy every element from history_of_expenses to expenses.
    history_of_expenses.pop()
    return

def filter_by_value(expenses, list_of_commands):
    """
    It removes all the apartments from the given list that have the sum of all expenses greater or equal than the given value.
    :param expenses: list
    :param list_of_commands: list
    :return: none
    """
    list_of_commands = list(list_of_commands)
    index = 0
    length_of_expenses = len(expenses)
    while index < length_of_expenses:
        if sum_of_all_expenses_for_an_apartment(expenses,int(get_apartment(expenses[index]))) >= int(list_of_commands[0]):
            remove([],expenses,str(get_apartment(expenses[index])))
            length_of_expenses = len(expenses)
            index -= 1
        index += 1
    return

def filter_by_type(expenses, *list_of_commands):
    """
    It removes all the expenses from the given list that don't have the given type.
    :param expenses: list
    :param *list_of_commands: tuple read from keyboard
    :return: none
    """
    types = ['water','heating','electricity','gas','other']
    for i in range(5):
        if types[i] != list_of_commands[0]:
            remove([], expenses, types[i])
    return


def filter(history_of_expenses ,expenses, *list_of_commands):
    """
    It checks if the input is correct: filter <type> or filter <value> and it calls the right function depending on type or value.
    :param expenses: list
    :param *list_of_commands: tuple read from the keyboard
    :return: none
    """
    list_of_commands = remove_whitespaces_in_list_of_commands(list(list_of_commands))
    if list_of_commands[0] == "help":
        raise ValueError("Input help: 'filter <type>' or 'filter <value>'")
    if len(list_of_commands) != 1:
        raise ValueError("Invalid input: you have to choose between filter <type> or filter <category> ")
    if list_of_commands[0].isdigit() == False:
        if check_type(list_of_commands[0]) == False:
            raise ValueError("Invalid input: you have to choose the type from one of the predefined categories: water, heating, electricity, gas and other or a value.")

    history_of_expenses.append(copy(expenses))
    if list_of_commands[0].isdigit() == True:
        filter_by_value(expenses, list_of_commands)
    else:
        filter_by_type(expenses, *list_of_commands)
    return


def initial_list():
    """
    It creates the initial list.
    :return: none
    """
    return [create_expenses(10, 20, "gas"),
            create_expenses(11, 153, "other"),
            create_expenses(13, 30, "electricity"),
            create_expenses(12, 80, "water"),
            create_expenses(11, 40, "gas"),
            create_expenses(13, 91, "heating"),
            create_expenses(15, 50, "water"),
            create_expenses(10, 80, "other"),
            create_expenses(16, 60, "electricity"),
            create_expenses(10, 70, "heating")]


def remove(history_of_expenses, expenses, *list_of_commands):
    """
    It checks if the input is valid ( remove <apartment>
                                      remove <start apartment> to <end apartment>
                                      remove <type> ) and if it is, then it removes from expenses the apartment or
                                      the type or the apartments from a start to an end.
    :param expenses: list
    :param *list_of_commands: tuple
    :return: none
    """
    list_of_commands = remove_whitespaces_in_list_of_commands(list(list_of_commands))
    if list_of_commands[0] == "help":
        raise ValueError("Input help: 'remove <apartment>' or 'remove <start apartment> to <end apartment>' or 'remove <type>'")
    if len(list_of_commands) > 3:
        raise ValueError("Invalid input: you can insert maximum 3 arguments")
    history_of_expenses.append(copy(expenses))
    if len(list_of_commands) == 1:
        given_type = -1
        given_number_of_apartment = -1
        if check_type(list_of_commands[0]) == True:   # this is the case: remove <type> gas
            given_type = list_of_commands[0]
        else:
            given_number_of_apartment = int(list_of_commands[0])   # this is the case: remove <apartment>
        index = 0
        length_of_expenses = len(expenses)

        if given_number_of_apartment == -1:   # this is the: remove <type>
            while index < length_of_expenses:
                if get_types(expenses[index]) == given_type:
                    del expenses[index]
                    index -= 1
                    length_of_expenses -= 1
                index += 1
        else:   # for case: remove <apartment>
            while index < length_of_expenses:
                if int(get_apartment(expenses[index])) == given_number_of_apartment:
                    del expenses[index]
                    index -= 1
                    length_of_expenses -= 1
                index += 1
        return

    else:    # This is for case from <start_apartment> to <end_apartment>
        start_apartment = int(list_of_commands[0])
        end_apartment = int(list_of_commands[2])
        if end_apartment < start_apartment:
            raise ValueError("Input error: <start apartment> is greater than <end apartment>.")
        index = 0
        length_of_expenses = len(expenses)
        while index < length_of_expenses:
            if int(get_apartment(expenses[index])) >= start_apartment and \
                    int(get_apartment(expenses[index])) <= end_apartment:
                del expenses[index]
                index -= 1
                length_of_expenses -= 1
            index += 1
        return


def replace(history_of_expenses, expenses, *list_of_commands):
    """
    It checks if the input is correct ( replace <apartment> <type> with <amount> ) and it removes the expenses from that apartment, type;
     and it adds the new one with the given parameters
    :param expenses: dictionary
    :param *list_of_commands: tuple
    :return: none
    """
    list_of_commands = remove_whitespaces_in_list_of_commands(list(list_of_commands))
    if list_of_commands[0] == "help":
        raise ValueError("Input help:'replace <apartment> <type> with <amount>'")
    if len(list_of_commands) != 4:
        raise ValueError("Invalid input: you can insert only 4 arguments: replace <apartment> <type> with <amount>")
    given_type = list_of_commands[1]

    if check_type(given_type) == False:
        raise ValueError("Invalid input: you have to choose the type from one of the predefined categories: water, heating, electricity, gas and other.")
    if list_of_commands[0].isdigit() == False:
        raise ValueError("Invalid input: you have to choose a positive integer for the number of apartment.")
    if list_of_commands[3].isdigit() == False:
        raise ValueError("Invalid input: you have to choose a positive integer for amount.")
    number_of_apartment = int(list_of_commands[0])
    if find_apartment(expenses,number_of_apartment) == False:
        raise ValueError("Invalid input: the given number of apartment is not found!")
    history_of_expenses.append(copy(expenses))
    given_amount = int(list_of_commands[3])

    index = 0
    length_of_expenses = len(expenses)
    while index < length_of_expenses:
        if int(get_apartment(expenses[index])) == number_of_apartment and \
                get_types(expenses[index]) == given_type and \
                int(get_amount(expenses[index])) != given_amount:
            set_amount(expenses[index], given_amount)
            index -= 1
        index += 1

    return
