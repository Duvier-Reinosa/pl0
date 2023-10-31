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
