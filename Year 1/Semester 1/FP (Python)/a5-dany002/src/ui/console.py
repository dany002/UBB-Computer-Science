from services.functions import ComplexNumberService
from tests.tests import Test
import random

class UI:
    def __init__(self):
        self.__services = ComplexNumberService()
        self.__commands = {'add': self.ui_add_number, 'print': self.print_all_numbers, 'undo': self.__services.undo, 'filter': self.__services.filter}

    def _print_menu(self):
        print("Choose one from the following:")
        print("   <add> for adding a complex number")
        print("   <print> to print all the list.")
        print("   <undo> to undo the last operation")
        print("   <filter> to filter the list between 2 given indices ( start and end )")
        print("   <exit> to close it.")

    def get_command_and_list(self, command_line):
        position = command_line.find(' ')
        if position == -1:
            return command_line, []
        command = command_line[:position]
        self.list_of_commands = command_line[position:]
        self.list_of_commands = self.list_of_commands.split(' ')
        self.list_of_commands = [elements.strip() for elements in self.list_of_commands]  # now is a list
        del self.list_of_commands[0]  # the first element is ''
        return command, self.list_of_commands


    def run_command(self):
        Test()
        random_number = random.Random(420)

        for i in range(10):
            self.__services.add_complex_number(random_number.randint(-10, 10), random_number.randint(-10, 10))  # generate 10 random numbers
        while True:
            self._print_menu()
            command_line = input("Enter command line: ")
            if command_line == "exit":
                break
            command, list_of_commands = self.get_command_and_list(command_line)
            try:
                if command in ['undo']:
                    if list_of_commands == []:
                        self.__services.undo()
                    else:
                        raise TypeError
                elif command in ['add', 'filter']:
                    self.__commands[command](*list_of_commands)
                else:
                    self.__commands[command](*list_of_commands)
            except KeyError:
                print("This option is not implemented yet!")
            except ValueError as ve:
                print("The following exception was:", ve)
            except TypeError:
                print("Incorrect input!")

    def check_real_number(self, number):  # example case: z=32 or z=235
        if number.find("i") == -1:
            imaginary_part = 0
            real_part = int(number)
            self.__services.add_complex_number(real_part, imaginary_part)
            return True
        return False

    def check_if_the_number_has_the_coefficient_1_for_imaginary_part(self, number):  # example case: z=3+i or z=123+i
        if number.find("+") != -1:
            if number[len(number) - 1] == "+":
                imaginary_part = 1
                split_number = number.split("+")
                real_part = int(split_number[0])
                self.__services.add_complex_number(real_part, imaginary_part)
                return True
        return False

    def check_if_the_imaginary_part_is_negative(self, number):
        if number.find("-") != -1:
            if number[len(number) - 1] == "-":
                if len(number) == 1:  # checks for case -i and Re(Z) = 0
                    imaginary_part = -1
                    real_part = 0
                    self.__services.add_complex_number(real_part, imaginary_part)
                elif len(number) == 2:
                    imaginary_part = -1
                    var = number.split("-")
                    real_part = int(var[0])
                    self.__services.add_complex_number(real_part, imaginary_part)
                elif len(number) == 3:  # checks if both are negative and the second one is -i
                    imaginary_part = -1
                    var = number.split("-")
                    real_part = -int(var[1])
                    self.__services.add_complex_number(real_part, imaginary_part)
                return True
        return False

    def check_if_the_number_has_only_imaginary_coefficient_for_a_given_number(self, number):
        if number.find("+") == -1 and number.find("-") == -1:  # no +/- in the number, example: z=17i or z=i
            real_part = 0
            if number != "":  # checks for case i
                imaginary_part = int(number)
            else:
                imaginary_part = 1
            self.__services.add_complex_number(real_part, imaginary_part)
            return True
        return False

    def check_if_both_real_part_and_imaginary_part_are_negative(self, new_number):  # example: z=-2-35i
        if len(new_number) == 3:
            real_part = -int(new_number[1])  # negative
            imaginary_part = -int(new_number[2])  # negative
            self.__services.add_complex_number(real_part, imaginary_part)
            return True
        return False

    def check_if_imaginary_part_is_negative(self, new_number):  # example: z=3-2i
        if new_number[0] != "":
            real_part = int(new_number[0])  # this one is positive
        else:
            real_part = 0
        imaginary_part = -int(new_number[1])  # this one is negative
        self.__services.add_complex_number(real_part, imaginary_part)

    def check_if_the_both_parts_are_positives(self, number):  # example: z=4+512i
        new_number = number.split("+")
        real_part = int(new_number[0])
        imaginary_part = int(new_number[1])
        self.__services.add_complex_number(real_part, imaginary_part)

    def ui_add_number(self):
        number = input("Z=")

        if self.check_real_number(number) == True:
            return

        number = number.replace("i", "")  # no more i, we dont need letters in a number !

        if self.check_if_the_number_has_the_coefficient_1_for_imaginary_part(number) == True:
            return

        if self.check_if_the_imaginary_part_is_negative(number) == True:
            return

        if self.check_if_the_number_has_only_imaginary_coefficient_for_a_given_number(number) == True:
            return

        if number.find("+") == -1:
            new_number = number.split("-")
            if self.check_if_both_real_part_and_imaginary_part_are_negative(new_number) == True:
                return

            self.check_if_imaginary_part_is_negative(new_number)
            return

        self.check_if_the_both_parts_are_positives(number)
        return



    def print_check_if_the_coefficient_of_imaginary_part_is_one(self, i):  # example case: z=4+i or z=i
        complex_number = self.__services.get_index(i)
        if complex_number.imaginary_part == 1:
            if complex_number.real_part != 0:
                print("Z=", complex_number.real_part, "+i", sep='')
                return True
            print("Z=i")
            return True
        return False

    def print_check_if_the_coefficient_of_imaginary_part_is_minus_one(self, i):  # example case: z=2-i or z=-i
        complex_number = self.__services.get_index(i)
        if complex_number.imaginary_part == -1:
            if complex_number.real_part != 0:
                print("Z=", complex_number.real_part, "-i", sep='')
                return True
            print("Z=-i")
            return True
        return False

    def print_check_if_the_imaginary_part_is_positive(self, i):  # example case: z=3+2i or z=5i
        complex_number = self.__services.get_index(i)
        if complex_number.imaginary_part > 0:
            if complex_number.real_part != 0:
                print("Z=", complex_number.real_part, "+", complex_number.imaginary_part, "i", sep='')  # no spaces
                return True

            print("Z=", complex_number.imaginary_part, "i", sep='')  # no spaces, no real number
            return True
        return False

    def print_check_if_the_imaginary_part_is_negative(self, i):  # example case: z=4-5i or z=-2i
        complex_number = self.__services.get_index(i)
        if complex_number.imaginary_part < 0:
            if complex_number.real_part != 0:
                print("Z=", complex_number.real_part, complex_number.imaginary_part, "i", sep='')  # no spaces
                return True
            print("Z=", complex_number.imaginary_part, "i", sep='')  # no spaces, no real number
            return True
        return False

    def print_check_if_the_number_is_a_real_number(self, i):  # example case: z=24 or z=0
        complex_number = self.__services.get_index(i)
        if complex_number.imaginary_part == 0:
            print("Z=", complex_number.real_part, sep='')  # no spaces
            return True
        return False

    def print_all_numbers(self):
        self.print_numbers(0, self.__services.get_number_of_complex_numbers())

    def print_numbers(self, start, final):
        if start >= final:
            print("There aren't any elements with the given property.")
        for index_in_the_list in range(start, final):
            if self.print_check_if_the_coefficient_of_imaginary_part_is_one(index_in_the_list) == True:
                continue

            if self.print_check_if_the_coefficient_of_imaginary_part_is_minus_one(index_in_the_list) == True:
                continue

            if self.print_check_if_the_imaginary_part_is_positive(index_in_the_list) == True:
                continue

            if self.print_check_if_the_imaginary_part_is_negative(index_in_the_list) == True:
                continue

            if self.print_check_if_the_number_is_a_real_number(index_in_the_list) == True:
                continue