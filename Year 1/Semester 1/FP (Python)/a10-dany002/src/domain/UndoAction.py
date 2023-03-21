

class UndoAction:
    def __init__(self, undo_action, redo_action):
        self.__undo_action = undo_action
        self.__redo_action = redo_action

    def undo(self):
        self.__undo_action.do_action()

    def redo(self):
        self.__redo_action.do_action()