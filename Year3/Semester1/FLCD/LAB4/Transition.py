class Transition:
    def __init__(self, initial_states, values, final_states):
        self.initial_states = initial_states
        self.values = values
        self.final_states = final_states

    def __str__(self):
        return str(self.initial_states) + ' ' + str(self.values) + ' ' + str(self.final_states)
