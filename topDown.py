'''
topdown.py

Analizador descendente recursivo.
'''
from dataclasses import dataclass
from model import *

import re

# =======================================
# ANALISIS LEXICO
# =======================================
@dataclass
class Token:
	'''
	Representacion de un token
	'''
	type  : str
	value : float or str
	lineno: int = 1


class Tokenizer:
	
	tokens = [
		(r'\n', lambda s, tok: Token('NEWLINE', tok)),
		(r'\s+', None),
		(r'//.*', None),
		(r'"[^"]*"', lambda s, tok: Token('SCONST', tok)),
		(r'\d+(\.\d+)?(E[-+]?\d+)?', lambda s, tok: Token('RCONST', tok)),
		(r'\d+', lambda s, tok: Token('ICONST', tok)),
		(r'[Bb][Ee][Gg][Ii][Nn]', lambda s, tok: Token('BEGIN', tok)),
		(r'[Ee][Nn][Dd]', lambda s, tok: Token('END', tok)),
		(r'[Ii][Ff]', lambda s, tok: Token('IF', tok)),
		(r'[a-zA-Z_]\w*', lambda s, tok: Token('IDENT', tok)),
		(r'[tT][hH][eE][nN]', lambda s, tok: Token('THEN', tok)),
		(r'\+', lambda s, tok: Token('+', tok)),
		(r'-', lambda s, tok: Token('-', tok)),
		(r'\*', lambda s, tok: Token('*', tok)),
		(r'/', lambda s, tok: Token('/', tok)),
		(r'\(', lambda s, tok: Token('(', tok)),
		(r'\)', lambda s, tok: Token(')', tok)),
		(r'=', lambda s, tok: Token('=', tok)),
		(r';', lambda s, tok: Token(';', tok)),
		(r',', lambda s, tok: Token(',', tok)),
		(r':', lambda s, tok: Token(':', tok)), 
		(r'\[', lambda s, tok: Token('[', tok)), 
		(r'\]', lambda s, tok: Token(']', tok)), 
		(r'<', lambda s, tok: Token('<', tok)), 
		(r'>', lambda s, tok: Token('>', tok)), 
		(r'.', lambda s, tok: print("Error: caracter ilegal '%s'" % tok))
	]


	def tokenizer(self, text):
		lineno = 1
		scanner = re.Scanner(self.tokens)
		results, remainder = scanner.scan(text)
		for token in results:
			if token.type is not None:  # Ignora los tokens None (espacios y comentarios)
				token.lineno = lineno
			if token.value == '\n':
				lineno += 1  # Aumenta el número de línea cuando se encuentra un salto de línea

		return iter(results)

# =======================================
# ANALISIS SINTACTICO
# =======================================
# Recursive Descent Parser.
#

