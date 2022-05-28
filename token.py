"""List of Token Class Mathmatical Names and thier proper Values...
#*** Id          := "[a-zA-Z]"
#*** Num         := "[0-9]+"
#*** Op          := "+|-|*|/"
#*** Plus        := "+"
#*** Minus       := "-"
#*** Times       := "*"
#*** Over        := "/"
#*** SpecialChr  := "()="
#*** Error       := scanner error

> Bases will be (name as well as operation)
	*** name for := Id, Number, SpecialChr
	*** op for   := otherwise like minus, over, times, div...
"""
class name(object):
	pass

class op(name):
	pass

class Id(name):
	def __init__(self,val):
		self.val = val
	def __repr__(self):
		return "<Id, %s>" %(self.val)

class Number(name):
	def __init__(self,val):
		self.val = val
	def __repr__(self):
		return "<Id, %s>" %(self.val)

class Plus(op):
	def __init__(self,val = '+'):
		self.val = val
	def __repr__(self):
		return "<%s>" %(self.val)

class Minus(op):
	def __init__(self,val = '-'):
		self.val = val
	def __repr__(self):
		return "<%s>" %(self.val)

class Times(op):
	def __init__(self,val = '*'):
		self.val = val
	def __repr__(self):
		return "<%s>" %(self.val)

class Over(op):
	def __init__(self,val = '/'):
		self.val = val
	def __repr__(self):
		return "< %s >" %(self.val)

class SpecialChr(name):
	def __init__(self,val):
		self.val = val
	def __repr__(self):
		return "<%s>" %(self.val)

class Error(object):
  def __init__(self, type = "Lexical"):
    self.type = type
  def __repr__(self):
    return "%s Error" %(self.type)