from dataclasses import dataclass
import Visitor

@dataclass
class Node:
  def accept(self, v:Visitor.Visitor(), *args, **kwargs):
    return v.visit(self, *args, **kwargs)

@dataclass
class Program(Node):
    def accept(self, v: Visitor.Visitor(), *args, **kwargs):
        return v.visit(self, *args, **kwargs)

# @dataclass
# class FunctionDeclaration(Node):
#     def __init__(self, name, arguments, local_variables, statements):
#         self.name = name
#         self.arguments = arguments
#         self.local_variables = local_variables
#         self.statements = statements