class CodeOptimizer:
    def __init__(self, intermediate_code):
        self.optimized_code = intermediate_code

    def constant_folding(self):
        for i in range(len(self.optimized_code)):
            line = self.optimized_code[i].split()
            if len(line) == 5:
                operand1, operator, operand2, equals, result = line
                try:
                    value = eval(f'{operand1} {operator} {operand2}')
                    self.optimized_code[i] = f'{result} = {value}'
                except:
                    pass  # Ignore if the expression cannot be evaluated

    def dead_code_elimination(self):
        live_vars = set()
        for line in self.optimized_code:
            tokens = line.split()
            if len(tokens) >= 3:
                live_vars.add(tokens[0])
                live_vars.discard(tokens[-1])

        self.optimized_code = [line for line in self.optimized_code if line.split()[0] in live_vars]

    def display_optimized_code(self):
        print("Optimized Code:")
        print("-------------------")
        for line in self.optimized_code:
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

# Create a code optimizer
code_optimizer = CodeOptimizer(intermediate_code)

# Display original code
print("Original Code:")
print("-------------------")
for line in intermediate_code:
    print(line)
print("-------------------")

# Apply constant folding
code_optimizer.constant_folding()

# Apply dead code elimination
code_optimizer.dead_code_elimination()

# Display optimized code
code_optimizer.display_optimized_code()
