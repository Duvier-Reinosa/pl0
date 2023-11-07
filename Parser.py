import sly
import Lexer
import AstNodes


# from dataclasses import dataclass
# import Visitor

# @dataclass
# class Node:
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# @dataclass
# class Program(Node):
#     name: str
#     funclist: "FuncList"  # Representa la lista de funciones
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# @dataclass
# class FuncList(Node):
#     functions: list  # Lista de funciones
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# @dataclass
# class Function(Node):
#     name: str
#     parmlist: "ParmList"  # Representa la lista de parámetros
#     varlist: "VarList"    # Representa la lista de variables locales
#     statements: "Statements"  # Representa el cuerpo de la función
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# @dataclass
# class ParmList(Node):
#     parms: list  # Lista de parámetros
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# @dataclass
# class VarList(Node):
#     decllist: "DeclList"  # Representa la lista de declaraciones
#     optsemi: str  # Representa la opción de punto y coma
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# @dataclass
# class DeclList(Node):
#     decls: list  # Lista de declaraciones
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# @dataclass
# class Decl(Node):
#     parm: "Parm"  # Representa una declaración de parámetro
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# @dataclass
# class Parm(Node):
#     name: str
#     typename: str  # Representa el tipo de parámetro (INT, FLOAT, ARRAY, etc.)
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# @dataclass
# class Statements(Node):
#     statements: list  # Lista de declaraciones
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# @dataclass
# class Statement(Node):
#     statement: str  # Representa una declaración
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# program ::= funclist

# funclist ::= funclist function
#     | function

# function ::= 'FUN' 'IDENT' parmlist varlist 'BEGIN' statements 'END'

# varlist ::= decllist optsemi
#     | 

# optsemi ::= ';'
#     |

# decllist ::= decllist ';' vardecl
#     | vardecl

# vardecl ::= parm 
#     | function

# parmlist ::= '(' parmlistitems ')'
#     | '(' ')'

# parmlistitems ::= parmlistitems ',' parm
#     | parm

# parm ::= 'IDENT' ':' typename

# typename ::= 'INT'
#     | 'FLOAT'
#     | 'INT' '[' expr ']'
#     | 'FLOAT' '[' expr ']'

# statements ::= statements ';' statement
#     | statement

# statement ::= 'PRINT' '(' 'STRING' ')'
#     | 'WRITE' '(' expr ')'
#     | 'READ' '(' location ')'
#     | 'WHILE' relop DO statement
#     | 'BREAK'
#     | 'IF' relop 'THEN' statement 
#     | 'IF' relop 'THEN' statement 'ELSE' statement
#     | 'BEGIN' statements 'END'
#     | location ':=' expr
#     | 'RETURN' expr
#     | 'SKIP'
#     | 'IDENT' '(' exprlist ')'

# location ::= 'IDENT'
#     | 'IDENT' '[' expr ']'

# exprlist ::= exprlistitems
#     |

# exprlistitems ::= exprlistitems ',' expr
#     | expr

# expr ::= expr '+' expr
#     | expr '-' expr
#     | expr '*' expr
#     | expr '/' expr
#     | '-' expr
#     | '+' expr
#     | '(' expr ')'
#     | 'IDENT' '[' expr ']'
#     | 'INUMBER'
#     | 'FNUMBER'
#     | 'IDENT' '(' exprlist ')'
#     | 'IDENT'
#     | 'INT' '(' expr ')'
#     | 'FLOAT' '(' expr ')'

# relop ::= expr 'LT' expr
#     | expr 'LE' expr
#     | expr 'GT' expr
#     | expr 'GE' expr
#     | expr 'EQ' expr
#     | expr 'NE' expr
#     | relop 'AND' relop
#     | relop 'OR' relop
#     | 'NOT' relop

