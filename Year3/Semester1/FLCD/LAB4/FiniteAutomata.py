from Transition import Transition


class FiniteAutomata:

    def __init__(self, Q, E, S, q0, F):
        self.Q = Q    # set of states
        self.E = E    # alphabet
        self.S = S    # set of transitions
        self.q0 = q0  # initial state
        self.F = F    # final state

    def read_automata(self, fileName):
        with open(fileName) as file:

            # Set the initial state
            first_line = file.readline()
            tokens = first_line.replace('\n', '').split(" ")
            self.q0 = tokens

            # Set the final state
            second_line = file.readline()
            tokens = second_line.replace('\n', '').split(" ")
            self.F = tokens

            # Transitions
            for line in file:
                tokens = line.replace('\n', '').split(" ")
                self.S.append(Transition(tokens[0], tokens[1], tokens[2]))
                if tokens[0] not in self.Q:
                    self.Q.append(tokens[0])
                if tokens[2] not in self.Q:
                    self.Q.append(tokens[2])
                if tokens[1] not in self.E:
                    self.E.append(tokens[1])

    @staticmethod
    def check_sequence(item, fa, initial_states):
        result = False
        following_states = list()
        if len(initial_states) == 0:
            return False
        for state in initial_states:
            if state in fa.F:
                return True
            if len(state) == 0:
                return False
            value = item[0:1]
            for transition in fa.S:
                if transition.values == value and transition.initial_states == state:
                    following_states.append(transition.final_states)
        if len(item) == 1:
            new_item = ""
        else:
            new_item = item[1:]
        result = result or FiniteAutomata.check_sequence(new_item, fa, following_states)
        return result
        # return False
