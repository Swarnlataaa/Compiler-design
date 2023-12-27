class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def insert(self, name, symbol_type, value=None):
        if name in self.symbols:
            print(f"Error: Identifier '{name}' already declared.")
            return False
        self.symbols[name] = {'type': symbol_type, 'value': value}
        return True

    def lookup(self, name):
        if name in self.symbols:
            return self.symbols[name]
        else:
            print(f"Error: Identifier '{name}' not found in the symbol table.")
            return None

    def update(self, name, value):
        if name in self.symbols:
            self.symbols[name]['value'] = value
        else:
            print(f"Error: Identifier '{name}' not found in the symbol table.")

    def display(self):
        print("Symbol Table:")
        print("--------------")
        for name, attributes in self.symbols.items():
            print(f"Name: {name}, Type: {attributes['type']}, Value: {attributes['value']}")
        print("--------------")


# Example usage:

# Create a symbol table
symbol_table = SymbolTable()

# Insert identifiers
symbol_table.insert('x', 'int', 10)
symbol_table.insert('y', 'float', 3.14)
symbol_table.insert('x', 'int')  # Error: Identifier 'x' already declared.

# Display the symbol table
symbol_table.display()

# Lookup identifiers
result = symbol_table.lookup('x')
if result:
    print(f"Lookup Result for 'x': {result}")

result = symbol_table.lookup('z')  # Error: Identifier 'z' not found in the symbol table.

# Update identifier value
symbol_table.update('y', 2.71)

# Display the updated symbol table
symbol_table.display()
