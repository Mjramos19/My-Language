#All AST node classes

#stores a literal value
class Literal:
    def __init__(self, value):
        self.value = value

#stores an operator and an expression
class Unary:
    def __init__(self, operator, right):
        self.operator = operator
        self.right = right

#stores an operator and two expressions
class Binary:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

#stores an expression grouped inside parentheses
class Grouping:
    def __init__(self, expression):
        self.expression = expression