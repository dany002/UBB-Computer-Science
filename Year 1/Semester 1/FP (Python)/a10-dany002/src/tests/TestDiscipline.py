import unittest

from domain.Discipline import Discipline

class TestDiscipline(unittest.TestCase):

    def test_discipline__with_valid_data__setters_and_getters(self):
        discipline = Discipline(23,"Math")
        self.assertEqual(discipline.discipline_id, 23)
        self.assertEqual(discipline.name, "Math")
        discipline.discipline_id = 48
        discipline.name = "FP"
        self.assertEqual(discipline.discipline_id, 48)
        self.assertEqual(discipline.name, "FP")

    def test_str__with_valid_data__is_going_to_print_in_a_specific_format(self):
        discipline = Discipline(23,"Math")
        self.assertEqual(str(discipline), 'Discipline id: 23  Discipline name: Math')

    def test_eq__with_valid_data__is_going_to_check_if_two_disciplines_are_equal_or_not(self):
        discipline = Discipline(23,"Math")
        another_discipline = Discipline(23,"Math")
        self.assertEqual(discipline, another_discipline)
        another_discipline_not_equal = Discipline(43,"FP")
        self.assertNotEqual(discipline, another_discipline_not_equal)

    def test_discipline(self):
        self.test_discipline__with_valid_data__setters_and_getters()
        self.test_eq__with_valid_data__is_going_to_check_if_two_disciplines_are_equal_or_not()
        self.test_str__with_valid_data__is_going_to_print_in_a_specific_format()