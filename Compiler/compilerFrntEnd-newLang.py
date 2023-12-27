import re

class SimpleLangLexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.current_token = None
        self.token_index = 0
        self.keywords = {'let', 'print'}

    def tokenize(self):
        self.source_code = self.source_code.replace('\n', ' ')
        self.tokens = re.findall(r'\b\w+\b|[^\w\s]', self.source_code)
        self.tokens = [token.strip() for token in self.tokens if token.strip()]

    def get_next_token(self):
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
            self.token_index += 1
            return self.current_token
        return None


class SimpleLangParser:
    def __init__(self, lexer):
        self.lexer = lexer

    def parse(self):
        self.lexer.tokenize()
        self.lexer.get_next_token()  # Initialize current_token
        self.program()

    def program(self):
        while self.lexer.current_token:
            if self.lexer.current_token == 'let':
                self.variable_declaration()
            elif self.lexer.current_token == 'print':
                self.print_statement()
            else:
                self.expression()

    def variable_declaration(self):
        self.lexer.get_next_token()  # Consume 'let'
        variable_name = self.lexer.get_next_token()
        if variable_name.isalpha():
            self.lexer.get_next_token()  # Consume '='
            self.expression()
        else:
            raise SyntaxError("Invalid variable name in variable declaration")

    def print_statement(self):
        self.lexer.get_next_token()  # Consume 'print'
        self.expression()

    def expression(self):
        # For simplicity, consider only binary addition
        left_operand = self.lexer.get_next_token()
        operator = self.lexer.get_next_token()
        right_operand = self.lexer.get_next_token()

        if left_operand.isnumeric() and operator == '+' and right_operand.isnumeric():
            pass  # Expression is valid
        else:
            raise SyntaxError("Invalid expression")


# Example usage:

source_code = """
let x = 10
print x + 5
"""

lexer = SimpleLangLexer(source_code)
parser = SimpleLangParser(lexer)

try:
    parser.parse()
    print("Parsing successful!")
except SyntaxError as e:
    print(f"Syntax Error: {e}")
