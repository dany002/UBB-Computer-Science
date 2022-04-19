from copy import deepcopy

class Repository:
    def __init__(self):
        self.__history_of_complex_numbers = []
        self.__complex_numbers = []

    def add_a_complex_number(self, the_complex_number_that_is_going_to_be_added):
        """
        It adds a complex number to the repository.
        :param the_complex_number_that_is_going_to_be_added: ComplexNumber
        :return: none
        """
        self.__history_of_complex_numbers.append(deepcopy(self.__complex_numbers))
        self.__complex_numbers.append(the_complex_number_that_is_going_to_be_added)

    def remove_a_lot_of_complex_numbers(self, start, end):
        """
        It removes complex numbers from the repository.
        :param start: int
        :param end: int
        :return: none
        """
        self.__history_of_complex_numbers.append(deepcopy(self.__complex_numbers))
        if int(start) > int(end):
            raise ValueError("Start is greater than end!")
        start = int(start)
        end = int(end)
        if start == 0:
            self.__history_of_complex_numbers.pop()
        while start < end:
            del self.__complex_numbers[start]
            end -= 1

    def undo(self):
        """
        It undo the last operation.
        :return: none
        """
        if len(self.__history_of_complex_numbers) == 0:
            raise ValueError("You can't undo anymore!")

        self.__complex_numbers[:] = self.__history_of_complex_numbers[-1]
        self.__history_of_complex_numbers.pop()

    def list(self):
        """
        It gets the list of complex numbers
        :return: the list
        """
        return self.__complex_numbers

    def __len__(self):
        """
        It gets the length of complex numbers
        :return: the length
        """
        return len(self.__complex_numbers)

    def get_index(self, index):
        """
        It gets the complex number from a given index in the list.
        :param index: int
        :return: the complex number
        """
        return self.__complex_numbers[index]