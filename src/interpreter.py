
from ast_nodes import *
class Interpreter:

    #determines what type of expression we are evaluating
    def evaluate(self, expr):

        #literal values can be returned directly
        if isinstance(expr, Literal):
            return expr.value

        #eval the expression inside parentheses
        elif isinstance(expr, Grouping):
            return self.evaluate(expr.expression)

        #eval unary expressions
        elif isinstance(expr, Unary):
            right = self.evaluate(expr.right)

            if expr.operator == "-":
                return -right
            elif expr.operator == "!":
                return not self.is_truthy(right)

        #eval binary expressions
        elif isinstance(expr, Binary):
            left = self.evaluate(expr.left)
            right = self.evaluate(expr.right)

            if expr.operator == "+":
                return left + right

            elif expr.operator == "-":
                return left - right

            elif expr.operator == "*":
                return left * right

            elif expr.operator == "/":
                return left / right

            elif expr.operator == ">":
                return left > right

            elif expr.operator == ">=":
                return left >= right

            elif expr.operator == "<":
                return left < right

            elif expr.operator == "<=":
                return left <= right

            elif expr.operator == "==":
                return left == right

            elif expr.operator == "!=":
                return left != right

        raise RuntimeError("Unknown expression")


    #determines whether a value is true or false
    def is_truthy(self, value):
        if value is None:
            return False

        if isinstance(value, bool):
            return value

        return True

    
    #calls execute function on a list of statements
    def interpret(self, statements):
        for statement in statements:
            self.execute(statement)


    #executes an individual statement
    def execute(self, statement):

        #expression statement
        if isinstance(statement, ExpressionStmt):
            self.evaluate(statement.expression)

        #print statement
        elif isinstance(statement, PrintStmt):
            value = self.evaluate(statement.expression)
            print(self.stringify(value))


    #converts values to readable output
    def stringify(self, value):

        if value is None:
            return "nil"

        if isinstance(value, bool):
            return str(value).lower()

        if isinstance(value, float) and value.is_integer():
            return str(int(value))

        return str(value)
