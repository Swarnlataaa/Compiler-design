import tkinter as tk
from tkinter import scrolledtext
from idlelib.colorizer import ColorDelegator
from idlelib.autocomplete import Autocomplete
from idlelib.tooltip import Hovertip
from idlelib.percolator import Percolator


class SimpleIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple IDE")

        # Text editor
        self.text_widget = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Courier New", 12))
        self.text_widget.pack(expand=True, fill='both')

        # Syntax highlighting
        self.colorizer = ColorDelegator()
        Percolator(self.text_widget).insertfilter(self.colorizer)

        # Autocomplete
        self.autocomplete = Autocomplete(self.text_widget)
        self.autocomplete.set_completion_list(['+', '-', '*', '/'])

        # Real-time error checking
        self.error_label = tk.Label(self.root, text="", fg="red")
        self.error_label.pack()

        # Hover tooltips
        Hovertip(self.text_widget)

        # Bind events
        self.text_widget.bind('<KeyRelease>', self.check_errors)

    def check_errors(self, event):
        source_code = self.text_widget.get("1.0", "end-1c")
        try:
            # Simulated syntax analysis
            syntax_analyzer = SyntaxAnalyzer()
            abstract_syntax_tree = syntax_analyzer.analyze(source_code)
            # Simulated semantic analysis
            semantic_analyzer = SemanticAnalyzer()
            validated_ast = semantic_analyzer.analyze(abstract_syntax_tree)
            # Clear previous errors
            self.error_label.config(text="")
        except CompilerError as e:
            # Display error message
            self.error_label.config(text=str(e))


class CompilerError(Exception):
    pass


class SyntaxAnalyzer:
    def analyze(self, source_code):
        # Simulated syntax analysis - just an example
        if not source_code.strip():
            raise CompilerError("Error: Empty source code.")
        tokens = source_code.split()
        if len(tokens) < 3 or tokens[1] not in {'+', '-', '*', '/'}:
            raise CompilerError("Syntax Error: Invalid arithmetic expression.")
        return ('add', ('number', int(tokens[0])), ('number', int(tokens[2])))


class SemanticAnalyzer:
    def analyze(self, ast):
        # Simulated semantic analysis - just an example
        if not ast or ast[0] != 'add':
            raise CompilerError("Semantic Error: Expected an addition operation.")
        return ast


if __name__ == "__main__":
    root = tk.Tk()
    ide = SimpleIDE(root)
    root.mainloop()
