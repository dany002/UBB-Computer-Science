#
# Write the implementation for A2 in this file
#
import random


################################################### DOMAIN ##################################################

def create_complex(real, imaginary):
    return {'real': real, 'imag': imaginary}


def get_real(complex):
    return complex['real']


def get_imaginary(complex):
    return complex['imag']


def set_real(complex, real):
    complex['real'] = real


def set_imaginary(complex, imaginary):
    complex['imag'] = imaginary


############################################# UI ###########################################################

# UI section
# (write all functions that have input or print statements here).
# Ideally, this section should not contain any calculations relevant to program functionalities

def run_menu():
    random_number = random.Random(420)
    complex = []
    for i in range(10):
       complex.append(create_complex(random_number.randint(-10,10),random_number.randint(-10,10))) # generate 10 random numbers
    options = {1: ui_add_number, 2: print_all_numbers, 3: difference_between_2_consecutive_modulus_prime, 4: modulus_in_range_1_10}
    while True:
        print_menu_options()
        opt = input("What is your option? ")
        if opt == 'x':
            break
        opt = int(opt)
        options[opt](complex)



def print_check_imaginary_i ( complex, i ): # example case: z=4+i or z=i
    token = complex[i]
    if get_imaginary(token) == 1:
        if get_real(token) != 0:
            print("Z=", get_real(token), "+i", sep='')
            return True
        print("Z=i")
        return True
    return False

def print_check_imaginary_neg_i ( complex, i ): # example case: z=2-i or z=-i
    token = complex[i]
    if get_imaginary(token) == -1:
        if get_real(token) != 0:
            print("Z=", get_real(token),"-i",sep='')
            return True

        print("Z=-i")
        return True
    return False

def print_check_positive_imaginary ( complex, i ): # example case: z=3+2i or z=5i
    token = complex[i]
    if get_imaginary(token) > 0:
        if get_real(token) != 0:
            print("Z=", get_real(token), "+", get_imaginary(token), "i", sep='')  # no spaces
            return True

        print("Z=", get_imaginary(token), "i", sep='')  # no spaces, no real number
        return True
    return False

def print_check_negative_imaginary ( complex, i ): # example case: z=4-5i or z=-2i
    token = complex[i]
    if get_imaginary(token) < 0:
        if get_real(token) != 0:
            print("Z=", get_real(token), get_imaginary(token), "i", sep='')  # no spaces
            return True
        print("Z=", get_imaginary(token), "i", sep='')  # no spaces, no real number
        return True
    return False

def print_check_real_number (complex, i): # example case: z=24 or z=0
    token = complex[i]
    if get_imaginary(token) == 0:
        print("Z=", get_real(token), sep='')  # no spaces
        return True
    return False

def print_all_numbers (complex):
    print_numbers(complex, 0, len(complex))


def print_menu_options():
    print(" 1 - Add a number \n"
          " 2 - Display the entire list of numbers \n"
          " 3 - Display the longest sequence that: the difference between the modulus of consecutive numbers is a prime number. \n"
          " 4 - Display the longest sequence that: the modulus of all elements is in the [0, 10] range.\n"
          " x - Exit")


def print_numbers( complex, start, final):
    if start >= final:
        print("There aren't any elements with the given property.")
    for i in range(start, final):
            if print_check_imaginary_i(complex, i) == True:
                continue

            if print_check_imaginary_neg_i(complex, i) == True:
                continue

            if print_check_positive_imaginary(complex, i) == True:
                continue

            if print_check_negative_imaginary(complex, i) == True:
                continue

            if print_check_real_number(complex, i) == True:
                continue



def check_real_number (complex, number): # example case: z=32 or z=235
    if number.find("i") == -1:
        imaginary = 0
        real = int(number)
        add_complex_number(complex,real,imaginary)
        return True
    return False


def check_imaginary_number_one (complex, number): # example case: z=3+i or z=123+i
    if number.find("+") != -1:
        if number[len(number)-1] == "+":
            imaginary = 1
            var = number.split("+")
            real = int(var[0])
            add_complex_number(complex, real, imaginary)
            return True
    return False


