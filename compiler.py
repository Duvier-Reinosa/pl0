from rich.console import Console
from rich.table import Table
from dataclasses import dataclass

# Class imports
from Lexer import Lexer
from Parser import Parser
# from Visitor import Visitor




# Main compiler code

if __name__ == '__main__':
    lexer = Lexer()
    parser = Parser()
    txt = open('tests/program1.pl0').read()

    # Crear una tabla para mostrar los tokens
    # console = Console()
    # table = Table(title="Tokens")
    # table.add_column("Token", justify="center")
    # table.add_column("Valor", justify="center")
    # table.add_column("Línea", justify="center")

    # for tok in lexer.tokenize(txt):
    #     # Agregar cada token a la tabla
    #     table.add_row(tok.type, str(tok.value), str(tok.lineno))

    # # Imprimir la tabla usando rich
    # console.print(table)