def generate_transition(init_state, final_state, start, end):
    transition_string = ""
    for char_ascii in range(ord(start), ord(end)+1):
        transition_string += init_state
        transition_string += ' '
        transition_string += chr(char_ascii)
        transition_string += ' '
        transition_string += final_state
        transition_string += '\n'
    return transition_string
