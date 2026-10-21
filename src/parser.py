from ast_nodes import *

class Parser:
    def __init__(self, tokens):
        #list of tokens
        self.tokens = tokens
        self.current = 0


    #checks whether or not the current token is the end of file token
    def at_the_end(self):
        return self.peek_current().token_type == "EOF"


    #returns the current token without moving current positoion
    def peek_current(self):
        return self.tokens[self.current]


    #return the current token and move position up 1 in list of tokens
    def move_up(self):
        if not self.at_the_end():
            self.current += 1
        return self.tokens[self.current-1]


    #helper function to look for specific token type
    def check_for_token(self, token_type):
        if self.at_the_end():
            return False
        #True if current token matches specified type
        return self.peek_current().token_type == token_type


    #Looking for matching tokens and move up if found
    def find_match(self, *types):
        #loops through list of token type arguments passed in
        for t in types:
            #if match is found, capture it and move up
            if self.check_for_token(t):
                self.move_up()
                return True

        return False


    #main function for parsing tokens into the AST
    def parse(self):
        expr = self.expression()

        if not self.at_the_end():
            raise SyntaxError(f"Unexpected token '{self.peek_current().lexeme}' on line {self.peek_current().line}")

        return expr


    
    def expression(self):
        return self.equality()


    #Parses the equality expressions that use == or != 
    def equality(self):
        #parses left side
        expr = self.comparison()

        #checks if next token is == or !=
        while self.find_match("DOUBLE_EQUAL", "EXCLAMATION_EQUAL"):
            operator = self.tokens[self.current - 1].lexeme
            right = self.comparison()
            #make node with left side, operator, right side
            expr = Binary(expr, operator, right)

        return expr


    #Parses the comparison expressions
    def comparison(self):
        #addition and subtraction take precedence, so handle that first
        expr = self.term()

        #checks if next token is <, >, <=, or >=
        while self.find_match("LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL"):
            operator = self.tokens[self.current - 1].lexeme
            right = self.term()
            #make node with left side, operator, right side
            expr = Binary(expr, operator, right)

        return expr


    #Parses additiopn and subtraction
    def term(self):
        #multiplication and division take precedence, so handle that first
        expr = self.factor()

        #checks if next token is + or -
        while self.find_match("PLUS", "MINUS"):
            operator = self.tokens[self.current - 1].lexeme
            right = self.factor()
            #make node with expr, operator, right side
            expr = Binary(expr, operator, right)

        return expr


    #parses multiplication and division
    def factor(self):
        #unary takes precedence, so handle that first
        expr = self.unary()

        #checks if next token is * or /
        while self.find_match("STAR", "SLASH"):
            operator = self.tokens[self.current - 1].lexeme
            right = self.unary()
            #make node with expr, operator, right side
            expr = Binary(expr, operator, right)

        return expr


    #parses unary like - and !
    def unary(self):
        #checks if next token is - or !
        if self.find_match("MINUS", "EXCLAMATION"):
            operator = self.tokens[self.current-1].lexeme
            right = self.unary()
            #make unary node with operator and right side
            #has to call itself to handle multiple operatorss
            return Unary(operator, right)

        return self.primary()


    #parses numbers, strings, booleans, and grouped expressions
    #also the final level of the chain of parsing
    def primary(self):
        #if number or string literal, make literal node
        if self.find_match("NUMBER", "STRING"):
            return Literal(self.tokens[self.current-1].literal)

        #if true, make literal true node
        if self.find_match("TRUE"):
            return Literal(True)

        #if false, make literal false node
        if self.find_match("FALSE"):
            return Literal(False)

        #if we find a left parentheses, parse the expression and make a grouping node
        if self.find_match("LEFT_PAREN"):
            expr = self.expression()

            #if it does not find a closing parentheses in the expression, raise error
            if not self.find_match("RIGHT_PAREN"):
                raise SyntaxError(f"Expected ')' on line {self.peek_current().line}")

            return Grouping(expr)

        #if no token types are matched, raise a SyntaxError
        raise SyntaxError(f"Unexpected token '{self.peek_current().lexeme}' on line {self.peek_current().line}")