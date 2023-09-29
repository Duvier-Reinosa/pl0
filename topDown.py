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
		(r'\n', 							lambda s, tok: Token('NEWLINE', tok)),
		(r'\s+', 							None),
		(r'//.*', 							None),
		(r'"[^"]*"', 						lambda s, tok: Token('SCONST', tok)),
		(r'\d+(\.\d+)?(E[-+]?\d+)?', 		lambda s, tok: Token('RCONST', tok)),
		(r'\d+', 							lambda s, tok: Token('ICONST', tok)),
		(r'[Bb][Ee][Gg][Ii][Nn]', 			lambda s, tok: Token('BEGIN', tok)),
		(r'[Ee][Nn][Dd]', 					lambda s, tok: Token('END', tok)),
		(r'[Ii][Ff]', 						lambda s, tok: Token('IF', tok)),
		(r'[wW][hH][iI][lL][eE]', 			lambda s, tok: Token('WHILE', tok)),
		(r'[dD][oO]', 						lambda s, tok: Token('DO', tok)),
		(r'[sS][kK][iI][pP]', 				lambda s, tok: Token('SKIP', tok)),
		(r'[bB][rR][eE][aA][kK]', 			lambda s, tok: Token('BREAK', tok)),
		(r'[tT][hH][eE][nN]', 				lambda s, tok: Token('THEN', tok)),
		(r'[wW][rR][iI][tT][eE]',	 		lambda s,tok:Token('WRITE',tok)),
		(r'[rR][eE][aA][dD]',		 		lambda s,tok:Token('READ ',tok)),
		(r'[fF][uU][nN]',    		 		lambda s,tok:Token(' FUN ',tok)),
		(r'<=',          		     		lambda s,tok:Token(' GT  ',tok)),
		(r'>=',             		 		lambda s,tok:Token(' GE  ',tok)),
		(r'==',             		 		lambda s,tok:Token(' EQ  ',tok)),
		(r'!=',             		 		lambda s,tok:Token(' NE  ',tok)),
		(r'<',              		 		lambda s,tok:Token(' LT  ',tok)),
		(r'>',           		     		lambda s,tok:Token(' LE  ',tok)),
		(r'[aA][nN][dD]',            		lambda s,tok:Token(' AND',tok)),
		(r'[oR][rR]',                		lambda s,tok:Token(' OR ',tok)),
		(r'[nN][oO][tT]',            		lambda s,tok:Token(' NOT ',tok)),
		(r'[a-zA-Z_]\w*', 					lambda s, tok: Token('IDENT', tok)),
		(r'\+', 							lambda s, tok: Token('+', tok)),
		(r'-', 								lambda s, tok: Token('-', tok)),
		(r'\*', 							lambda s, tok: Token('*', tok)),
		(r'/', 								lambda s, tok: Token('/', tok)),
		(r'\(', 							lambda s, tok: Token('(', tok)),
		(r'\)', 							lambda s, tok: Token(')', tok)),
		(r'=', 								lambda s, tok: Token('=', tok)),
		(r';', 								lambda s, tok: Token(';', tok)),
		(r',', 								lambda s, tok: Token(',', tok)),
		(r':', 								lambda s, tok: Token(':', tok)), 
		(r'\[', 							lambda s, tok: Token('[', tok)), 
		(r'\]', 							lambda s, tok: Token(']', tok)), 
		(r'.', 								lambda s, tok: print("Error: caracter ilegal '%s'" % tok))
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
	# parser = RecursiveDescentParser()
	tokens = lexer.tokenizer(text)
	for token in tokens:
		print(token)

	