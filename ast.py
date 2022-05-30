from grammer import *
from token import *

class ParseTree(object):
  def __init__(self, ast):
    self.ast   = ast
    self.stack = []
    self.ans = 0

  def _parse(self, tree):
  	if isinstance(tree, Number):
  		self.stack.append(tree.val)
  		return str(tree.val)

  	if isinstance(tree, Identifier):
  		#self.stack.append(tree.value)
  		return str(tree.id)

  	if isinstance(tree, Term):
  		return tree.op + self._parse(tree.factor) + self._parse(tree.term)

  	if isinstance(tree, Expr):
  		return tree.op + self._parse(tree.term) + self._parse(tree.expr)
  	
  	if isinstance(tree, Except):
  		return 'incorrect syntax'
  	if isinstance(tree, Empty):
  		return ''

  def parse(self) -> str:
    return self._parse(self.ast)