class Parser(sly.Parser):
    debugfile='pl0DEBUGFILE.txt'
  
    tokens = Lexer.Lexer.tokens

    @_("funclist")
    def program(self, p):
        return AstNodes.Program(p.funclist)
    
    @_("funclist function")
    def funclist(self, p):
        return AstNodes.FuncList(p.funclist, p.function)
    
    @_("function")
    def funclist(self, p):
        return AstNodes.FuncList(p.function)
    
    @_("FUN IDENTIFIER LPAREN parmlist RPAREN varlist BEGIN statements END SEMICOLON NEWLINE")
    def function(self, p):
        return AstNodes.Function(p.IDENTIFIER, p.parmlist, p.varlist, p.statements)
    
    @_("IDENTIFIER COLON typename")
    def parm(self, p):
        return AstNodes.Parm(p.IDENTIFIER, p.typename)
    
    @_("parmlistitems")
    def parmlist(self, p):
        return AstNodes.ParmList(p.parmlistitems)
    
    @_("parmlistitems parm")
    def parmlistitems(self, p):
        return AstNodes.ParmList(p.parmlistitems, p.parm)
    
    @_("parm")
    def parmlistitems(self, p):
        return AstNodes.ParmList(p.parm)
    
    @_("INT")
    def typename(self, p):
        return AstNodes.TypeName(p.INT)
    
    @_("FLOAT")
    def typename(self, p):
        return AstNodes.TypeName(p.FLOAT)
    
    @_("INT LBRACKET expr RBRACKET")
    def typename(self, p):
        return AstNodes.TypeName(p.INT, p.expr)
    
    @_("FLOAT LBRACKET expr RBRACKET")
    def typename(self, p):
        return AstNodes.TypeName(p.FLOAT, p.expr)
    
    @_("decllist optsemi")
    def varlist(self, p):
        return AstNodes.VarList(p.decllist, p.optsemi)
    
    @_("decllist")
    def varlist(self, p):
        return AstNodes.VarList(p.decllist)
    
    @_("decllist SEMICOLON")
    def optsemi(self, p):
        return AstNodes.OptSemi(p.decllist, p.SEMICOLON)
    
    @_("decllist")
    def optsemi(self, p):
        return AstNodes.OptSemi(p.decllist)
    
    @_("decllist SEMICOLON vardecl")
    def decllist(self, p):
        return AstNodes.DeclList(p.decllist, p.vardecl)
    
    @_("vardecl")
    def decllist(self, p):
        return AstNodes.DeclList(p.vardecl)
    
    @_("parm")
    def vardecl(self, p):
        return AstNodes.Decl(p.parm)
    
    @_("function")
    def vardecl(self, p):
        return AstNodes.Decl(p.function)
    
    @_("statements")
    def statements(self, p):
        return AstNodes.Statements(p.statements)
    
    @_("statements SEMICOLON statement")
    def statements(self, p):
        return AstNodes.Statements(p.statements, p.statement)
    
    @_("PRINT LPAREN SCONST RPAREN")
    def statement(self, p):
        return AstNodes.Statement(p.SCONST)
    
    @_("WRITE LPAREN expr RPAREN")
    def statement(self, p):
        return AstNodes.Statement(p.expr)
    
    @_("READ LPAREN location RPAREN")
    def statement(self, p):
        return AstNodes.Statement(p.location)
    
    @_("WHILE relop DO statement")
    def statement(self, p):
        return AstNodes.Statement(p.relop, p.statement)
    
    @_("BREAK")
    def statement(self, p):
        return AstNodes.Statement(p.BREAK)
    
    @_("IF relop THEN statement")
    def statement(self, p):
        return AstNodes.Statement(p.relop, p.statement)
    
    @_("IF relop THEN statement ELSE statement")
    def statement(self, p):
        return AstNodes.Statement(p.relop, p.statement, p.statement)
    
    @_("BEGIN statements END")
    def statement(self, p):
        return AstNodes.Statement(p.statements)
    
    @_("location ASSIGN expr")
    def statement(self, p):
        return AstNodes.Statement(p.location, p.expr)
    
    @_("RETURN expr")
    def statement(self, p):
        return AstNodes.Statement(p.expr)
    
    @_("SKIP")
    def statement(self, p):
        return AstNodes.Statement(p.SKIP)
    
    @_("IDENTIFIER LPAREN exprlist RPAREN")
    def statement(self, p):
        return AstNodes.Statement(p.IDENTIFIER, p.exprlist)
    
    @_("IDENTIFIER")
    def location(self, p):
        return AstNodes.Location(p.IDENTIFIER)
    
    @_("IDENTIFIER LBRACKET expr RBRACKET")
    def location(self, p):
        return AstNodes.Location(p.IDENTIFIER, p.expr)
    
    @_("exprlistitems")
    def exprlist(self, p):
        return AstNodes.ExprList(p.exprlistitems)
    
    @_("exprlistitems expr")
    def exprlistitems(self, p):
        return AstNodes.ExprList(p.exprlistitems, p.expr)
    
    @_("expr")
    def exprlistitems(self, p):
        return AstNodes.ExprList(p.expr)
    
    @_("expr PLUS expr")
    def expr(self, p):
        return AstNodes.Binary(p.PLUS, p.expr0, p.expr1)
    
    @_("expr MINUS expr")
    def expr(self, p):
        return AstNodes.Binary(p.MINUS, p.expr0, p.expr1)
    
    @_("expr TIMES expr")
    def expr(self, p):
        return AstNodes.Binary(p.TIMES, p.expr0, p.expr1)
    
    @_("expr DIVIDE expr")
    def expr(self, p):
        return AstNodes.Binary(p.DIVIDE, p.expr0, p.expr1)
    
    @_("MINUS expr")
    def expr(self, p):
        return AstNodes.Unary(p.MINUS, p.expr)
    
    @_("PLUS expr")
    def expr(self, p):
        return AstNodes.Unary(p.PLUS, p.expr)
    
    @_("LPAREN expr RPAREN")
    def expr(self, p):
        return AstNodes.Paren(p.expr)
    
    @_("IDENTIFIER LBRACKET expr RBRACKET")
    def expr(self, p):
        return AstNodes.Array(p.IDENTIFIER, p.expr)
    
    @_("INUMBER")
    def expr(self, p):
        return AstNodes.Number(p.INUMBER)
    
    @_("FNUMBER")
    def expr(self, p):
        return AstNodes.Number(p.FNUMBER)
    
    @_("IDENTIFIER LPAREN exprlist RPAREN")
    def expr(self, p):
        return AstNodes.FunctionCall(p.IDENTIFIER, p.exprlist)
    
    @_("IDENTIFIER")
    def expr(self, p):
        return AstNodes.Identifier(p.IDENTIFIER)
    
    @_("INT LPAREN expr RPAREN")
    def expr(self, p):
        return AstNodes.Cast(p.INT, p.expr)
    
    @_("FLOAT LPAREN expr RPAREN")
    def expr(self, p):
        return AstNodes.Cast(p.FLOAT, p.expr)
    
    @_("expr LT expr")
    def relop(self, p):
        return AstNodes.Binary(p.LT, p.expr0, p.expr1)
    
    @_("expr LE expr")
    def relop(self, p):
        return AstNodes.Binary(p.LE, p.expr0, p.expr1)
    
    @_("expr GT expr")
    def relop(self, p):
        return AstNodes.Binary(p.GT, p.expr0, p.expr1)
    
    @_("expr GE expr")
    def relop(self, p):
        return AstNodes.Binary(p.GE, p.expr0, p.expr1)
    
    @_("expr EQ expr")
    def relop(self, p):
        return AstNodes.Binary(p.EQ, p.expr0, p.expr1)
    
    @_("expr NE expr")
    def relop(self, p):
        return AstNodes.Binary(p.NE, p.expr0, p.expr1)
    
    @_("relop AND relop")
    def relop(self, p):
        return AstNodes.Binary(p.AND, p.relop0, p.relop1)
    
    @_("relop OR relop")
    def relop(self, p):
        return AstNodes.Binary(p.OR, p.relop0, p.relop1)
    
    @_("NOT relop")
    def relop(self, p):
        return AstNodes.Unary(p.NOT, p.relop)
    
    @_("programDefinition")
    def program(self, p):
        return AstNodes.Program(p.programDefinition)



    # @_("program IDENTIFIER SEMICOLON NEWLINE")
    # def programDefinition(self, p):
    #     return AstNodes.Program(p.IDENTIFIER)
    
    # @_("programDefinition funcList")
    # def programDefinition(self, p):
    #     return AstNodes.Program(p.programDefinition, p.funcList)
    
    # @_("funcList")
    # def programDefinition(self, p):
    #     return AstNodes.Program(p.funcList)
    
    # @_("funcList function")
    # def funcList(self, p):
    #     return AstNodes.FuncList(p.funcList, p.function)
    
    # @_("function")
    # def funcList(self, p):
    #     return AstNodes.FuncList(p.function)
    
    # @_("functionDefinition")
    # def function(self, p):
    #     return AstNodes.Function(p.functionDefinition)
    
    # @_("functionDefinition function")
    # def function(self, p):
    #     return AstNodes.Function(p.functionDefinition, p.function)
    
    # @_("FUN IDENTIFIER LPAREN RPAREN BEGIN statements END SEMICOLON NEWLINE")
    # def functionDefinition(self, p):
    #     print(p)
    #     return AstNodes.Function(p.IDENTIFIER, p.statements)
    
    



