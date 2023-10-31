import sly

class Lexer(sly.Lexer):
    tokens = {
        # Palabras Reservadas
        'program', 'FUN', 'LOCALS', 'BEGIN', 'END', 'IF', 'THEN', 'ELSE', 'PRINT', 'WRITE', 'READ', 'RETURN', 'SKIP', 'BREAK', 'INT', 'FLOAT', 'FOR',  # Agregamos 'FOR' como palabra reservada

        # Literales
        'ICONST', 'RCONST', 'SCONST', 'IDENTIFIER',

        # Operadores y símbolos
        'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN', 'COLON', 'LPAREN', 'RPAREN', 'COMMA', 'SEMICOLON', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE', 'LBRACKET', 'RBRACKET',
        'NEWLINE'  # Agregamos el token NEWLINE
    }

    # Ignora espacios en blanco y comentarios
    NEWLINE = r'\n'  # Agregamos el token NEWLINE
    ignore = ' \t\r'
    ignore_comment = r'\#.*'

    literals = {'+', '-', '*', '/', ':', '=', ',', ';', '(', ')', '[', ']'}

    def __init__(self):
        self.lineno = 1  # Variable para mantener el número de línea actual
    
    # Palabras reservadas
    FOR = r'for'  # Agregamos el token 'FOR'
    program = r'program'

    # Literales
    SCONST = r'"[^"]*"'
    IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'

    # Expresiones regulares para los tokens
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    ASSIGN = r':='
    COLON = r':'
    LPAREN = r'\('
    RPAREN = r'\)'
    COMMA = r','
    SEMICOLON = r';'
    LE = r'<='
    GE = r'>='
    EQ = r'=='
    LT = r'<'
    GT = r'>'
    NE = r'!='
    LBRACKET = r'\['
    RBRACKET = r'\]'

    @_(r'\d+\.\d*')
    def RCONST(self, t):
        t.value = float(t.value)
        return t

    @_(r'\d+')
    def ICONST(self, t):
        t.value = int(t.value)
        return t

    @_(r'\n+')
    def NEWLINE(self, t):
        self.lineno += t.value.count('\n')  # Incrementa el número de línea por cada salto de línea
        return t

    def error(self, t):
        print(f"Caracter ilegal '{t.value[0]}' en la línea {self.lineno}")
        self.index += 1
