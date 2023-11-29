from AstNodes import *

class Eval():
    def __init__(self):
        self.variables = [] 

    @classmethod
    def eval(cls, n:Node):
      vis = cls()
      return n.accept(vis)

    def visit_Program(self, node: Program):
        # Lógica para manejar un nodo Program
        for function in node.functions:
            self.visit_Function(function)  # Llama a visit_Function en lugar de visit_AssignmentStatement

        # Retorna un valor si es necesario, dependiendo de tu lógica de evaluación

    # Asegúrate de tener un método visit_Function para manejar los nodos Function
    def visit_Function(self, node: Function):
        # Lógica para evaluar una función
        for param in node.parameters:
            self.visit_Parameter(param)  # Llama al método específico para Parameter
        for var in node.var_declarations:
            self.visit_VarDeclaration(var)  # Llama al método específico para VarDeclaration
        for stmt in node.statements:
            self.generic_visit(stmt)  # Puedes usar un método genérico que redirija a visit_<TipoDeNodo>

    def visit_Parameter(self, node: Parameter):
        # Lógica para manejar un parámetro
        pass

    def visit_VarDeclaration(self, node: VarDeclaration):
        # Lógica para manejar una declaración de variable
        pass

    def generic_visit(self, node):
        # Método genérico que redirige a métodos específicos
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.unhandled_node)
        return visitor(node)

    def unhandled_node(self, node):
        # Lógica para manejar nodos no soportados o no esperados
        raise Exception(f'No visit_{type(node).__name__} method')

    def visit_AssignmentStatement(self, node: AssignmentStatement):
        # Lógica para manejar un nodo AssignmentStatement
        left_value = self.visit_VariableExpression(node.left)
        right_value = self.visit(node.right)
        # Implementa la lógica de asignación aquí

    # ... y así sucesivamente para cada tipo de nodo ...

    def visit_VariableExpression(self, node: VariableExpression):
        # Lógica para manejar un nodo VariableExpression
        # Retorna el valor de la variable
        return node.value

    def visit_BinaryExpression(self, node: BinaryExpression):
        # Evalúa ambos lados de la expresión
        left_value = node.left.accept(self)
        right_value = node.right.accept(self)

        # Realiza la operación correspondiente según el operador
        if node.operator == '+':
            return left_value + right_value
        elif node.operator == '-':
            return left_value - right_value
        elif node.operator == '*':
            return left_value * right_value
        elif node.operator == '/':
            return left_value / right_value
        elif node.operator == '%':
            return left_value % right_value
        # Agrega aquí más operadores si es necesario
        else:
            raise Exception(f'Operador no soportado: {node.operator}')
        
    def visit_IfStatement(self, node: IfStatement):
        condition_value = node.condition.accept(self)
        if condition_value:
            self.generic_visit(node.if_block)
        else:
            # Verificar si else_block es un ReturnStatement
            if isinstance(node.else_block, ReturnStatement):
                # Manejar el caso de un solo ReturnStatement
                return node.else_block.accept(self)
            else:
                # Si no es un ReturnStatement, visitarlo como cualquier otra lista de statements
                self.generic_visit(node.else_block)
  
    def visit_RelationalExpression(self, node: RelationalExpression):
          left_value = node.left.accept(self)
          right_value = node.right.accept(self)

          if node.operator == '<':
              return left_value < right_value
          elif node.operator == '>':
              return left_value > right_value
          elif node.operator == '<=':
              return left_value <= right_value
          elif node.operator == '>=':
              return left_value >= right_value
          elif node.operator == '==':
              return left_value == right_value
          elif node.operator == '!=':
              return left_value != right_value
          else:
              raise Exception(f'Operador no soportado: {node.operator}')
    def visit_VariableExpression(self, node: VariableExpression):
        # Buscar la variable en la lista de variables y obtener su valor
        for var_name, var_value in self.variables:
            if var_name == node.var_name:
                return var_value
        # Si la variable no se encuentra, devolver un valor predeterminado (por ejemplo, 0)
        return 0

    def visit_AssignmentStatement(self, node: AssignmentStatement):
        # Evaluar la expresión del lado derecho
        value = node.right.accept(self)

        # Buscar la variable en la lista de variables y actualizar su valor si existe
        for i, (var_name, _) in enumerate(self.variables):
            if var_name == node.left.var_name:
                self.variables[i] = (var_name, value)
                return value

        # Si la variable no existe en la lista, agregarla
        self.variables.append((node.left.var_name, value))
        return value
    
    def visit_NumberLiteral(self, node: NumberLiteral):
        return node.value  # Puedes simplemente devolver el valor numérico del nodo
    
    def visit_ReturnStatement(self, node: ReturnStatement):
        return node.expr.accept(self)
    
    def visit_FunctionCall(self, node):
        # Obtén el nombre de la función
        function_name = node.function_name

        # Obtén los argumentos de la función (que son una lista de expresiones)
        arguments = node.arguments

        # Realiza las acciones necesarias en función de la llamada a la función.
        if function_name == 'print':
            # Si la función es 'print', evalúa y muestra los argumentos en la consola
            values = [arg.accept(self) for arg in arguments]
            result = ' '.join(map(str, values))
            print(result)
            return None  # La función 'print' no devuelve un valor
        elif function_name == 'fact':
            # Si la función es 'fact', calcula el factorial del primer argumento
            if len(arguments) != 1:
                raise Exception('La función "fact" debe tener un solo argumento')
            n = arguments[0].accept(self)
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result

        # Puedes agregar más casos para otras funciones aquí

        # Si la función no se reconoce, puedes lanzar un error
        raise Exception(f'Función no reconocida: {function_name}')
    
    def visit_PrintStatement(self, node: PrintStatement):
        # Obtén la expresión que se va a imprimir
        expression = node.value

        if isinstance(expression, str):
            # Verifica si la cadena representa un número
            if expression.isdigit():
                # Convierte la cadena en un nodo NumberLiteral
                expression = NumberLiteral(int(expression))
            else:
                # La cadena representa una cadena de caracteres, simplemente imprímela
                print(expression)
                return None

        if not isinstance(expression, Node):
            # Maneja otros casos según tu lógica si expression no es un nodo del AST
            raise Exception(f'Expresión no válida para imprimir: {expression}')

        # Evalúa la expresión y muestra su valor en la consola
        result = expression.accept(self)
        print(result)

    def visit_ReadStatement(self, node: ReadStatement):
        # Lógica para manejar un nodo ReadStatement
        variable_name = node.location.var_name

        # Solicita al usuario que ingrese un valor y lo almacena en la variable
        input_value = input(f'Ingrese un valor para la variable "{variable_name}": ')

        try:
            # Intenta convertir el valor ingresado en un número entero
            input_value = int(input_value)
        except ValueError:
            # Si no se puede convertir en un número, muestra un mensaje de error
            raise Exception(f'El valor ingresado para la variable "{variable_name}" no es un número válido.')

        # Almacena el valor en la lista de variables
        self.variables.append((variable_name, input_value))

    def visit_WriteStatement(self, node: WriteStatement):
      # Obtén el valor de la expresión que se va a escribir
      value = node.expression.accept(self)
      
      # Aquí debes implementar la lógica para escribir el valor en la salida estándar o en otro lugar
      # Por ejemplo, puedes imprimirlo en la consola
      print(value)





