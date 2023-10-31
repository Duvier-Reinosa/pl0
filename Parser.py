import sly
import Lexer
import AstNodes

class Parser(sly.Parser):
    debugfile='pl0DEBUGFILE.txt'
  
    tokens = Lexer.Lexer.tokens

    @_("program IDENTIFIER SEMICOLON")
    def programDefinition(self, p):
        return AstNodes.Program(p.IDENTIFIER)
