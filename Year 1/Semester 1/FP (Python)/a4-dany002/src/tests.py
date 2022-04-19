
from functions import add, create_expenses, check_type, remove, replace, sum_of_all_expenses_for_an_apartment, sort_expenses_by_number_of_apartment, sort_expenses_by_type, \
    find_apartment, sum_for_a_given_type, maximum_amount_per_each_expense_type_for_a_given_apartment, filter_by_type, filter_by_value

def tests_add():
    test_expenses = []
    history_of_expenses = []
    add(history_of_expenses, test_expenses, ('15'), ('gas'), ('200'))
    assert test_expenses == [create_expenses('15','200','gas')]
    add(history_of_expenses, test_expenses, ('17'), ('gas'), ('200'))
    assert test_expenses == [create_expenses('15','200','gas'), create_expenses('17', '200', 'gas')]
    add(history_of_expenses, test_expenses, ('13'), ('water'), ('186'))
    assert test_expenses == [create_expenses('15','200','gas'), create_expenses('17', '200', 'gas'), create_expenses('13', '186', 'water')]
    add(history_of_expenses, test_expenses, ('12'), ('heating'), ('1385'))
    assert test_expenses == [create_expenses('15','200','gas'), create_expenses('17', '200', 'gas'), create_expenses('13', '186', 'water'), create_expenses('12','1385','heating')]
    add(history_of_expenses, test_expenses, ('10'), ('other'), ('2654'))
    assert test_expenses == [create_expenses('15','200','gas'), create_expenses('17', '200', 'gas'), create_expenses('13', '186', 'water'), create_expenses('12','1385','heating'),
                             create_expenses('10','2654','other')]
    add(history_of_expenses, test_expenses, ('16'), ('electricity'), ('6548'))
    assert test_expenses == [create_expenses('15','200','gas'), create_expenses('17', '200', 'gas'), create_expenses('13', '186', 'water'), create_expenses('12','1385','heating'),
                             create_expenses('10','2654','other'), create_expenses('16','6548','electricity')]
    add(history_of_expenses, test_expenses, ('685'), ('other'), ('3247'))
    assert test_expenses == [create_expenses('15','200','gas'), create_expenses('17', '200', 'gas'), create_expenses('13', '186', 'water'), create_expenses('12','1385','heating'),
                             create_expenses('10','2654','other'), create_expenses('16','6548','electricity'), create_expenses('685','3247','other')]
    add(history_of_expenses, test_expenses, ('13'), ('water'), ('87986'))
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
    history_of_expenses = []
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
    remove(history_of_expenses, expenses, ('10'))
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

    remove(history_of_expenses,expenses, ('160'), ('to'), ('1000'))
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

    remove(history_of_expenses,expenses, ('electricity'))
    assert [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(156, 648, "water"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water")] == expenses

    remove(history_of_expenses,expenses, ('12'))
    assert [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(156, 648, "water"),
            create_expenses(51, 7654, "other"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),] == expenses

    remove(history_of_expenses,expenses,('12'),('to'),('30'))
    assert [create_expenses(38, 34, "other"),
            create_expenses(156, 648, "water"),
            create_expenses(51, 7654, "other")] == expenses

    remove(history_of_expenses,expenses,('other'))
    assert [create_expenses(156, 648, "water")] == expenses

    remove(history_of_expenses, expenses,('156'))
    assert [] == expenses


def test_replace():
    history_of_expenses = []

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

    replace(history_of_expenses, expenses, '10','electricity','with','775')
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

    replace(history_of_expenses, expenses, '987','other','with','4312')
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

    replace(history_of_expenses, expenses, '10', 'water', 'with', '65')
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

    replace(history_of_expenses, expenses, '161', 'gas', 'with', '79')
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

    replace(history_of_expenses, expenses, '16', 'heating', 'with', '98')
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


def test_sum_of_all_expenses_for_an_apartment():
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


def test_sort():
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

    expenses = sort_expenses_by_number_of_apartment(expenses)
    assert [create_expenses(10, 1986, "water"),
            create_expenses(10, 13, "electricity"),
            create_expenses(12, 16, "gas"),
            create_expenses(13, 65, "water"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 384, "electricity"),
            create_expenses(16, 50, "heating"),
            create_expenses(17, 19, "gas"),
            create_expenses(19, 561, "electricity"),
            create_expenses(38, 34, "other"),
            create_expenses(51, 7654, "other"),
            create_expenses(156, 648, "water"),
            create_expenses(161, 6540, "gas"),
            create_expenses(618, 321, "heating"),
            create_expenses(987, 213, "other")] == expenses

    expenses = sort_expenses_by_type(expenses)
    assert [create_expenses(10, 13, "electricity"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 384, "electricity"),
            create_expenses(19, 561, "electricity"),
            create_expenses(12, 16, "gas"),
            create_expenses(17, 19, "gas"),
            create_expenses(161, 6540, "gas"),
            create_expenses(16, 50, "heating"),
            create_expenses(618, 321, "heating"),
            create_expenses(38, 34, "other"),
            create_expenses(51, 7654, "other"),
            create_expenses(987, 213, "other"),
            create_expenses(10, 1986, "water"),
            create_expenses(13, 65, "water"),
            create_expenses(156, 648, "water")] == expenses


def test_find_apartment():
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
    assert find_apartment(expenses, 10)
    assert find_apartment(expenses, 11) == False
    assert find_apartment(expenses, 12)
    assert find_apartment(expenses, 13)
    assert find_apartment(expenses, 14)
    assert find_apartment(expenses, 15)
    assert find_apartment(expenses, 16)
    assert find_apartment(expenses, 17)
    assert find_apartment(expenses, 18) == False
    assert find_apartment(expenses, 19)


def test_sum_for_a_given_type():
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
    assert sum_for_a_given_type(expenses, "gas") == 6575
    assert sum_for_a_given_type(expenses, "electricity") == 1126
    assert sum_for_a_given_type(expenses, "other") == 7901
    assert sum_for_a_given_type(expenses, "water") == 2699
    assert sum_for_a_given_type(expenses, "heating") == 371


def test_maximum_amount_per_each_expense_type_for_a_given_apartment():
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

    assert maximum_amount_per_each_expense_type_for_a_given_apartment(expenses, ("10")) ==\
           [{'type': 'gas', 'amount': 0}, {'type': 'water', 'amount': 1986},
            {'type': 'heating', 'amount': 0}, {'type': 'other', 'amount': 0},
            {'type': 'electricity', 'amount': 13}]

    assert maximum_amount_per_each_expense_type_for_a_given_apartment(expenses, ("12")) == \
           [{'type': 'gas', 'amount': 16}, {'type': 'water', 'amount': 0},
            {'type': 'heating', 'amount': 321}, {'type': 'other', 'amount': 213},
            {'type': 'electricity', 'amount': 0}]

    assert maximum_amount_per_each_expense_type_for_a_given_apartment(expenses, ("13")) == \
           [{'type': 'gas', 'amount': 0}, {'type': 'water', 'amount': 648},
            {'type': 'heating', 'amount': 0}, {'type': 'other', 'amount': 34},
            {'type': 'electricity', 'amount': 0}]

    assert maximum_amount_per_each_expense_type_for_a_given_apartment(expenses, ("14")) ==\
           [{'type': 'gas', 'amount': 0}, {'type': 'water', 'amount': 0},
            {'type': 'heating', 'amount': 0}, {'type': 'other', 'amount': 0},
            {'type': 'electricity', 'amount': 168}]

    assert maximum_amount_per_each_expense_type_for_a_given_apartment(expenses, ("15")) == \
           [{'type': 'gas', 'amount': 6540}, {'type': 'water', 'amount': 0},
            {'type': 'heating', 'amount': 0}, {'type': 'other', 'amount': 0},
            {'type': 'electricity', 'amount': 0}]

    assert maximum_amount_per_each_expense_type_for_a_given_apartment(expenses, ("16")) ==\
           [{'type': 'gas', 'amount': 0}, {'type': 'water', 'amount': 0},
            {'type': 'heating', 'amount': 50}, {'type': 'other', 'amount': 7654},
            {'type': 'electricity', 'amount': 384}]

    assert maximum_amount_per_each_expense_type_for_a_given_apartment(expenses, ("17")) == \
           [{'type': 'gas', 'amount': 19}, {'type': 'water', 'amount': 0},
            {'type': 'heating', 'amount': 0}, {'type': 'other', 'amount': 0},
            {'type': 'electricity', 'amount': 0}]

    assert maximum_amount_per_each_expense_type_for_a_given_apartment(expenses, ("19")) ==\
           [{'type': 'gas', 'amount': 0}, {'type': 'water', 'amount': 0},
            {'type': 'heating', 'amount': 0}, {'type': 'other', 'amount': 0},
            {'type': 'electricity', 'amount': 561}]


def test_filter_type():

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

    filter_by_type(expenses,"electricity")
    assert [create_expenses(16, 384, "electricity"),
            create_expenses(10, 13, "electricity"),
            create_expenses(14, 168, "electricity"),
            create_expenses(19, 561, "electricity")] == expenses


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

    filter_by_type(expenses,"gas")
    assert [create_expenses(17, 19, "gas"),
            create_expenses(161, 6540, "gas"),
            create_expenses(12, 16, "gas")] == expenses


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

    filter_by_type(expenses, "heating")
    assert [create_expenses(618, 321, "heating"),
            create_expenses(16, 50, "heating")] == expenses


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

    filter_by_type(expenses, "other")
    assert [create_expenses(38, 34, "other"),
            create_expenses(987, 213, "other"),
            create_expenses(51, 7654, "other")] == expenses


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
    filter_by_type(expenses, "water")
    assert [create_expenses(10, 1986, "water"),
            create_expenses(156, 648, "water"),
            create_expenses(13, 65, "water")] == expenses


def test_filter_value():
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

    filter_by_value(expenses,["1000"])
    assert [create_expenses(17, 19, "gas"),
            create_expenses(13, 34, "other"),
            create_expenses(12, 321, "heating"),
            create_expenses(13, 648, "water"),
            create_expenses(12, 213, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")] == expenses

    filter_by_value(expenses,["900"])
    assert [create_expenses(17, 19, "gas"),
            create_expenses(13, 34, "other"),
            create_expenses(12, 321, "heating"),
            create_expenses(13, 648, "water"),
            create_expenses(12, 213, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")] == expenses

    filter_by_value(expenses,["800"])
    assert [create_expenses(17, 19, "gas"),
            create_expenses(13, 34, "other"),
            create_expenses(12, 321, "heating"),
            create_expenses(13, 648, "water"),
            create_expenses(12, 213, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")] == expenses

    filter_by_value(expenses,["700"])
    assert [create_expenses(17, 19, "gas"),
            create_expenses(12, 321, "heating"),
            create_expenses(12, 213, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(19, 561, "electricity")] == expenses

    filter_by_value(expenses,["600"])
    assert [create_expenses(17, 19, "gas"),
            create_expenses(12, 321, "heating"),
            create_expenses(12, 213, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(19, 561, "electricity")] == expenses

    filter_by_value(expenses,["500"])
    assert [create_expenses(17, 19, "gas"),
            create_expenses(14, 168, "electricity")] == expenses

    filter_by_value(expenses,["400"])
    assert [create_expenses(17, 19, "gas"),
            create_expenses(14, 168, "electricity")] == expenses

    filter_by_value(expenses, ["300"])
    assert [create_expenses(17, 19, "gas"),
            create_expenses(14, 168, "electricity")] == expenses

    filter_by_value(expenses, ["200"])
    assert [create_expenses(17, 19, "gas"),
            create_expenses(14, 168, "electricity")] == expenses

    filter_by_value(expenses, ["100"])
    assert [create_expenses(17, 19, "gas")] == expenses

    filter_by_value(expenses, ["0"])
    assert [] == expenses

def tests():
    tests_add()
    test_check_type()
    test_sum_of_all_expenses_for_an_apartment()
    test_sum_for_a_given_type()
    test_remove()
    test_replace()
    test_sort()
    test_find_apartment()
    test_maximum_amount_per_each_expense_type_for_a_given_apartment()
    test_filter_type()
    test_filter_value()



