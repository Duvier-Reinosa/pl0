# model.py
from dataclasses import dataclass

@dataclass
class Node:
    pass

@dataclass
class Statement(Node):
    pass

@dataclass
class Expression(Node):
    pass

@dataclass
class Program(Node):
    def __init__(self, declarations):
        self.declarations = declarations

@dataclass
class FunctionDeclaration(Node):
    name: str
    arguments: list
    local_variables: list
    statements: list

@dataclass
class Argument:
    name: str
    data_type: str

@dataclass
class LocalVariable:
    name: str
    data_type: str

@dataclass
class AssignmentStatement(Statement):
    identifier: str
    expression: Expression

@dataclass
class WhileStatement(Statement):
    condition: Expression
    body: Statement

@dataclass
class IfStatement(Statement):
    condition: Expression
    then_body: Statement
    else_body: Statement

@dataclass
class PrintStatement(Statement):
    expressions: list

@dataclass
class WriteStatement(Statement):
    expression: Expression

@dataclass
class ReadStatement(Statement):
    identifier: str

@dataclass
class ReturnStatement(Statement):
    expression: Expression

@dataclass
class FunctionCallStatement(Statement):
    function_name: str
    arguments: list

@dataclass
class Block(Statement):
    statements: list

@dataclass
class DataType:
    name: str

@dataclass
class ExpressionList:
    expressions: list

@dataclass
class BinaryExpression(Expression):
    operator: str
    left: Expression
    right: Expression

@dataclass
class UnaryExpression(Expression):
    operator: str
    operand: Expression

@dataclass
class ParenthesizedExpression(Expression):
    expression: Expression

@dataclass
class Identifier(Expression):
    name: str

@dataclass
class NumberLiteral(Expression):
    value: float

@dataclass
class FunctionCall(Expression):
    function_name: str
    arguments: list
