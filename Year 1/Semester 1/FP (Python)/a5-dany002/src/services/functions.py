
from repository.Repository import Repository
from domain.ComplexNumber import ComplexNumber

class ComplexNumberService:
    def __init__(self):
        self.__repository = Repository()

    def add_complex_number(self, real_part, imaginary_part):
        self.__repository.add_a_complex_number(ComplexNumber(real_part, imaginary_part))

    def filter(self, start, end):
        start = int(start)
        end = int(end)
        if end + 1 > len(self.__repository):
            raise ValueError("The end is greater than the length of complex numbers!")
        if start > end:
            raise ValueError("Start is greater than end")
        self.__repository.remove_a_lot_of_complex_numbers(end+1,len(self.__repository))
        self.__repository.remove_a_lot_of_complex_numbers(0,start)



    def undo(self):
        self.__repository.undo()

    def list(self):
        return self.__repository.list()

    def get_number_of_complex_numbers(self):
        return len(self.__repository)

    def get_index(self, index):
        return self.__repository.get_index(index)