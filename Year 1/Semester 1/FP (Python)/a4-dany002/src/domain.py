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
