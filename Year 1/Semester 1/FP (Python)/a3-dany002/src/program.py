

################################################### DOMAIN ##################################################

def create_expenses(apartment, amount, types):
    return {'number_of_apartment': apartment, 'amount': amount, 'type': types}


def get_apartment(expenses):
    return expenses['number_of_apartment']


def get_amount(expenses):
    return expenses['amount']


def get_types(expenses):
    return expenses['type']


def set_apartment(expenses, number_of_apartment):
    expenses['number_of_apartment'] = number_of_apartment


def set_amount(expenses, amount):
    expenses['amount'] = amount


def set_type(expenses, types):
    expenses['type'] = types

############################################# UI ###########################################################



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
    list_of_commands = list(list_of_commands)    # convert from tuple to list
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


def get_command_and_list(command_line):
    position = command_line.find(' ')
    if position == -1:
        return command_line, []
    command = command_line[:position]
    list_of_commands = command_line[position:]
    list_of_commands = list_of_commands.split(' ')
    list_of_commands = [elements.strip() for elements in list_of_commands]    # now is a list
    del list_of_commands[0]    # the first element is ''
    return command, list_of_commands


def print_commands(commands):
    """
    It prints all the commands ( add, remove, replace, list, exit )
    :param commands: dictionary
    :return: none
    """
    print(*list(commands.keys()), 'exit', sep='\n')


def run_command():

    commands = {'add': add, 'remove': remove, 'replace': replace, 'list': ui_list}
    expenses = initial_list()
    tests()
    while True:
        print_commands(commands)
        command_line = input("Enter command line: ")
        if command_line == "exit":
            break
        command, list_of_commands = get_command_and_list(command_line)
        try:
            commands[command](expenses, *list_of_commands)
        except KeyError:
            print("This option is not implemented yet!")
        except ValueError as ve:
            print("The following exception was:", ve)



