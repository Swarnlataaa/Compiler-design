class IntermediateCodeGenerator:
    def __init__(self):
        self.code = []
        self.temp_count = 0

    def generate_temp(self):
        temp_var = f'T{self.temp_count}'
        self.temp_count += 1
        return temp_var

    def generate_code(self, ast):
        if ast:
            if ast[0] == 'number':
                return ast[1], 'int'
            elif ast[0] in {'add', 'subtract', 'multiply', 'divide'}:
                left_operand, left_type = self.generate_code(ast[1])
                right_operand, right_type = self.generate_code(ast[2])

                result_type = 'int'  # Assuming numbers are integers

                if left_type != 'int' or right_type != 'int':
                    print("Semantic Error: Operands must be of type 'int' for arithmetic operations.")

                temp_var = self.generate_temp()
                self.code.append(f'{temp_var} = {left_operand} {ast[0]} {right_operand}')
                return temp_var, result_type
            else:
                print(f"Intermediate Code Generation Error: Unexpected AST node: {ast[0]}")
        return None

    def display_code(self):
        print("Intermediate Code:")
        print("-------------------")
        for line in self.code:
            print(line)
        print("-------------------")


# Example usage:

# Sample AST for the expression: 3 + 5 * (7 - 2)
ast_example = ('add', ('number', 3), ('multiply', ('number', 5), ('subtract', ('number', 7), ('number', 2))))

# Create an intermediate code generator
intermediate_code_generator = IntermediateCodeGenerator()

# Generate intermediate code from AST
result, result_type = intermediate_code_generator.generate_code(ast_example)

# Display the intermediate code
intermediate_code_generator.display_code()