class RecursiveDescentParser:
	def __init__(self):
		self.tok = None
		self.nexttok = None

	def parse(self, tokens):
		self.tokens = tokens
		self._advance()
		return self.program()

	def program(self):
		declarations = []
		while self._accept('FUN'):
			declarations.append(self.declaration_function())
		return Program(declarations)

	def declaration_function(self):
		self._expect('FUN')
		name = self.tok.value
		self._expect('IDENT')
		self._expect('(')
		arguments = self.argument_list()
		self._expect(')')
		self._expect('LOCALS')
		local_variables = self.local_variables()
		self._expect('BEGIN')
		statements = self.statements()
		self._expect('END')
		return FunctionDeclaration(name, arguments, local_variables, statements)

	def argument_list(self):
		arguments = []
		if self._accept('IDENT'):
			identifier = self.tok.value
			self._expect(':')
			data_type = self.data_type()
			arguments.append(Argument(identifier, data_type))
			while self._accept(','):
				identifier = self.tok.value
				self._expect(':')
				data_type = self.data_type()
				arguments.append(Argument(identifier, data_type))
		return arguments

	def local_variables(self):
		local_vars = []
		while self._accept('IDENT'):
			identifier = self.tok.value
			self._expect(':')
			data_type = self.data_type()
			local_vars.append(LocalVariable(identifier, data_type))
			if not self._accept(';'):
				break
		return local_vars

	def statements(self):
		stmts = []
		while self._accept('PRINT') or self._accept('IF') or self._accept('IDENT'):
			stmt = self.statement()
			stmts.append(stmt)
		return stmts

	def statement(self):
		if self._accept('PRINT'):
			return self.print_statement()
		elif self._accept('IF'):
			return self.if_statement()
		elif self._accept('IDENT'):
			return self.assignment_statement()

	def print_statement(self):
		self._expect('PRINT')
		self._expect('(')
		expr_list = self.expression_list()
		self._expect(')')
		self._expect(';')
		return PrintStatement(expr_list)

	def if_statement(self):
		self._expect('IF')
		self._expect('(')
		condition = self.expression()
		self._expect(')')
		self._expect('THEN')
		then_stmt = self.statement()
		if self._accept('ELSE'):
			else_stmt = self.statement()
		else:
			else_stmt = None
		return IfStatement(condition, then_stmt, else_stmt)

	def assignment_statement(self):
		identifier = self.tok.value
		self._expect('IDENT')
		self._expect('=')
		expression = self.expression()
		self._expect(';')
		return AssignmentStatement(identifier, expression)

	def expression(self):
		return self.expr()

	def expression_list(self):
		expressions = []
		expressions.append(self.expression())
		while self._accept(','):
			expressions.append(self.expression())
		return expressions

	def expr(self):
		term = self.term()
		while self._accept('+') or self._accept('-'):
			operator = self.tok.value
			right = self.term()
			term = BinaryExpression(operator, term, right)
		return term

	def term(self):
		factor = self.factor()
		while self._accept('*') or self._accept('/'):
			operator = self.tok.value
			right = self.factor()
			factor = BinaryExpression(operator, factor, right)
		return factor

	def factor(self):
		if self._accept('ICONST') or self._accept('RCONST') or self._accept('SCONST'):
			return self.literal()
		elif self._accept('IDENT'):
			return Identifier(self.tok.value)
		elif self._accept('('):
			self._expect('(')
			expr = self.expression()
			self._expect(')')
			return ParenthesizedExpression(expr)
		else:
			raise SyntaxError('Esperando NUMBER, RCONST, SCONST, IDENT o "("')

	def literal(self):
		if self._accept('ICONST'):
			return NumberLiteral(int(self.tok.value))
		elif self._accept('RCONST'):
			return NumberLiteral(float(self.tok.value))
		elif self._accept('SCONST'):
			return StringLiteral(self.tok.value)
		else:
			raise SyntaxError('Esperando ICONST, RCONST o SCONST')

	def data_type(self):
		if self._accept('INT') or self._accept('FLOAT'):
			return DataType(self.tok.value)
		else:
			raise SyntaxError('Esperando INT o FLOAT')

	def _advance(self):
			if self.nexttok is not None:
				while self.nexttok.type is None:
					self.nexttok = next(self.tokens, None)
					self.tok, self.nexttok = self.nexttok, next(self.tokens, None)
			else:
				self.tok = None

# class RecursiveDescentParser(object):
# 	'''
# 	Implementación de un Analizador 
# 	descendente recursivo.  Cada método 
# 	implementa una sola regla de la 
# 	gramática.

# 	Use el metodo ._accept() para probar 
# 	y aceptar el token actualmente leído.  
# 	use el metodo ._expect() para 
# 	coincidir y descartar exactamente el 
# 	token siguiente en la entrada (o 
# 	levantar un SystemError si no coincide).

# 	El atributo .tok contiene el último
# 	token aceptado. El atributo .nexttok 
# 	contiene el siguiente token leído.
# 	'''

# 	def program(self):
# 		'''
# 			program : BEGIN stmts END
# 		'''
# 		self._expect('BEGIN')
# 		stmts = self.stmts()
# 		self._expect('END')
# 		return Program(stmts)
# 	def stmts(self):
# 		'''
# 		stmts : stmt*
# 		'''
# 		stmts = []
# 		while self._accept('PRINT') or self._accept('IF') or self._accept('IDENT'):
# 			stmt = self.stmt()
# 			stmts.append(stmt)
# 		return stmts

# 	def stmt(self):
# 		'''
# 		stmt : printstmt | ifstmt | assignstmt
# 		'''
# 		if self._accept('PRINT'):
# 			return self.printstmt()
# 		elif self._accept('IF'):
# 			return self.ifstmt()
# 		elif self._accept('IDENT'):
# 			return self.assignstmt()

# 	def printstmt(self):
# 		'''
# 		printstmt : 'PRINT' exprlist ';'
# 		'''
# 		self._expect('PRINT')
# 		exprs = self.exprlist()
# 		self._expect(';')
# 		return PrintStatement(exprs)

# 	def ifstmt(self):
# 		'''
# 		ifstmt : 'IF' '(' expr ')' 'THEN' stmt ';'
# 		'''
# 		self._expect('IF')
# 		self._expect('(')
# 		condition = self.expr()
# 		self._expect(')')
# 		self._expect('THEN')
# 		stmt = self.stmt()
# 		self._expect(';')
# 		return IfStatement(condition, stmt)

