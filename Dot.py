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
  
  def visit(self, n: FuncList):
    self.dot.node('FuncList', label=f'FuncList')
    for func in n.functions:
      func.accept(self)
    return
  
  def visit(self, n: Function):
    name = self.name()
    self.dot.node(name, label=f'Function\nName: {n.name}')
    n.parmlist.accept(self)
    n.varlist.accept(self)
    n.statements.accept(self)
    self.dot.edge('FuncList', name)
    return
  
  def visit(self, n: ParmList):
    self.dot.node('ParmList', label=f'ParmList')
    for parm in n.parms:
      parm.accept(self)
    return
  
  def visit(self, n: Parm):
    name = self.name()
    self.dot.node(name, label=f'Parm\nName: {n.name}\nType: {n.typename}')
    self.dot.edge('ParmList', name)
    return
  
  def visit(self, n: VarList):
    self.dot.node('VarList', label=f'VarList')
    n.decllist.accept(self)
    return
  
  def visit(self, n: DeclList):
    self.dot.node('DeclList', label=f'DeclList')
    for decl in n.decls:
      decl.accept(self)
    return
  
  def visit(self, n: Decl):
    name = self.name()
    self.dot.node(name, label=f'Decl\nName: {n.parm.name}\nType: {n.parm.typename}')
    self.dot.edge('DeclList', name)
    return
  
  def visit(self, n: Statements):
    self.dot.node('Statements', label=f'Statements')
    for statement in n.statements:
      statement.accept(self)
    return
  
  def visit(self, n: Statement):
    name = self.name()
    self.dot.node(name, label=f'Statement\n{str(n.statement)}')
    self.dot.edge('Statements', name)
    return

  
  
