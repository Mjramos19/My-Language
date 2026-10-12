import sys
import os
sys.path.insert(0, os.path.abspath("src"))
from ast_nodes import Literal, Binary, Unary, Grouping
from ast_printer import ASTPrinter


#AI Generated AST TESTS
#------------------------------
printer = ASTPrinter()

expression1 = Binary(
    Unary("-", Literal(123)),
    "*",
    Grouping(Literal(45.67))
)

expression2 = Binary(
    Literal(10),
    "+",
    Literal(20)
)

expression3 = Binary(
    Literal("hello"),
    "==",
    Literal("world")
)

expression4 = Unary("!", Literal(True))

expression5 = Binary(
    Binary(Literal(20), "-", Literal(5)),
    "/",
    Literal(3)
)

expression6 = Binary(Literal(10), ">", Literal(5))
expression7 = Binary(Literal(10), ">=", Literal(10))
expression8 = Binary(Literal(3), "<", Literal(8))
expression9 = Binary(Literal(3), "<=", Literal(3))

expression10 = Binary(Literal(5), "!=", Literal(10))

print("Test 1:", printer.print(expression1))
print("Test 2:", printer.print(expression2))
print("Test 3:", printer.print(expression3))
print("Test 4:", printer.print(expression4))
print("Test 5:", printer.print(expression5))
print("Test 6:", printer.print(expression6))
print("Test 7:", printer.print(expression7))
print("Test 8:", printer.print(expression8))
print("Test 9:", printer.print(expression9))
print("Test 10:", printer.print(expression10))
#-------------------------------s