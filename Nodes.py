class Node:
    pass

class Program(Node):
    def __init__(self, function_declarations):
        self.function_declarations = function_declarations

class FunctionDeclaration(Node):
    def __init__(self, name, arguments, local_variables, statements):
        self.name = name
        self.arguments = arguments
        self.local_variables = local_variables
        self.statements = statements