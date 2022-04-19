from domain.Discipline import Discipline

from domain.Validators import DisciplineIdError, DisciplineValidator


class DisciplinesService:
    def __init__(self, discipline_repository, grade_repository):
        self.__repository = discipline_repository
        self.__grade_repository = grade_repository

    def add_a_discipline(self, discipline_id, name):
        """
        It adds a discipline to the discipline repository.
        :param discipline_id: string
        :param name: string
        :return: none
        """
        if discipline_id.isdigit() == False:
            raise DisciplineIdError("Discipline id has to be a positive integer.")
        DisciplineValidator.validate(discipline_id, name)
        self.__repository.add_a_discipline(Discipline(int(discipline_id), name))

    def search_a_discipline_by_discipline_ID(self, discipline_id):
        """
        It searches a discipline by id in the discipline repository.
        :param discipline_id: string
        :return: list
        """
        if discipline_id.isdigit() == False:
            raise DisciplineIdError("Discipline id must be a positive integer.")
        return self.__repository.search_a_discipline_by_discipline_ID(discipline_id)

    def search_a_discipline_by_name(self, discipline_name):
        """
        It searches a discipline by name in the discipline repository.
        :param discipline_name: string
        :return: none
        """
        the_list_of_disciplines_that_match_the_given_name = []
        for discipline in self.__repository.list_of_disciplines():
            if discipline.name.lower().find(discipline_name.lower()) != -1:
                the_list_of_disciplines_that_match_the_given_name.append(discipline)
        return the_list_of_disciplines_that_match_the_given_name


    def update_a_discipline_by_id(self, discipline_id, new_discipline_name):
        """
        It updates a discipline by id in the discipline repository.
        :param discipline_that_is_going_to_be_updated: string
        :param new_discipline_id: string
        :return: none
        """
        self.__repository.update_a_discipline_by_id(discipline_id, new_discipline_name)

    def update_a_discipline_by_name(self, discipline_name, new_discipline_id):
        """
        It updates a discipline by name in the discipline repository.
        :param new_discipline_name: string
        :param discipline_id_that_is_going_to_be_updated: string
        :return: none
        """
        self.__repository.update_a_discipline_by_name(discipline_name, int(new_discipline_id))

    def remove_a_discipline(self, discipline_id):
        """
        It removes a discipline from discipline repository using discipline id. Also it removes all the grades for that discipline.
        :param discipline_id: string
        :return: none
        """
        self.__grade_repository.remove_grades_for_a_discipline(int(discipline_id))
        self.__repository.remove_a_discipline(int(discipline_id))


    def list_of_disciplines(self):
        """
        It return the list of all disciplines from the disciplines repository.
        :return: self.__repository.list_of_disciplines()
        """
        return self.__repository.list_of_disciplines()

    def get_index_of_disciplines_list(self, index):
        """
        It return the index-th element from the disciplines list.
        :param index: integer
        :return: self.__repository.get_index_of_disciplines_list(index)
        """
        return self.__repository.get_index_of_disciplines_list(index)

    def length_of_disciplines(self):
        """
        It return the length of disciplines list from the disciplines repository.
        :return: self.__repository.length_of_disciplines()
        """
        return self.__repository.length_of_disciplines()
