from rich.console import Console
from rich.table import Table
from rich import print
from dataclasses import dataclass

# Class imports
from Lexer import Lexer
from Parser import Parser
from Dot import Dot, render_dot
from Eval import Eval
# from Visitor import Visitor




# Main compiler code

if __name__ == '__main__':
    lexer = Lexer()
    parser = Parser()

    txt = open('tests/fact.pl0').read()
    tokenized = lexer.tokenize(txt)
    ast = parser.parse(tokenized)

    print(ast)
    dot = render_dot(ast)
    print(dot)
    print(Eval.eval(ast))

    # Crear una tabla para mostrar los tokens
    # console = Console()
    # table = Table(title="Tokens")
    # table.add_column("Token", justify="center")
    # table.add_column("Valor", justify="center")
    # table.add_column("Línea", justify="center")

    # for tok in tokenized:
    #     # Agregar cada token a la tabla
    #     table.add_row(tok.type, str(tok.value), str(tok.lineno))

    # # Imprimir la tabla usando rich
    # console.print(table)

