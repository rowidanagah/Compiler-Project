"""List of grammer base.
#*** Expr   for := ADD, SUB
#*** Term   for := Div, Mul   
#*** Factor for := Id, number
"""
class Goal(object):
	pass

class Empty(object):
	pass

class Expr(Goal):
	"""Operation bettween 2 terms
	"""
	pass

class Term(Expr):
	"""Operation beteen 2 factors
	"""
	pass

class Factor(Term):
	""" Factors of a Term?
	  The numbers or variables that are multiplied to form a term are called its factors. 
	  For example, 5xy is a term with factors 5, x and y.
	"""
	pass

"""List of Expr operations
*** ADD
*** SUB
"""
class Add(Expr):
	op = "+"
	def __init(self,term: Term = None, expr: Expr =None):
		self.term = term
		self.expr = expr
	def __repr__(self):
		return 'Add %s , %s' %(self.term, self.expr)

class Sub(Expr):
	op = "-"
	def __init(self, term: Term = None, expr: Expr = None):
		self.term = term
		self.expr = expr
	def __repr__(self):
		return "Sub (%s , %s)" %(self.term, self.expr)

"""List of Term operations
*** DIV
*** MUL
"""
class Mul(Term):
	"""
	* Given expression 5x (2-y)
	**The factors of 5x (2-y) are 5, x, and (2-y).
	"""
	op = "*"
	def __init(self, factor: Factor = None, term: Term = None):
		self.term = term
		self.factor = factor
	def __repr__(self):
		return "Mul %s , %s" %(self.factor, self.term)

class Div(Term):
	op = "/"
	def __init(self, factor: Factor = None, term: Term = None):
		self.term = term
		self.factor = factor
	def __repr__(self):
		return "Div %s , %s" %(self.factor, self.term)

"""List of numarical types factors
*** Number
*** Identifier
* Both of them are factors...
"""
class Number(Factor):
	def __init__(self, val: int = None):
		self.val = val
	def __repr__(self):
		return "Specified Number is {}".foramt(self.val)
		
class Identifier(Factor):
	def __init__(self, val: str = None):
		self.id = id
	def __repr__(self):
		return "Given Identifier is {}".foramt(self.id)

"""Export the Goal of the module
"""
class Except(Goal):
  def __init__(self, msg: str = None):
    self.msg = msg
  def __str__(self):
    return self.msg
  def __repr__(self):
    return self.msg
  