# 	def assignstmt(self):
# 		'''
# 		assignstmt : IDENT '=' expr ';'
# 		'''
# 		self._expect('IDENT')
# 		name = self.tok.value
# 		self._expect('=')
# 		expr = self.expr()
# 		self._expect(';')
# 		return Assignment(SimpleLocation(name), expr)

# 	def expr(self):
# 		'''
# 		expr : term '+' expr
# 			| term '-' expr
# 			| term
# 		'''
# 		expr = self.term()
# 		while self._accept('+') or self._accept('-'):
# 			operator = self.tok.value
# 			right = self.term()
# 			expr = Binop(operator, expr, right)
# 		return expr

# 	def term(self):
# 		'''
# 		term : factor '*' term
# 			| factor '/' term
# 			| factor
# 		'''
# 		term = self.factor()
# 		while self._accept('*') or self._accept('/'):
# 			operator = self.tok.value
# 			right = self.factor()
# 			term = Binop(operator, term, right)
# 		return term

# 	def factor(self):
# 		'''
# 		factor : literal
# 			| IDENT
# 			| '(' expr ')'
# 		'''
# 		if self._accept('IDENT'):
# 			return ReadLocation(self.tok.value)
# 		elif self._accept('('):
# 			expr = self.expr()
# 			self._expect(')')
# 			return expr
# 		else:
# 			return self.literal()

# 	def literal(self):
# 		'''
# 		literal : ICONST
# 				| RCONST
# 				| SCONST
# 		'''
# 		if self._accept('NUMBER'):
# 			return Number(self.tok.value)
# 		elif self._accept('SCONST'):
# 			return String(self.tok.value)
# 		else:
# 			raise SyntaxError('Esperando NUMBER o SCONST')

# 	def exprlist(self):
# 		'''
# 		exprlist : expr (',' expr)*
# 		'''
# 		exprs = []
# 		exprs.append(self.expr())
# 		while self._accept(','):
# 			exprs.append(self.expr())
# 		return exprs


	# -----------------------------------------
	# Funciones de Utilidad.  No cambie nada
	# 
	def _advance(self):
		'Advanced the tokenizer by one symbol, skipping comments'
		if self.nexttok is not None:
			while self.nexttok.type is None:
				self.nexttok = next(self.tokens, None)
				self.tok, self.nexttok = self.nexttok, next(self.tokens, None)
		else:
			self.tok = None
		
	def _accept(self,toktype):
		'Consume the next token if it matches an expected type'
		if self.nexttok and self.nexttok.type == toktype:
			self._advance()
			return True
		else:
			return False
			
	def _expect(self,toktype):
		'Consume and discard the next token or raise SyntaxError'
		if not self._accept(toktype):
			raise SyntaxError("Expected %s" % toktype)
			
	def start(self):
		'Entry point to parsing'
		self._advance()              # Load first lookahead token
		return self.assignstmt()
		
	def parse(self,tokens):
		'Entry point to parsing'
		self.tok = None         # Last symbol consumed
		self.nexttok = None     # Next symbol tokenized
		self.tokens = tokens
		return self.start()
		


if __name__ == '__main__':
	text = '''
			fun quicksort(l:int, r:int, a:int[8192])
				i:int;
				j:int;
				x:int;
				w:int;
				tmp:int;
				done:int;
			begin
				i := l;
				j := r;
				x := a[(l+r)/2];
				done := 0;
				while done == 0 do
				begin
					while a[i] < x do
						i := i + 1;
					while x < a[j] do
						j := j - 1;
					if i <= j then
					begin
						tmp := a[i];
						a[i] := a[j];
						a[j] := tmp;
						i := i + 1;
						j := j - 1
					end;
					if i > j then
						done := 1
				end;
				if l < j then
					tmp := quicksort(l, j, a);
				if i < r then
					tmp := quicksort(i, r, a)
			end
				fun main()
					v:int[8192];
					i:int;
					n:int;
				begin
					print("Entre n: ");
					read(n);
					i := 0;
					while i < n do
					begin
						read(v[i]);
						i := i+1
					end;
					quicksort(0, n-1, v);
					i := 0;
					while i < n-1 do
					begin
						write(v[i]); print(" ");
						if 0 < v[i] - v[i+1] then
						begin
							print("Quicksort falló "); write(i); print("\n") ; return(0)
						end
						else
							i := i+1
					end;
					write(v[i]);
					print("Éxito\n")
				end
						'''
	lexer = Tokenizer()
	parser = RecursiveDescentParser()
	tokens = lexer.tokenizer(text)
	for token in tokens:
		print(token)

	