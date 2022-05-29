from grammer import *
from token import *

class Scanner():
	def __init__(self):
		pass

	def _scan(self, word):
		if word.isdigit():
			return Number(word)
		if word == '+':
			return Plus('+')
		if word =='-':
			return Minus('-')
		if word =='-':
			return Minus('-')
		if word =='/':
			return Over('/')
		if word =='*':
			return Times('*')
		if len(word) == 1:
			return Id(word)

		return [Error("Syntax Error")] ## otherwise raise error, egnore special chr `()` for now

	def scan(self, text):
		token_lst, lst = [], text.split()
		for word in lst:
			token_lst.append(self._scan(word))
		return token_lst

text = ' 2 + 2 y '
scan = Scanner()
print(scan.scan(text)) # op [<Id, 2>, <+>, <Id, 2>, <Id, y>]
