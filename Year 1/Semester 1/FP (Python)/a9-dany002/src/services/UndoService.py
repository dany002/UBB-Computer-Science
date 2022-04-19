from services.UndoExceptions import UndoServiceException

class UndoService:
    def __init__(self, undo_repository):
        self.__undo_repository = undo_repository
        self.__index = -1

    def add(self, action):
        while len(self.__undo_repository) > self.__index + 1:
            self.__undo_repository.pop()
        self.__undo_repository.add(action)
        self.__index += 1


    def undo(self):
        if self.__index == -1:
            raise UndoServiceException("You can't undo anymore.")
        self.__undo_repository.get_by_index(self.__index).undo()
        self.__index -= 1

    def redo(self):
        self.__index += 1
        if self.__index >= len(self.__undo_repository):
            raise UndoServiceException("You can't redo anymore.")
        self.__undo_repository.get_by_index(self.__index).redo()

    def get_all(self):
        return self.__undo_repository
