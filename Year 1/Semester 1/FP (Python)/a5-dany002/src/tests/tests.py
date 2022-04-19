from services.functions import ComplexNumberService
from domain.ComplexNumber import ComplexNumber


def test_add_a_complex_number__with_valid_data__is_going_to_be_added_in_the_class():
    service = ComplexNumberService()
    the_list_of_expected_complex_numbers = []
    service.add_complex_number(65,-54)
    the_list_of_expected_complex_numbers.append(ComplexNumber(65,-54))
    assert the_list_of_expected_complex_numbers == service.list()


def test_add_a_complex_number__raise_exception():
    service = ComplexNumberService()
    try:
        service.add_complex_number("what's going on", "rip")
        assert False
    except Exception:
        assert True

def test_add_a_complex_number():
    test_add_a_complex_number__with_valid_data__is_going_to_be_added_in_the_class()
    test_add_a_complex_number__raise_exception()


def test_filter__with_valid_data__keeps_the_numbers_between_start_and_end():
    service = ComplexNumberService()
    service.add_complex_number(5,7)
    service.add_complex_number(17,3)
    service.add_complex_number(12,124)
    service.add_complex_number(0,-123)
    service.add_complex_number(-4,-5)
    service.add_complex_number(7,0)
    service.filter(1,3)
    the_list_of_expected_complex_numbers = []
    the_list_of_expected_complex_numbers.append(ComplexNumber(17,3))
    the_list_of_expected_complex_numbers.append(ComplexNumber(12,124))
    the_list_of_expected_complex_numbers.append(ComplexNumber(0,-123))
    assert the_list_of_expected_complex_numbers == service.list()


def test_filter_raise_exception__start_is_greater_than_the_end():
    try:
        service = ComplexNumberService()
        service.add_complex_number(13, 2)
        service.add_complex_number(65, 12)
        service.add_complex_number(1, 1)
        service.add_complex_number(0, -1)
        service.add_complex_number(65, 198)
        service.add_complex_number(321, 69)
        service.add_complex_number(156, 21)
        service.add_complex_number(65, -2)
        service.add_complex_number(-4, 65)
        service.add_complex_number(564, 18)
        service.filter(45, 30)
        assert False
    except Exception:
        assert True


def test_filter():
    test_filter__with_valid_data__keeps_the_numbers_between_start_and_end()
    test_filter_raise_exception__start_is_greater_than_the_end()

def test_undo_with_valid_data():
    service = ComplexNumberService()
    service.add_complex_number(5, 7)
    service.add_complex_number(17, 3)
    service.add_complex_number(12, 124)
    service.add_complex_number(0, -123)
    service.add_complex_number(-4, -5)
    service.add_complex_number(7, 0)
    service.add_complex_number(13, 2)
    service.add_complex_number(65, 12)
    service.add_complex_number(1, 1)
    service.add_complex_number(0, -1)
    service.add_complex_number(65, 198)
    service.add_complex_number(321, 69)
    service.add_complex_number(156, 21)
    service.filter(1, 3)
    service.undo()
    the_list_of_expected_numbers = []
    the_list_of_expected_numbers.append(ComplexNumber(5,7))
    the_list_of_expected_numbers.append(ComplexNumber(17,3))
    the_list_of_expected_numbers.append(ComplexNumber(12,124))
    the_list_of_expected_numbers.append(ComplexNumber(0,-123))
    the_list_of_expected_numbers.append(ComplexNumber(-4,-5))
    the_list_of_expected_numbers.append(ComplexNumber(7,0))
    the_list_of_expected_numbers.append(ComplexNumber(13,2))
    the_list_of_expected_numbers.append(ComplexNumber(65,12))
    the_list_of_expected_numbers.append(ComplexNumber(1,1))
    the_list_of_expected_numbers.append(ComplexNumber(0,-1))
    the_list_of_expected_numbers.append(ComplexNumber(65,198))
    the_list_of_expected_numbers.append(ComplexNumber(321,69))
    the_list_of_expected_numbers.append(ComplexNumber(156,21))
    assert the_list_of_expected_numbers == service.list()

def test_undo_raise_exception_length_is_zero():
    try:
        service = ComplexNumberService()
        service.undo()
        assert False
    except Exception:
        assert True

def test_undo():
    test_undo_with_valid_data()
    test_undo_raise_exception_length_is_zero()


def Test():
    test_add_a_complex_number()
    test_filter()
    test_undo()
