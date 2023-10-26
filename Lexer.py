import sly

class Lexer(sly.Lexer):
    tokens = {
        # Palabras Reservadas
        'FUN', 'LOCALS', 'BEGIN', 'END', 'IF', 'THEN', 'ELSE', 'PRINT', 'WRITE', 'READ', 'RETURN', 'SKIP', 'BREAK', 'INT', 'FLOAT', 'FOR',  # Agregamos 'FOR' como palabra reservada

        # Literales
        'ICONST', 'RCONST', 'SCONST', 'IDENT',

        # Operadores y símbolos
        'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN', 'COLON', 'LPAREN', 'RPAREN', 'COMMA', 'SEMICOLON', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE', 'LBRACKET', 'RBRACKET'
    }

    # Ignora espacios en blanco y comentarios
    ignore = ' \t\r'
    ignore_comment = r'\#.*'

    literals = {'+', '-', '*', '/', ':', '=', ',', ';', '(', ')', '[', ']'}

    def __init__(self):
        self.lineno = 1  # Variable para mantener el número de línea actual

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


    # Palabras reservadas
    FOR = r'for'  # Agregamos el token 'FOR'

    # Literales
    SCONST = r'"[^"]*"'
    IDENT = r'[a-zA-Z][a-zA-Z0-9]*'

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
