

class Discipline:
    def __init__(self, discipline_id, name):
        self.__discipline_id = discipline_id
        self.__name = name


    @property
    def discipline_id(self):
        return self.__discipline_id

    @discipline_id.setter
    def discipline_id(self, discipline_id):
        self.__discipline_id = discipline_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __eq__(self, other_discipline):
        if self.discipline_id == other_discipline.discipline_id:
            if self.name == other_discipline.name:
                return True
        return False

    def __str__(self):
        return f'Discipline id: ' + str(self.discipline_id) + '  Discipline name: ' + self.name