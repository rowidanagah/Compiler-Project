from grammer import *
from token import *
from Lexer import Scanner
from ast import *
from parser import Parser

scanner = Scanner()

def fun ():
    codes = ["x-2*y ","a+35-b", "10+*5"]
    inter_codes = []
    for code in codes[:]:
    	token_list = scanner.scan(code)
    	parser = pr.Parser(token_list)
    	ast = parser.parse()
    	translator = ParseTree(ast)
    	inter_code = translator.parse()
    	inter_codes.append(inter_code)
    	print(inter_code)
fun()
