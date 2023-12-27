class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def analyze(self, ast):
        if ast:
            if ast[0] == 'number':
                return 'int'  # Assuming numbers are integers in this example
            elif ast[0] in {'add', 'subtract', 'multiply', 'divide'}:
                left_type = self.analyze(ast[1])
                right_type = self.analyze(ast[2])

                # Check if operands have compatible types
                if left_type != 'int' or right_type != 'int':
                    print("Semantic Error: Operands must be of type 'int' for arithmetic operations.")
                return 'int'
            else:
                print(f"Semantic Error: Unexpected AST node: {ast[0]}")
        return None

# Example usage:

# Sample AST for the expression: 3 + 5 * (7 - 2)
ast_example = ('add', ('number', 3), ('multiply', ('number', 5), ('subtract', ('number', 7), ('number', 2))))

# Create a semantic analyzer
semantic_analyzer = SemanticAnalyzer()

# Analyze the AST
result_type = semantic_analyzer.analyze(ast_example)

# Print the result type
if result_type:
    print(f"The result type of the expression is: {result_type}")
