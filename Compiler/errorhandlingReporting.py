class CompilerError(Exception):
    pass


class LexicalAnalyzer:
    def analyze(self, source_code):
        # Simulated lexical analysis - just an example
        if not source_code.strip():
            raise CompilerError("Error: Empty source code.")

        tokens = source_code.split()
        return tokens


class SyntaxAnalyzer:
    def analyze(self, tokens):
        # Simulated syntax analysis - just an example
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

try:
    # Lexical analysis
    lexical_analyzer = LexicalAnalyzer()
    tokens = lexical_analyzer.analyze(source_code)

    # Syntax analysis
    syntax_analyzer = SyntaxAnalyzer()
    abstract_syntax_tree = syntax_analyzer.analyze(tokens)

    # Semantic analysis
    semantic_analyzer = SemanticAnalyzer()
    validated_ast = semantic_analyzer.analyze(abstract_syntax_tree)

    # Continue with further compilation stages...

except CompilerError as e:
    print(f"Compilation Error: {str(e)}")
