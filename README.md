# A simple Compiler of Basic Mathematical Expressions.

Simple math Parser, Our last semaster project for Compiler course that aims to implement simple math compilation operation.

# File Structure

```
#File Name    #Objective
grammer       Get rules of mathmatical exprestions, terms, and factors
tokenes		  generate lexer& tokens by specifing thier class type or class name	 	
```

# Grammar
```
#CLASS        #BNF
Goal          <goal>
Expr          <expr>
Term          <term>
Factor        <factor>
Add           <term>+<expr>
Sub           <term>-<expr>
Mul           <factor>*<term>
Div           <factor>/<term>
Number        NUMBER
Indentifier   ID
```

## Token
```
#CLASS
Id          := "[a-zA-Z]"
Num         := "[0-9]+"
Op        := "+|-|*|/"
Plus        := "+"
Minus       := "-"
Times       := "*"
Over        := "/"
SpecialChr  := "()"
Error       := scanner error
```
## Scanner
specify the token list of a given text
```
```

# To-do
- [x] Scanner
- [ ] Ast & parser
- [ ] Interpreter
- [ ] Power