from ast_nodes import *

#prints AST's
class ASTPrinter:

    #method checks which type of expression it was given and formats accordingly
    #Calls itself recursively
    def print(self, exp):
        #literal(5) - 5
        if isinstance(exp, Literal):
            #formatting output
            #-----------------------------
            if isinstance(exp.value, bool):
                return str(exp.value).lower()

            if isinstance(exp.value, str):
                return f'"{exp.value}"'
            #-----------------------------
            return str(exp.value)

        #Unary("-", literal(5)) - (- 5)
        elif isinstance(exp, Unary):
            return f"({exp.operator} {self.print(exp.right)})"

        #Binary(literal(5), "+", literal(3)) - (+ 5 3)
        elif isinstance(exp, Binary):
            return f"({exp.operator} {self.print(exp.left)} {self.print(exp.right)})"

        #Grouping(literal(5)) - (group 5)
        elif isinstance(exp, Grouping):
            return f"(group {self.print(exp.expression)})"