

class ActionComposite:
    def __init__(self):
        self.__children = []

    def add_child(self, child):
        self.__children.append(child)

    def do_action(self):
        for child in self.__children:
            child.do_action()