############################################################## FUNCTION SECTION ######################################

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
    :return none:
    """
    person = create_expenses(apartment, amount, types)
    expenses.append(person)


def sort_expenses_by_number_of_apartment(expenses):
    """
    It sorts the expenses list by the number of apartment.
    :param expenses: list
    :return: none
    """
    return sorted(expenses, key=lambda x: x['number_of_apartment'])


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


def add(expenses, *list_of_commands):
    """
    It checks if the input is correct ( add <number of apartment> <type> <amount> ) and if it is, the function will add the input in expenses by using function add_expenses
    :param expenses: list
    :param *list_of_commands: a tuple read from keyboard.
    :return: none
    """
    list_of_commands = list(list_of_commands)   # convert from tuple to list
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
    add_expenses(expenses, number_of_apartment, amount, types)


def initial_list():
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


def remove(expenses, *list_of_commands):
    """
    It checks if the input is valid ( remove <apartment>
                                      remove <start apartment> to <end apartment>
                                      remove <type> ) and if it is, then it removes from expenses the apartment or
                                      the type or the apartments from a start to an end.
    :param expenses: list
    :param *list_of_commands: tuple
    :return: none
    """
    list_of_commands = list(list_of_commands)   # convert from tuple to list
    if len(list_of_commands) > 3:
        raise ValueError("Invalid input: you can insert maximum 3 arguments")
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


def replace(expenses, *list_of_commands):
    """
    It checks if the input is correct ( replace <apartment> <type> with <amount> ) and it removes the expenses from that apartment, type;
     and it adds the new one with the given parameters
    :param expenses: dictionary
    :param *list_of_commands: tuple
    :return: none
    """
    if len(list_of_commands) != 4:
        raise ValueError("Invalid input: you can insert only 4 arguments: replace <apartment> <type> with <amount>")
    list_of_commands = list(list_of_commands)
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

############################################################## Tests SECTION ######################################

def tests_add():
    test_expenses = []
    add(test_expenses, ('15'), ('gas'), ('200'))
    assert test_expenses == [create_expenses('15','200','gas')]
    add(test_expenses, ('17'), ('gas'), ('200'))
    assert test_expenses == [create_expenses('15','200','gas'), create_expenses('17', '200', 'gas')]
    add(test_expenses, ('13'), ('water'), ('186'))
    assert test_expenses == [create_expenses('15','200','gas'), create_expenses('17', '200', 'gas'), create_expenses('13', '186', 'water')]
    add(test_expenses, ('12'), ('heating'), ('1385'))
    assert test_expenses == [create_expenses('15','200','gas'), create_expenses('17', '200', 'gas'), create_expenses('13', '186', 'water'), create_expenses('12','1385','heating')]
    add(test_expenses, ('10'), ('other'), ('2654'))
    assert test_expenses == [create_expenses('15','200','gas'), create_expenses('17', '200', 'gas'), create_expenses('13', '186', 'water'), create_expenses('12','1385','heating'),
                             create_expenses('10','2654','other')]
    add(test_expenses, ('16'), ('electricity'), ('6548'))
    assert test_expenses == [create_expenses('15','200','gas'), create_expenses('17', '200', 'gas'), create_expenses('13', '186', 'water'), create_expenses('12','1385','heating'),
                             create_expenses('10','2654','other'), create_expenses('16','6548','electricity')]
    add(test_expenses, ('685'), ('other'), ('3247'))
    assert test_expenses == [create_expenses('15','200','gas'), create_expenses('17', '200', 'gas'), create_expenses('13', '186', 'water'), create_expenses('12','1385','heating'),
                             create_expenses('10','2654','other'), create_expenses('16','6548','electricity'), create_expenses('685','3247','other')]
    add(test_expenses, ('13'), ('water'), ('87986'))
    assert test_expenses == [create_expenses('15','200','gas'), create_expenses('17', '200', 'gas'), create_expenses('13', '186', 'water'), create_expenses('12','1385','heating'),
                             create_expenses('10','2654','other'), create_expenses('16','6548','electricity'), create_expenses('685','3247','other'), create_expenses('13','87986','water')]


def test_check_type():
    assert check_type("water")
    assert check_type("heating")
    assert check_type("electricity")
    assert check_type("gas")
    assert check_type("other")
    assert check_type("asdf") == False
    assert check_type("gAs")
    assert check_type("heATIng")
    assert check_type("WATER")
    assert check_type("HEATing")
    assert check_type("ELecTRiciTY")
    assert check_type("gaz") == False
    assert check_type("type") == False
    assert check_type("0ther") == False
    assert check_type("Other")
    assert check_type("heat") == False
    assert check_type("electric") == False


def test_remove():
    expenses = [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(16, 384, "electricity"),
            create_expenses(10, 1986, "water"),
            create_expenses(161, 6540, "gas"),
            create_expenses(618, 321, "heating"),
            create_expenses(156, 648, "water"),
            create_expenses(987, 213, "other"),
            create_expenses(10, 13, "electricity"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")]

    remove(expenses, ('10'))
    assert [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(16, 384, "electricity"),
            create_expenses(161, 6540, "gas"),
            create_expenses(618, 321, "heating"),
            create_expenses(156, 648, "water"),
            create_expenses(987, 213, "other"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")] == expenses

    remove(expenses, ('160'), ('to'), ('1000'))
    assert [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(16, 384, "electricity"),
            create_expenses(156, 648, "water"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")] == expenses

    remove(expenses, ('electricity'))
    assert [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(156, 648, "water"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water")] == expenses

    remove(expenses, ('12'))
    assert [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(156, 648, "water"),
            create_expenses(51, 7654, "other"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),] == expenses

    remove(expenses,('12'),('to'),('30'))
    assert [create_expenses(38, 34, "other"),
            create_expenses(156, 648, "water"),
            create_expenses(51, 7654, "other")] == expenses

    remove(expenses,('other'))
    assert [create_expenses(156, 648, "water")] == expenses

    remove(expenses,('156'))
    assert [] == expenses


def test_replace():
    expenses = [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(16, 384, "electricity"),
            create_expenses(10, 1986, "water"),
            create_expenses(161, 6540, "gas"),
            create_expenses(618, 321, "heating"),
            create_expenses(156, 648, "water"),
            create_expenses(987, 213, "other"),
            create_expenses(10, 13, "electricity"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")]

    replace(expenses, '10','electricity','with','775')
    assert [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(16, 384, "electricity"),
            create_expenses(10, 1986, "water"),
            create_expenses(161, 6540, "gas"),
            create_expenses(618, 321, "heating"),
            create_expenses(156, 648, "water"),
            create_expenses(987, 213, "other"),
            create_expenses(10, 775, "electricity"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")] == expenses

    replace(expenses, '987','other','with','4312')
    assert [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(16, 384, "electricity"),
            create_expenses(10, 1986, "water"),
            create_expenses(161, 6540, "gas"),
            create_expenses(618, 321, "heating"),
            create_expenses(156, 648, "water"),
            create_expenses(987, 4312, "other"),
            create_expenses(10, 775, "electricity"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")] == expenses

    replace(expenses, '10', 'water', 'with', '65')
    assert [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(16, 384, "electricity"),
            create_expenses(10, 65, "water"),
            create_expenses(161, 6540, "gas"),
            create_expenses(618, 321, "heating"),
            create_expenses(156, 648, "water"),
            create_expenses(987, 4312, "other"),
            create_expenses(10, 775, "electricity"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")] == expenses

    replace(expenses, '161', 'gas', 'with', '79')
    assert [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(16, 384, "electricity"),
            create_expenses(10, 65, "water"),
            create_expenses(161, 79, "gas"),
            create_expenses(618, 321, "heating"),
            create_expenses(156, 648, "water"),
            create_expenses(987, 4312, "other"),
            create_expenses(10, 775, "electricity"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")] == expenses

    replace(expenses, '16', 'heating', 'with', '98')
    assert [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(16, 384, "electricity"),
            create_expenses(10, 65, "water"),
            create_expenses(161, 79, "gas"),
            create_expenses(618, 321, "heating"),
            create_expenses(156, 648, "water"),
            create_expenses(987, 4312, "other"),
            create_expenses(10, 775, "electricity"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 98, "heating"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")] == expenses


def test_sum():
    expenses = [create_expenses(17, 19, "gas"),
            create_expenses(13, 34, "other"),
            create_expenses(16, 384, "electricity"),
            create_expenses(10, 1986, "water"),
            create_expenses(15, 6540, "gas"),
            create_expenses(12, 321, "heating"),
            create_expenses(13, 648, "water"),
            create_expenses(12, 213, "other"),
            create_expenses(10, 13, "electricity"),
            create_expenses(16, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")]

    assert sum_of_all_expenses_for_an_apartment(expenses,"10") == 1999
    assert sum_of_all_expenses_for_an_apartment(expenses,"11") == False
    assert sum_of_all_expenses_for_an_apartment(expenses,"12") == 550
    assert sum_of_all_expenses_for_an_apartment(expenses,"13") == 747
    assert sum_of_all_expenses_for_an_apartment(expenses,"14") == 168
    assert sum_of_all_expenses_for_an_apartment(expenses,"15") == 6540
    assert sum_of_all_expenses_for_an_apartment(expenses,"16") == 8088
    assert sum_of_all_expenses_for_an_apartment(expenses,"17") == 19
    assert sum_of_all_expenses_for_an_apartment(expenses,"18") == False
    assert sum_of_all_expenses_for_an_apartment(expenses,"19") == 561

def tests():
    tests_add()
    test_check_type()
    test_sum()
    test_remove()
    test_replace()

############################################################## Main SECTION ######################################

if __name__ == '__main__':
    run_command()

