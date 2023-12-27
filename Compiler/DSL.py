class DSLCompiler:
    def __init__(self):
        self.lexer = DSLLexer()
        self.parser = DSLParser()
        self.semantic_analyzer = DSLSemanticAnalyzer()

    def compile_and_execute(self, source_code):
        try:
            # Lexical analysis
            tokens = self.lexer.tokenize(source_code)

            # Syntax analysis
            abstract_syntax_tree = self.parser.parse(tokens)

            # Semantic analysis
            validated_ast = self.semantic_analyzer.analyze(abstract_syntax_tree)

            # Generate and execute code dynamically
            generated_code = self.generate_code(validated_ast)
            result = self.execute_code(generated_code)

            return result

        except DSLCompilationError as e:
            print(f"DSL Compilation Error: {str(e)}")
            return None

    def generate_code(self, ast):
        # Simplified code generation for demonstration
        if ast[0] == 'add':
            return ast[1][1] + ast[2][1]
        elif ast[0] == 'subtract':
            return ast[1][1] - ast[2][1]
        elif ast[0] == 'multiply':
            return ast[1][1] * ast[2][1]
        elif ast[0] == 'divide':
            if ast[2][1] == 0:
                raise DSLCompilationError("Division by zero is not allowed.")
            return ast[1][1] / ast[2][1]
        else:
            raise DSLCompilationError("Unsupported operation in DSL")

    def execute_code(self, generated_code):
        return generated_code


class DSLCompilationError(Exception):
    pass


class DSLLexer:
    def tokenize(self, source_code):
        # Simplified tokenization for demonstration
        return source_code.split()


class DSLParser:
    def parse(self, tokens):
        # Simplified parsing for demonstration
        if len(tokens) < 3 or tokens[1] not in {'+', '-', '*', '/'}:
            raise DSLCompilationError("Syntax Error: Invalid DSL expression.")
        operation = {
            '+': 'add',
            '-': 'subtract',
            '*': 'multiply',
            '/': 'divide',
        }[tokens[1]]
        return (operation, ('number', int(tokens[0])), ('number', int(tokens[2])))


class DSLSemanticAnalyzer:
    def analyze(self, ast):
        # Simulated semantic analysis - just an example
        if not ast or ast[0] not in {'add', 'subtract', 'multiply', 'divide'}:
            raise DSLCompilationError("Semantic Error: Invalid DSL operation.")
        return ast


# Example usage:

dsl_source_code = "3 + 5"

dsl_compiler = DSLCompiler()
dsl_result = dsl_compiler.compile_and_execute(dsl_source_code)

if dsl_result is not None:
    print(f"Result of DSL compilation and execution: {dsl_result}")
