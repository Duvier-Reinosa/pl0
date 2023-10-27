import sly
import Lexer
import Nodes

class Parser(sly.Parser):
    debugfile='pl0DEBUGFILE.txt'
  
    tokens = Lexer.Lexer.tokens

    @_('program IDENTIFIER')
    def programDefinition(self, p):
        return Nodes.Program(p.IDENTIFIER)

    

    def error(self, p):
        print(p)
        self.errors.append(f"Error sintáctico en línea {p.lineno}: Token inesperado '{p.value}'")
        self.index += 1  # Avanzar al siguiente token

    # Opcionalmente, puedes proporcionar una función para obtener los errores
    def get_errors(self):
        return self.errors

    def __init__(self):
        super().__init__()
        self.errors = []