def check_imaginary_negative_number (complex, number):
    if number.find("-") != -1:
        if number[len(number)-1] == "-":
            if len(number) == 1: # checks for case -i and Re(Z) = 0
                imaginary = -1
                real = 0
                add_complex_number(complex, real, imaginary)
            elif len(number) == 2:
                imaginary = -1
                var = number.split("-")
                real = int(var[0])
                add_complex_number(complex, real, imaginary)
            elif len(number) == 3: # checks if both are negative and the second one is -i
                imaginary = -1
                var = number.split("-")
                real = -int(var[1])
                add_complex_number(complex, real, imaginary)
            return True
    return False


def check_imaginary_number (complex, number):
    if number.find("+") == -1 and number.find("-") == -1: # no +/- in the number, example: z=17i or z=i
        real = 0
        if number != "": #checks for case i
            imaginary = int(number)
        else:
            imaginary = 1
        add_complex_number(complex, real, imaginary)
        return True
    return False


def check_both_negative (complex, new_number): # example: z=-2-35i
    if len(new_number) == 3:
        real = -int(new_number[1]) # negative
        imaginary = -int(new_number[2]) # negative
        add_complex_number(complex, real, imaginary)
        return True
    return False


def imaginary_negative (complex, new_number): # example: z=3-2i
    if new_number[0] != "":
        real = int(new_number[0])  # this one is positive
    else:
        real = 0
    imaginary = -int(new_number[1])  # this one is negative
    add_complex_number(complex, real, imaginary)


def both_positives(complex, number): # example: z=4+512i
    new_number = number.split("+")
    real = int(new_number[0])
    imaginary = int(new_number[1])
    add_complex_number(complex, real, imaginary)


def ui_add_number (complex):
    number = input("Z=")

    if check_real_number(complex, number) == True:
        return

    number = number.replace("i","") # no more i, we dont need letters in a number !

    if check_imaginary_number_one(complex, number) == True:
        return

    if check_imaginary_negative_number(complex, number) == True:
        return

    if check_imaginary_number(complex, number) == True:
        return
        
    if number.find("+") == -1: 
        new_number = number.split("-")
        if check_both_negative(complex, new_number) == True:
            return

        imaginary_negative(complex,new_number)
        return

    both_positives(complex, number)
    return

############################################################## FUNCTION SECTION ######################################

# Function section
# (write all non-UI functions in this section)
# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values

# print('Hello A2'!) -> prints aren't allowed here!

def is_prime (number):
    if number == 2:
        return True
    if number < 2:
        return False
    if number % 2 == 0:
        return False
    for i in range (3, number // 2 + 1, 2):
        if number % i == 0:
            return False
    return True


def get_modulus(complex, i): #get_modulus
    modulus_number = int((get_real(complex[i]) ** 2 + get_imaginary(complex[i]) ** 2) ** 0.5)
    return modulus_number


def difference_between_2_consecutive_modulus_prime (complex):
    """
    It goes through every element from dictionary and computes its modulus and check if the difference between 2 consecutive numbers' modulus is prime.
    If it is prime, it compares with a maximum and after that it memorise the length of the sequence and the final index from dictionary. In the end, it prints
    the sequence.
    :param: complex - dictionary
    :return: none
    """
    modulus_first_number = get_modulus(complex, 0)
    sequence = 1
    max_sequence = 0
    final_index = 0
    for i in range(1, len(complex)):
        modulus_second_number = get_modulus(complex, i)
        if is_prime(modulus_second_number - modulus_first_number) == True or is_prime(modulus_first_number - modulus_second_number ) == True:
                sequence += 1
                if sequence > max_sequence:
                    max_sequence = sequence
                    final_index = i
        else:
            sequence = 1
        modulus_first_number = modulus_second_number

    print_numbers(complex, final_index-max_sequence+1, final_index+1)



def modulus_in_range_1_10(complex):
    """
    It goes through every element from dictionary, it computes its modulus and if it's in the [0,10] range, the sequence increments
    and it is compared with a maximum sequence and if it's higher, it memorises its length and final index from dictionary. Also it prints
    the sequence.
    :param: complex - dictionary
    :return: none
    """
    sequence = 0
    max_sequence = 0
    final_index = 0
    for i in range( len(complex)):
        modulus_number = get_modulus(complex, i)
        if modulus_number >= 0 and modulus_number <= 10:
                sequence += 1
                if sequence > max_sequence:
                    max_sequence = sequence
                    final_index = i
        else:
            sequence = 0

    print_numbers(complex, final_index-max_sequence+1, final_index+1)


def add_complex_number (complex, real, imaginary):
    number = create_complex(real,imaginary)
    complex.append(number)



if __name__ == '__main__':
    run_menu()