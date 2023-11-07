from dataclasses import dataclass
import Visitor

@dataclass
class Node:
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)

@dataclass
class Program(Node):
    name: str
    funclist: "FuncList"  # Representa la lista de funciones
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)

@dataclass
class FuncList(Node):
    functions: list  # Lista de funciones
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)

@dataclass
class Function(Node):
    name: str
    parmlist: "ParmList"  # Representa la lista de parámetros
    varlist: "VarList"    # Representa la lista de variables locales
    statements: "Statements"  # Representa el cuerpo de la función
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)

@dataclass
class ParmList(Node):
    parms: list  # Lista de parámetros
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)

@dataclass
class VarList(Node):
    decllist: "DeclList"  # Representa la lista de declaraciones
    optsemi: str  # Representa la opción de punto y coma
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)

@dataclass
class DeclList(Node):
    decls: list  # Lista de declaraciones
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)

@dataclass
class Decl(Node):
    parm: "Parm"  # Representa una declaración de parámetro
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)

@dataclass
class Parm(Node):
    name: str
    typename: str  # Representa el tipo de parámetro (INT, FLOAT, ARRAY, etc.)
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)

@dataclass
class Statements(Node):
    statements: list  # Lista de declaraciones
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)

@dataclass
class Statement(Node):
    statement: str  # Representa una declaración
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
    # hasme los nodos que nos hicieron falta en el parser

@dataclass
class Assign(Node):
    name: str
    expr: "Expression"
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
@dataclass
class If(Node):
    expr: "Expression"
    statements: "Statements"
    else_statements: "Statements"
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
@dataclass
class While(Node):
    expr: "Expression"
    statements: "Statements"
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
@dataclass
class For(Node):
    name: str
    expr: "Expression"
    statements: "Statements"
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
@dataclass
class Print(Node):
    expr: "Expression"
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
@dataclass
class Read(Node):
    name: str
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
@dataclass
class Return(Node):
    expr: "Expression"
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
@dataclass
class Expression(Node):
    expr: "Expression"
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
@dataclass
class ExpressionList(Node):
    exprlist: list
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# =====================================================================
# Expresiones

@dataclass
class Number(Expression):
    value: int
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
@dataclass
class String(Expression):
    value: str
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
@dataclass
class Boolean(Expression):
    value: bool
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# =====================================================================

@dataclass
class Binary(Expression):
    op: str
    left: Expression
    right: Expression
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# =====================================================================
# Funciones

@dataclass
class FunctionCall(Expression):
    func_name: str
    exprlist: "ExpressionList"
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# =====================================================================

@dataclass
class Array(Expression):
    array: list
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# =====================================================================

@dataclass
class ArrayAccess(Expression):
    name: str
    index: int
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# =====================================================================

@dataclass
class ArrayAssign(Expression):
    name: str
    index: int
    expr: "Expression"
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# =====================================================================

@dataclass
class ArrayAssignList(Expression):
    name: str
    exprlist: "ExpressionList"
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# =====================================================================
# Otros

@dataclass
class PrintString(Expression):
    value: str
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# =====================================================================

@dataclass
class PrintExpression(Expression):
    expr: "Expression"
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# =====================================================================

@dataclass
class PrintExpressionList(Expression):
    exprlist: "ExpressionList"
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# =====================================================================

@dataclass
class ReadExpression(Expression):
    name: str
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# =====================================================================

# @dataclass
# class ReadExpressionList(Expression):
#     exprlist: "ExpressionList"
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# =====================================================================

@dataclass
class ReadString(Expression):
    value: str
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# =====================================================================

# @dataclass
# class ReadStringList(Expression):
#     exprlist: "ExpressionList"
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# =====================================================================

@dataclass
class FunctionCallExpression(Expression):
    func_name: str
    exprlist: "ExpressionList"
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# =====================================================================

# @dataclass
# class FunctionCallExpressionList(Expression):
#     exprlist: "ExpressionList"
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# =====================================================================

@dataclass
class FunctionCallString(Expression):
    func_name: str
    value: str
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# =====================================================================

# @dataclass
# class FunctionCallStringList(Expression):
#     exprlist: "ExpressionList"
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# =====================================================================

@dataclass
class FunctionCallExpressionList(Expression):
    func_name: str
    exprlist: "ExpressionList"
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# =====================================================================

# @dataclass
# class FunctionCallExpressionListList(Expression):
#     exprlist: "ExpressionList"
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# =====================================================================

# @dataclass
# class FunctionCallStringListList(Expression):
#     exprlist: "ExpressionList"
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# =====================================================================

@dataclass
class FunctionCallStringList(Expression):
    func_name: str
    exprlist: "ExpressionList"
    value: str
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# =====================================================================

# TypeName, OptSemi, Location, ExprList, Unary, Identifier, Cast, Unary

# =====================================================================
# =====================================================================

@dataclass
class TypeName(Expression):
    typename: str
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# @dataclass
# class TypeNameList(Expression):
#     typename: str
#     exprlist: "ExpressionList"
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# =====================================================================

@dataclass
class OptSemi(Expression):
    optsemi: str
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# @dataclass
# class OptSemiList(Expression):
#     optsemi: str
#     exprlist: "ExpressionList"
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# =====================================================================

@dataclass
class Location(Expression):
    name: str
    index: int
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# @dataclass
# class LocationList(Expression):
#     name: str
#     index: int
#     exprlist: "ExpressionList"
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# =====================================================================

# @dataclass
# class ExprList(Expression):
#     exprlist: "ExpressionList"
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)
#

# =====================================================================

@dataclass
class Unary(Expression):
    op: str
    expr: "Expression"
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# @dataclass
# class UnaryList(Expression):
#     op: str
#     expr: "Expression"
#     exprlist: "ExpressionList"
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# =====================================================================

@dataclass
class Identifier(Expression):
    name: str
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
# @dataclass  
# class IdentifierList(Expression):
#     name: str
#     exprlist: "ExpressionList"
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)
#

# =====================================================================

@dataclass
class Cast(Expression):
    typename: str
    expr: "Expression"
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)

# @dataclass
# class CastList(Expression):
#     typename: str
#     expr: "Expression"
#     exprlist: "ExpressionList"
#     def accept(self, v: Visitor.Visitor, *args, **kwargs):
#         return v.visit(self, *args, **kwargs)

# =====================================================================

@dataclass
class UnaryMinus(Expression):
    expr: "Expression"
    def accept(self, v: Visitor.Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)
    
    
