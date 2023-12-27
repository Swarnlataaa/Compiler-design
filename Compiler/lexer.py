import ply.lex as lex
import ply.yacc as yacc

# Define the tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Define the token regex patterns
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Define a token for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define ignored characters (whitespace)
t_ignore = ' \t\n'

# Error handling for invalid characters
def t_error(t):
    print(f"Invalid character: {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Define the grammar rules
def p_expression(p):
    '''
    expression : expression PLUS term
               | expression MINUS term
               | term
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '+':
            p[0] = ('add', p[1], p[3])
        elif p[2] == '-':
            p[0] = ('subtract', p[1], p[3])

def p_term(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
         | factor
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '*':
            p[0] = ('multiply', p[1], p[3])
        elif p[2] == '/':
            p[0] = ('divide', p[1], p[3])

def p_factor(p):
    '''
    factor : NUMBER
           | LPAREN expression RPAREN
    '''
    if len(p) == 2:
        p[0] = ('number', p[1])
    else:
        p[0] = p[2]

# Error handling for syntax errors
def p_error(p):
    print(f"Syntax error at token {p.value}")

# Build the parser
parser = yacc.yacc()

# Example input
input_expr = "3 + 5 * ( 7 - 2 )"

# Run the lexer and parser
lexer.input(input_expr)
result = parser.parse(input_expr)

# Print the Abstract Syntax Tree (AST)
print("Abstract Syntax Tree:", result)
