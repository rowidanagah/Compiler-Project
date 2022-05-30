from grammer import *
from token import *
from re import search


class Scanner():
	def __init__(self):
		pass

	def _scan(self, word):
		if word.isdigit():
			return [Number(word)]
		if word == '+':
			return [Plus()]
		if word =='-':
			return [Minus()]
		if word =='/':
			return [Over()]
		if word =='*':
			return [Times()]
		if len(word) == 1:
			return [Id(word)]
		m = search(r'(.+)(\+|-|\*|/)(.+)', word)
		if m:
			left = m.group(1)
			op = m.group(2)
			right = m.group(3)
			return self._scan(left) + self._scan(op) + self._scan(right)
	    
		return [Error("Syntax Error")] ## otherwise raise error, egnore special chr `()` for now

	def scan(self, text):
		token_lst, lst = [], text.split()
		for word in lst:
			token_lst.extend(self._scan(word))
		return token_lst
text = ' 2 + 2 y '
scan = Scanner()
scanner = Scanner()

def fun ():
    codes = ["x-2*y ","a+35-b", "10+*5"]
    inter_codes = []
    for code in codes:
    	token_list = scanner.scan(code)
    	print(token_list)
    	
