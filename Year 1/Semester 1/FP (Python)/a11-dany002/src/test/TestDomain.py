import unittest

from domain.Validators import NotNumber, NotInTheRangeAJ, NotInTheRange, IsNumber, CheckIfTheSecondCoordinateIsRight, CheckIfTheFirstCoordinateIsRight

class TestDomain(unittest.TestCase):

    def test_CheckIfTheFirstCoordinateIsRight__raise_exception_NotNumber__the_first_coordinate_is_not_a_number(self):
        with self.assertRaises(NotNumber):
            CheckIfTheFirstCoordinateIsRight.validate("1o")

    def test_CheckIfTheFirstCoordinateIsRight__raise_exception_NotInTheRange__the_first_coordinate_is_not_between_1_and_10(self):
        with self.assertRaises(NotInTheRange):
            CheckIfTheFirstCoordinateIsRight.validate("12")

    def test_CheckIfTheSecondCoordinateIsRight__raise_exception_IsNumber__the_second_coordinate_is_a_number(self):
        with self.assertRaises(IsNumber):
            CheckIfTheSecondCoordinateIsRight.validate("5")

    def test_CheckIfTheSecondCoordinateIsRight__raise_exception_NotInTheRangeAJ__the_second_coordinate_is_not_between_A_and_J(self):
        with self.assertRaises(NotInTheRangeAJ):
            CheckIfTheSecondCoordinateIsRight.validate('M')
