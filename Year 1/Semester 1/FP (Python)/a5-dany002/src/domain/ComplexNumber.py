class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.__real_part = real_part
        self.__imaginary_part = imaginary_part
        
    @property
    def real_part(self):
        return self.__real_part

    @real_part.setter
    def real_part(self, real_part):
        self.__real_part = real_part

    @property
    def imaginary_part(self):
        return self.__imaginary_part

    @imaginary_part.setter
    def imaginary_part(self, imaginary_part):
        self.__imaginary_part = imaginary_part

    def __eq__(self, other):
        if self.real_part == other.real_part:
            if self.imaginary_part == other.imaginary_part:
                return True
        return False