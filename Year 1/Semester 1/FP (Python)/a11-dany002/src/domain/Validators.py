class Error(Exception):
    pass

class PlaneDoesntFit(Error):
    pass

class ThereIsAlreadyAPlaneThere(Error):
    pass

class NotNumber(Error):
    pass

class NotInTheRangeAJ(Error):
    pass

class NotInTheRange(Error):
    pass

class IsNumber(Error):
    pass

class CheckIfTheFirstCoordinateIsRight(Error):
    @staticmethod
    def validate(coordinate):
        if coordinate.isnumeric() == False:
             raise NotNumber
        if int(coordinate) < 1 or int(coordinate) > 10:
            raise NotInTheRange

class CheckIfTheSecondCoordinateIsRight(Error):
    @staticmethod
    def validate(coordinate):
        if coordinate.isnumeric() == True:
            raise IsNumber
        if coordinate < 'A' or coordinate > 'J':
            raise NotInTheRangeAJ