from dataclasses import dataclass
from Visitor import Visitor
from typing import Union, Optional, List


class Node:
    def accept(self, visitor, *args, **kwargs):
        # Redirecciona a los métodos específicos basado en el tipo del nodo
        method_name = 'visit_' + type(self).__name__
        visitor_method = getattr(visitor, method_name, self.generic_visit)
        return visitor_method(self, *args, **kwargs)

    def generic_visit(self, visitor, *args, **kwargs):
        raise Exception(f'No visit_{type(self).__name__} method in {type(visitor).__name__}')


# Nodo para un programa completo
@dataclass
class Program(Node):
    functions: list  # Lista de nodos Function
    def accept(self, visitor, *args, **kwargs):
        return visitor.visit_Program(self, *args, **kwargs)

# Nodo para una función
@dataclass
class Function(Node):
    name: str
    parameters: list  # Lista de nodos Parameter
    var_declarations: list  # Lista de nodos VarDeclaration
    statements: list  # Lista de nodos Statement

# Nodo para declaraciones de variables
@dataclass
class VarDeclaration(Node):
    var_name: str
    var_type: str
    array_size: Node  # Nodo Expression si es un arreglo, None si no lo es

# Nodo para parámetros de función
@dataclass
class Parameter(Node):
    param_name: str
    param_type: str

@dataclass
class ReadStatement(Node):
    location: Node  # Suponiendo que 'Node' es la clase base de tus nodos AST

    def __init__(self, location):
        self.location = location

    def __repr__(self):
        return f"ReadStatement(location={self.location})"

# Nodo para los tipos de datos
@dataclass
class TypeName(Node):
    type_name: str
    array_size: Optional[Node] = None  # Añade esto si necesitas almacenar el tamaño del array

    def __repr__(self):
        if self.array_size:
            return f"TypeName({self.type_name}, array_size={self.array_size})"
        else:
            return f"TypeName({self.type_name})"


# Nodo para las declaraciones (statements)
@dataclass
class Statement(Node):
    # Esta clase podría ser abstracta y servir como base para diferentes tipos de statements
    pass

# Ejemplos de nodos para diferentes tipos de statements
@dataclass
class PrintStatement(Statement):
    value: Node  # Nodo Expression

@dataclass
class AssignmentStatement(Statement):
    left: Node  # Nodo Location
    right: Node  # Nodo Expression

@dataclass
class IfStatement(Statement):
    condition: Node  # Nodo Expression
    then_block: list  # Lista de nodos Statement
    else_block: list  # Lista de nodos Statement (opcional)

# ... otros tipos de statements ...

# Nodo para expresiones
@dataclass
class Expression(Node):
    # Similar a Statement, esta clase podría ser una base para diferentes tipos de expresiones
    pass

# Ejemplos de nodos para diferentes tipos de expresiones
@dataclass
class BinaryExpression(Expression):
    left: Node
    operator: str
    right: Node

@dataclass
class UnaryExpression(Expression):
    operator: str
    operand: Node

@dataclass
class LiteralExpression(Expression):
    value: str

@dataclass
class VariableExpression(Expression):
    var_name: str

from dataclasses import dataclass
import Visitor

@dataclass
class Expression(Node):
    pass

# Expresiones binarias (como suma, resta, multiplicación, división)
@dataclass
class BinaryExpression(Expression):
    left: Expression
    operator: str
    right: Expression

# Expresiones unarias (como negación)
@dataclass
class UnaryExpression(Expression):
    operator: str
    operand: Expression

# Expresiones literales (números enteros, números flotantes)
@dataclass
class LiteralExpression(Expression):
    value: str  # Puede ser 'INUMBER' o 'FNUMBER'

# Identificadores (variables)
@dataclass
class IdentifierExpression(Expression):
    name: str

# Expresiones de llamada a función
@dataclass
class FunctionCallExpression(Expression):
    function_name: str
    arguments: list  # Lista de Expression

# Expresiones de acceso a arreglo
@dataclass
class ArrayAccessExpression(Expression):
    array_name: str
    index: Expression

# Expresiones de tipo (para conversiones de tipo)
@dataclass
class TypeExpression(Expression):
    type_name: str
    expression: Expression

# Expresiones relacionales (como <, <=, >, >=, ==, !=)
@dataclass
class RelationalExpression(Expression):
    left: Expression
    operator: str
    right: Expression

# Expresiones lógicas (AND, OR)
@dataclass
class LogicalExpression(Expression):
    left: Expression
    operator: str
    right: Expression

# Expresión NOT
@dataclass
class NotExpression(Expression):
    expression: Expression


# Nodo para ubicaciones (locations)
@dataclass
class Location(Node):
    var_name: str
    index: Node  # Nodo Expression si es un arreglo, None si no lo es

@dataclass
class NumberLiteral(Node):
    value: Union[int, float]

    def __repr__(self):
        return f"NumberLiteral({self.value})"

@dataclass
class BlockStatement(Node):
    statements: List[Node]

    def __repr__(self):
        return f"BlockStatement({self.statements})"


@dataclass
class WhileStatement(Node):
    condition: Node   # La condición del bucle while
    body: Node        # El cuerpo del bucle while

    def __repr__(self):
        return f"WhileStatement(condition={self.condition}, body={self.body})"

@dataclass
class ReturnStatement(Node):
    expression: Optional[Expression]  # La expresión que se retorna

    def __init__(self, expression: Optional[Expression] = None):
        self.expression = expression

    def __repr__(self):
        return f"ReturnStatement(expression={self.expression})"



@dataclass
class FunctionCall(Node):
    function_name: str
    arguments: List[Expression]

    def __repr__(self):
        return f"FunctionCall(function_name={self.function_name}, arguments={self.arguments})"

@dataclass
class WriteStatement(Node):
    expression: Expression  # La expresión cuyo valor se va a escribir

    def __repr__(self):
        return f"WriteStatement(expression={self.expression})"



@dataclass
class ReturnStatement(Node):
    expr: Expression  # La expresión que se retorna

    def __repr__(self):
        return f"ReturnStatement(expression={self.expr})"
