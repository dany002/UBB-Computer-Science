from repository.RepositoryException import RepositoryException, RepositoryException2
from Utils.CustomIterable import CustomIterable

class DisciplineRepository:
    def __init__(self):
        self._disciplines = CustomIterable()


    def add_a_discipline(self, discipline_that_is_going_to_be_added):
        """
        It adds a discipline in the list
        :param discipline_that_is_going_to_be_added: Discipline
        :return: none
        """

        for index in range(len(self._disciplines)):
            if self._disciplines[index].discipline_id == discipline_that_is_going_to_be_added.discipline_id:
                raise RepositoryException("Discipline ID is already taken.")
        self._disciplines.append(discipline_that_is_going_to_be_added)

    def remove_a_discipline(self, discipline_id):
        """
        It removes a discipline from the list. Also it checks if the discipline id is in the list.
        :param discipline_id: integer
        :return: none
        """
        found_id = False
        for index in range(len(self._disciplines)):
            if self._disciplines[index].discipline_id == discipline_id:
                found_id = True
        if found_id == False:
            raise RepositoryException("Discipline ID is not found.")


        index = 0
        length = len(self._disciplines)
        while index < length:
            if int(self._disciplines[index].discipline_id) == int(discipline_id):
                del self._disciplines[index]
                index -= 1
                length -= 1
            index += 1

    def search_a_discipline_by_discipline_ID(self, discipline_id):
        """
        It searches a discipline by discipline ID and it creates a new list result_list_with_searched_discipline: [{'id': id, 'name': name}, {'id': id, 'name': name2}, ...]
        :param discipline_id: integer
        :return: result_list_with_searched_discipline
        """
        result_list_with_searched_discipline = []
        for index in range(len(self._disciplines)):
            if int(self._disciplines[index].discipline_id) == int(discipline_id):
                discipline = self._disciplines[index]
                result_list_with_searched_discipline.append(discipline)

        if result_list_with_searched_discipline == []:
            raise RepositoryException("Discipline id is not found.")
        return result_list_with_searched_discipline

    def search_a_discipline_by_name(self, discipline_name):
        """
        It searches a discipline by discipline name and it creates a new list result_list_with_searched_discipline: [{'id': id, 'name': name}, {'id': id, 'name': name2}, ...]
        :param discipline_name: string
        :return: result_list_with_searched_discipline
        """
        if discipline_name.isalpha() == False:
            raise RepositoryException2("Discipline name has to contain only letters.")
        result_list_with_searched_discipline = []
        for index in range(len(self._disciplines)):
            if self._disciplines[index].name == discipline_name:
                discipline = {'id': self._disciplines[index].discipline_id, 'name': self._disciplines[index].name}
                result_list_with_searched_discipline.append(discipline)
        if result_list_with_searched_discipline == []:
            raise RepositoryException("Discipline name is not found.")
        return result_list_with_searched_discipline

    def update_a_discipline_by_name(self, discipline_name, new_discipline_id):
        """
        It updates a discipline by name and it assign the new_discipline_id to the discipline name that was given.
        Also it checks if the new_discipline_id is taken or not and if there is a name.
        :param discipline_name: string
        :param new_discipline_id: integer
        :return:
        """
        for index in range(len(self._disciplines)):
            if self._disciplines[index].discipline_id == int(new_discipline_id):
                raise RepositoryException("Discipline ID is already taken.")
        name_found = False

        for index in range(len(self._disciplines)):
            if self._disciplines[index].name == discipline_name:
                self._disciplines[index].discipline_id = new_discipline_id
                name_found = True
        if name_found == False:
            raise RepositoryException2("There is no name to be updated.")

    def update_a_discipline_by_id(self, discipline_id, new_discipline_name):
        """
        It updates a discipline by id and it assign the new_discipline_name to the discipline id that was given
        :param discipline_id_that_is_going_to_be_updated: string
        :param new_discipline_name: string
        :return: none
        """
        id_found = False
        for index in range(len(self._disciplines)):
            if int(self._disciplines[index].discipline_id) == int(discipline_id):
                self._disciplines[index].name = new_discipline_name
                id_found = True
        if id_found == False:
            raise RepositoryException("There is no id to be updated.")

    def list_of_disciplines(self):
        """
        It return the list of disciplines.
        :return: self.__disciplines
        """
        return [discipline for discipline in self._disciplines]

    def length_of_disciplines(self):
        """
        It return the length of list of disciplines.
        :return: len(self.__disciplines)
        """
        return len(self._disciplines)

    def get_index_of_disciplines_list(self, index):
        """
        It return the index-th element from the disciplines list.
        :param index: integer
        :return: self.__disciplines[index]
        """
        return self._disciplines[index]