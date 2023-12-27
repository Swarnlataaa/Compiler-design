class CodeGenerator:
    def __init__(self, intermediate_code):
        self.intermediate_code = intermediate_code
        self.machine_code = []

    def generate_code(self):
        for line in self.intermediate_code:
            tokens = line.split()
            if len(tokens) == 3:
                # Directly copy lines without operations (e.g., result = T3)
                self.machine_code.append(line)
            elif len(tokens) == 5:
                # Translate intermediate code to machine code (e.g., T3 = T0 + T2)
                operand1, operator, operand2, equals, result = tokens
                machine_instruction = self.translate_instruction(operator)
                self.machine_code.append(f'{machine_instruction} {result}, {operand1}, {operand2}')

    def translate_instruction(self, operator):
        # Simple translation for illustration purposes
        translation_map = {
            '+': 'ADD',
            '-': 'SUB',
            '*': 'MUL',
            '/': 'DIV'
        }
        return translation_map.get(operator, operator)

    def display_machine_code(self):
        print("Machine Code:")
        print("-------------------")
        for line in self.machine_code:
            print(line)
        print("-------------------")


# Example usage:

# Sample intermediate code
intermediate_code = [
    'T0 = 3 + 5',
    'T1 = 7 - 2',
    'T2 = 5 * T1',
    'T3 = T0 + T2',
    'result = T3'
]

# Create a code generator
code_generator = CodeGenerator(intermediate_code)

# Display original intermediate code
print("Original Intermediate Code:")
print("-------------------")
for line in intermediate_code:
    print(line)
print("-------------------")

# Generate machine code
code_generator.generate_code()

# Display generated machine code
code_generator.display_machine_code()
