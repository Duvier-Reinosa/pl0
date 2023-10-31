from Visitor import Visitor
from graphviz import Digraph
from AstNodes import *
# =====================================================================
# Dibuja el AST
#
class Dot():
  node_defaults = {
    'shape' : 'box',
    'color' : 'cyan',
    'style' : 'filled',
  }
  edge_defaults = {
    'arrowhead' : 'none',
  }

  def __init__(self):
    self.dot = Digraph('AST')
    self.dot.attr('node', **self.node_defaults)
    self.dot.attr('edge', **self.edge_defaults)
    self.seq = 0
  
  def __str__(self):
    return self.dot.source
  
  def __repr__(self):
    return self.dot.source

  def name(self):
    self.seq += 1
    return f'n{self.seq:02d}'

  @classmethod
  def render(cls, n:Node):
    dot = cls()
    n.accept(dot)
    return dot.dot
  
  def visit(self, n: Program):
    self.dot.node('Program', label=f'Program\nName: {n.name}')
    return
  
  # def visit(self, n:Number):
  #   name = self.name()
  #   self.dot.node(name, label=f'{n.value}')
  #   return name
  
  # def visit(self, n:Binary):
  #   name = self.name()
  #   left  = n.left.accept(self)
  #   right = n.right.accept(self)
  #   self.dot.node(name, label=f'{n.op}', shape='circle', color='bisque')
  #   self.dot.edge(name, left)
  #   self.dot.edge(name, right)
  #   return name
  
  # def visit(self, n:Assignment):
  #   name = self.name()
  #   self.dot.node(name, label=f'Assignment\nVariable: {n.variable}')
  #   expr_name = n.expr.accept(self)
  #   self.dot.edge(name, expr_name)
  #   return name

  # def visit(self, n:FunctionCall):
  #   name = self.name()
  #   self.dot.node(name, label=f'FunctionCall\nFunction: {n.func_name}')
  #   expr_name = n.expr.accept(self)
  #   self.dot.edge(name, expr_name)
  #   return name
