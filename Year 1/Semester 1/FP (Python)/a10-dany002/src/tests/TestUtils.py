import unittest
from Utils.Utils import Utils
class TestUtils(unittest.TestCase):
    def setUp(self) -> None:
        self.list_of_elements = []

    def tearDown(self) -> None:
        pass

    def test_shellSort__with_valid_data__is_going_to_return_the_list_sorted_ascending(self):
        self.list_of_elements.append(15)
        self.list_of_elements.append(17)
        self.list_of_elements.append(13)
        self.list_of_elements.append(15)
        self.list_of_elements.append(-8)
        self.list_of_elements.append(-9)
        self.list_of_elements.append(30)
        self.list_of_elements = Utils.shellSort(self.list_of_elements, lambda first_element, second_element: -1 if first_element < second_element else (0 if first_element == second_element else 1))
        list_of_sorted_elements = []
        list_of_sorted_elements.append(-9)
        list_of_sorted_elements.append(-8)
        list_of_sorted_elements.append(13)
        list_of_sorted_elements.append(15)
        list_of_sorted_elements.append(15)
        list_of_sorted_elements.append(17)
        list_of_sorted_elements.append(30)
        self.assertEqual(self.list_of_elements, list_of_sorted_elements)

    def test_filter__with_valid_data__is_going_to_keep_only_the_elements_that_validate_as_true(self):
        self.list_of_elements.append(15)
        self.list_of_elements.append(17)
        self.list_of_elements.append(13)
        self.list_of_elements.append(15)
        self.list_of_elements.append(-8)
        self.list_of_elements.append(-9)
        self.list_of_elements.append(30)
        self.list_of_elements = Utils.filter(self.list_of_elements, lambda element: element > 0)
        list_of_filtered_elements = []
        list_of_filtered_elements.append(15)
        list_of_filtered_elements.append(17)
        list_of_filtered_elements.append(13)
        list_of_filtered_elements.append(15)
        list_of_filtered_elements.append(30)
        self.assertEqual(self.list_of_elements, list_of_filtered_elements)