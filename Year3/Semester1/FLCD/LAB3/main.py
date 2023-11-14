import re
import os

class Scanner:
    def __init__(self):
        self.program = ""
        self.tokens = []
        self.reserved_words = []
        self.symbol_table = {}
        self.PIF = []
        self.index = 0
        self.current_line = 1
        self.ok = 0
        self.errors = []

    def read_tokens(self):
        with open("token.in", "r") as token_file:
            for line in token_file:
                token = line.strip().split()[0]
                if token in ["OF", "read", "write", "if", "else", "while", "for", "true", "false", "auto", "ret", "BEGIN", "END"]:
                    self.reserved_words.append(token)
                else:
                    self.tokens.append(token)

    def skip_spaces(self):
        while self.index < len(self.program) and self.program[self.index].isspace():
            if self.program[self.index] == '\n':
                self.current_line += 1
            self.index += 1

    def skip_comments(self):
        while self.index < len(self.program) and self.program[self.index] == '#':
            while self.index < len(self.program) and self.program[self.index] != '\n':
                self.index += 1

    def treat_string_constant(self):
        regex_for_string_constant = re.compile(r'^"[a-zA-Z0-9_ ?:*^+=.!]*"')
        match = regex_for_string_constant.search(self.program[self.index:])
        if not match:
            if re.search(r'^"[^\"]"', self.program[self.index:]):  # checks if it doesn't have illegal characters
                raise ScannerException("Invalid string constant at line " + str(self.current_line))
            if re.search(r'^"[^\"]', self.program[self.index:]):  # checks if the " are closed
                raise ScannerException("Missing \" at line " + str(self.current_line))
            return False

        string_constant = match.group(0)
        self.index += len(string_constant)

        if string_constant not in self.symbol_table:
            # Assign a unique position/index for each string constant
            position = len(self.symbol_table) + 1
            self.symbol_table[string_constant] = position
        else:
            position = self.symbol_table[string_constant]

        position = (self.current_line, position)  # Use the Symbol Table position
        self.PIF.append(("str const", position))  # add it as str const in PIF
        return True

    def treat_int_constant(self):
        regex_for_int_constant = re.compile(r'^([+-]?[1-9][0-9]*|0)')  # checks if there are only numbers, only +- are optional
        match = regex_for_int_constant.search(self.program[self.index:])
        if not match:
            return False
        int_constant = match.group(1)
        self.index += len(int_constant)

        if int_constant not in self.symbol_table:
            # Assign a unique position/index for each integer constant
            position = len(self.symbol_table) + 1
            self.symbol_table[int_constant] = position
        else:
            position = self.symbol_table[int_constant]

        position = (self.current_line, position)  # Use the Symbol Table position
        self.PIF.append(("int const", position))  # add it as int const in PIF
        return True

    def check_if_valid(self, possible_identifier):
        if possible_identifier in self.reserved_words:
            return False
        if re.search(r'\b(int|string|char|bool)\b', possible_identifier):
            self.ok = 1
            return False
        if self.ok == 1 and re.search(r'^[A-Za-z][A-Za-z0-9_]*', possible_identifier): # it s the variable after the declaration
            self.ok = 0
            return True
        return possible_identifier in self.symbol_table

    def treat_identifier(self):
        regex_for_identifier = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*')
        match = regex_for_identifier.search(self.program[self.index:])
        if not match:
            return False
        identifier = match.group(0)
        if not self.check_if_valid(identifier):
            return False

        if identifier not in self.symbol_table:
            # Add the identifier to the Symbol Table with a unique index
            self.symbol_table[identifier] = len(self.symbol_table) + 1

        # Get the position from the Symbol Table
        symbol_table_position = self.symbol_table[identifier]

        self.index += len(identifier)
        position = (self.current_line, symbol_table_position)  # Use the Symbol Table position
        self.PIF.append(("identifier", position))

        return True

    def treat_from_token_list(self):
        possible_token = self.program[self.index:].split(" ")[0]
        for reserved_token in self.reserved_words:
            if possible_token.startswith(reserved_token):
                regex = f"^[a-zA-Z0-9_]*{reserved_token}[a-zA-Z0-9_]+" # for example it checks for atBEGINsfd -> is not a reserved word
                if re.search(regex, possible_token):
                    return False
                self.index += len(reserved_token)
                self.PIF.append((reserved_token, (-1, -1)))
                return True
        for token in self.tokens:
            if possible_token == token or possible_token.startswith(token):
                self.index += len(token)
                self.PIF.append((token, (-1, -1)))
                return True
        return False

    def next_token(self):
        self.skip_spaces()
        self.skip_comments()
        if self.index == len(self.program):
            return
        if self.treat_identifier():
            return
        if self.treat_string_constant():
            return
        if self.treat_int_constant():
            return
        if self.treat_from_token_list():
            return

        raise ScannerException("Lexical error: invalid token at line " + str(self.current_line) + ", index " + str(self.index))

    def scan(self, program_filename):
        try:
            with open(program_filename, "r") as program_file:
                self.program = program_file.read()
                self.index = 0
                self.PIF = []
                self.symbol_table = {}
                self.current_line = 1
                while self.index < len(self.program):
                    self.next_token()

            with open("PIF" + os.path.splitext(program_filename)[0] + ".out", "w") as pif_file:
                for token, position in self.PIF:
                    pif_file.write(f"{token} -> ({position[0]}, {position[1]})\n")

            with open("ST" + os.path.splitext(program_filename)[0] + ".out", "w") as st_file:
                for symbol, index in self.symbol_table.items():
                    st_file.write(f"{symbol} -> {index}\n")
        except ScannerException as e:
            print(e)

class ScannerException(Exception):
    pass

if __name__ == '__main__':
    scanner = Scanner()
    scanner.read_tokens()
    program_filename = "p1"  # options: p1, p2, p3 and p1err
    scanner.scan(program_filename)
