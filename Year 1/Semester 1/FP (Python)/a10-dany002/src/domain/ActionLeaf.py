

class ActionLeaf:
    def __init__(self, action_function, arguments):
        self.action_function = action_function
        self.arguments = arguments

    def do_action(self):
        self.action_function(*self.arguments)
