import math 
from dataclasses import dataclass

from Visitor import Visitor


# =====================================================================
# Arbol de Sintaxis Abstracto
#

@dataclass
class Node:
  def accept(self, v:Visitor, *args, **kwargs):
    return v.visit(self, *args, **kwargs)

@dataclass
class Expression(Node):
  ...

@dataclass
class Number(Expression):
  value : int

@dataclass
class Binary(Expression):
  op    : str
  left  : Expression
  right : Expression

@dataclass
class Factorial(Expression):
    expr: Expression

@dataclass
class FunctionCall(Expression):
    func_name: str
    expr: Expression

@dataclass
class Assignment(Node):
  variable: str
  expr: Expression

  def accept(self, v: Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)

@dataclass
class Variables:
  _vars = {'pi': math.pi, 'e': math.e}

  @classmethod
  def get(cls, name):
      return cls._vars.get(name)

  @classmethod
  def set(cls, name, value):
      cls._vars[name] = value