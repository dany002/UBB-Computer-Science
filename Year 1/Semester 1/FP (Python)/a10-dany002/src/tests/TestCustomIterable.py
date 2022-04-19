import unittest

from Utils.CustomIterable import CustomIterable


class TestCustomIterable(unittest.TestCase):
    def setUp(self) -> None:
        self.element = CustomIterable()

    def tearDown(self) -> None:
        pass

    def test_setItem__with_valid_data__is_going_to_set_the_given_value_for_a_key(self):
        self.element.append(0)
        self.element[0] = 1
        self.assertEqual(self.element[0], 1)

    def test_delItem__with_valid_data__is_going_to_remove_the_element_from_the_list(self):
        self.element.append(1)
        self.element.append(2)
        self.element.append(3)
        del self.element[1]
        list_of_expected_elements = CustomIterable()
        list_of_expected_elements.append(1)
        list_of_expected_elements.append(3)
        self.assertEqual(self.element, list_of_expected_elements)

    def test_iter_and_next__with_valid_data__is_going_to_parse_all_the_elements_and_it_checks_if_it_s_okay(self):
        index_of_the_element_that_is_being_iterated = 0
        self.element.append(1)
        self.element.append(2)
        self.element.append(3)
        for the_element_that_is_being_iterated in self.element:
            self.assertEqual(the_element_that_is_being_iterated, self.element[index_of_the_element_that_is_being_iterated])
            index_of_the_element_that_is_being_iterated += 1

    def test_length__with_valid_data__is_going_to_return_the_length_of_the_iterable(self):
        self.element.append(1)
        self.element.append(2)
        self.element.append(3)
        self.element.append(4)
        self.element.append(5)
        self.assertEqual(len(self.element), 5)

    def test_not_eqaul__with_valid_data__is_going_to_return_false(self):
        self.element.append(1)
        self.element.append(2)
        self.element.append(3)
        self.element.append(4)
        list_of_elements = CustomIterable()
        list_of_elements.append(1)
        list_of_elements.append(2)
        list_of_elements.append(3)
        list_of_elements.append(4)
        list_of_elements.append(1)
        self.assertNotEqual(self.element, list_of_elements)