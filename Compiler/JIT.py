class JITCompiler:
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()
        self.semantic_analyzer = SemanticAnalyzer()

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

        except CompilerError as e:
            print(f"Compilation Error: {str(e)}")
            return None

    def generate_code(self, ast):
        # Simplified code generation for demonstration
        if ast[0] == 'add':
            return f'result = {ast[1][1]} + {ast[2][1]}'
        else:
            raise CompilerError("Unsupported operation for JIT compilation")

    def execute_code(self, generated_code):
        # Execute generated code dynamically
        namespace = {}
        exec(generated_code, globals(), namespace)
        return namespace['result']


class CompilerError(Exception):
    pass


class Lexer:
    def tokenize(self, source_code):
        # Simplified tokenization for demonstration
        return source_code.split()


class Parser:
    def parse(self, tokens):
        # Simplified parsing for demonstration
        if len(tokens) < 3 or tokens[1] not in {'+', '-', '*', '/'}:
            raise CompilerError("Syntax Error: Invalid arithmetic expression.")
        return ('add', ('number', int(tokens[0])), ('number', int(tokens[2])))


class SemanticAnalyzer:
    def analyze(self, ast):
        # Simulated semantic analysis - just an example
        if not ast or ast[0] != 'add':
            raise CompilerError("Semantic Error: Expected an addition operation.")
        return ast


# Example usage:

source_code = "3 + 5"

jit_compiler = JITCompiler()
result = jit_compiler.compile_and_execute(source_code)

if result is not None:
    print(f"Result of JIT compilation and execution: {result}")
