from repository.RepositoryException import RepositoryException

class UndoRepository:
    def __init__(self):
        self.__list_of_commands_for_undo = []


    def add(self, action):
        self.__list_of_commands_for_undo.append(action)


    def remove_last_action(self):
        if len(self.__list_of_commands_for_undo) == 0:
            raise RepositoryException("List is empty.")
        self.__list_of_commands_for_undo.pop()

    def get_by_index(self, index):
        return self.__list_of_commands_for_undo[index]

    def get_all(self):
        return self.__list_of_commands_for_undo

    def __len__(self):
        return len(self.__list_of_commands_for_undo)

    def __eq__(self, other):
        if self.__list_of_commands_for_undo == other:
            return True
        return False

    def __str__(self):
        return str(self.__list_of_commands_for_undo)