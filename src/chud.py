import sys
#AI CODE----------------
keywords = {
    "print" : "PRINT",
    "var" : "VAR",
    "if" : "IF",
    "else" : "ELSE",
    "while" : "WHILE",
    "true" : "TRUE",
    "false" : "FALSE"
            }
#-----------------------
#wasnt sure what keywords i should have so i generated it
class Token:

    #valid token: Token("NUMBER", "123.45", 123.45, 1)
    def __init__(self, token_type, lexeme, literal, line):
        self.token_type = token_type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line


    #string displaying token info
    def __str__(self):
        return f"{self.token_type} {self.lexeme} {self.literal} line: {self.line}"
        

class Scanner:

    def __init__(self, source):
        #source input
        self.source = source
        #empty tokens list
        self.tokens = []

        #start of current token
        self.start = 0
        #moves forwrd through the characters
        self.current = 0
        self.line = 1


    #bumps self.current to the next character
    def move_up(self):
        #grab current character to return and move up to next character
        char = self.source[self.current]
        self.current += 1

        return char


    #look ahead for matching/specific characters
    def look_ahead(self, expected_char):
        if self.current >= len(self.source):
            return False
        #if next character isn't relevant
        if self.source[self.current] != expected_char:
            return False

        #move current forward and return true when match is found
        self.current += 1
        return True


    def at_the_end(self):
        #return True if at the end of the source input
        return self.current >= len(self.source)


    #look at next (technically current) character (return it) without chanding current stored position
    def peek_current(self):
        if self.at_the_end():
            return "\0"

        #return the next (technically current) character without moving forward
        return self.source[self.current]


    #look at actual next character 1 up from current (return it) without changing current stored position
    def peek_next(self):
        if self.current + 1 >= len(self.source):
            return "\0"

        #return the next character after current without moving forward
        return self.source[self.current + 1]


    #adds group of characters (lexeme) to the self.tokens list
    def add_token(self, token_type, literal = None):

        #the set of charcters from starting position (beginning of the lexeme)
        #to current position (end of the lexeme)
        lexeme = self.source[self.start : self.current]

        #add new token to tokens list
        self.tokens.append(Token(token_type, lexeme, literal, self.line))


    #sends important characters to the add_token() function to be
    #added to the self.tokens list
    def find_token(self):
        #next character in line from move_up() function
        char = self.move_up()

        if char == "(":
            self.add_token("LEFT_PAREN")
        elif char == ")":
            self.add_token("RIGHT_PAREN")
        elif char == "{":
            self.add_token("LEFT_BRACE")
        elif char == "}":
            self.add_token("RIGHT_BRACE")
        elif char == "+":
            self.add_token("PLUS")
        elif char == "-":
            self.add_token("MINUS")
        elif char == "*":
            self.add_token("STAR")
        elif char == ";":
            self.add_token("SEMICOLON")
        elif char == ",":
            self.add_token("COMMA")

        #ignore these characters
        elif char == " " or char == "\r" or char == "\t":
            pass
        #newline - just increments scanners line number
        elif char == "\n":
            self.line += 1

        #determine if = or ==
        elif char == "=":
            if self.look_ahead("="):
                self.add_token("DOUBLE_EQUAL")
            else:
                self.add_token("EQUAL")
        elif char == "!":
            if self.look_ahead("="):
                self.add_token("EXCLAMATION_EQUAL")
            else:
                self.add_token("EXCLAMATION")
        elif char == "<":
            if self.look_ahead("="):
                self.add_token("LESS_EQUAL")
            else:
                self.add_token("LESS")
        elif char == ">":
            if self.look_ahead("="):
                self.add_token("GREATER_EQUAL")
            else:
                self.add_token("GREATER")
        elif char == "/":
            if self.look_ahead("/"):
                while self.peek_current() != "\n" and not self.at_the_end():
                    self.move_up()
            else:
                self.add_token("SLASH")
        
        #if character is a digit
        elif char.isdigit():
            self.build_number()

        #if character is parentheses (indicating a string)
        elif char == '"':
            self.build_string()

        #if the character is alphabetical or underscore, it could be an identifier
        elif char.isalpha() or char == "_":
            self.build_identifier()


        #if all ifs pass and char is not of any significance, print an unexpected error 
        else:
            print(f"Error on line {self.line}: Unexpected character '{char}'")


    #figuring out the format of and storing a number from source input as token
    def build_number(self):

        while self.peek_current().isdigit():
            self.move_up()

        #if next character is a . and the characters after that are more digits
        if self.peek_current() == "." and self.peek_next().isdigit():
            self.move_up()

            #move up to grab all remaining digits
            while self.peek_current().isdigit():
                self.move_up()

        #number token is set of characters from start to current position (end of number)
        #convert string number to float before adding it to tokens (literal value)
        number = float(self.source[self.start : self.current])

        self.add_token("NUMBER", number)


     #figuring out the format of and storing a string from source input as token   
    def build_string(self):

        #while still searching for closing parentheses and not at the end of lexeme
        while self.peek_current() != '"' and not self.at_the_end():
            #if i hit a newline character, increment current line to keep going
            if self.peek_current() == "\n":
                self.line += 1

            self.move_up()

        #if the end of the source is reached and still no closing parantheses, error: unterminated string
        if self.at_the_end():
            print(f"Error on line {self.line}: Unterminated string.")
            return

        self.move_up()

        #start + 1 and current - 1 to grab everything besides parentheses
        val = self.source[self.start + 1 : self.current - 1]
        self.add_token("STRING", val)



    def build_identifier(self):

        #move up while next character is alpha numeric or an underscore
        while self.peek_current().isalnum() or self.peek_current == "_":
            self.move_up()

        #grab lexeme
        val = self.source[self.start : self.current]

        #if the lexeme is a keyword, set the token type to the corresponding keyword type
        if val in keywords:
            token_type = keywords[val]
        #if completed lexeme is not a keyword, set it as an identifier
        else:
            token_type = "IDENTIFIER"

        self.add_token(token_type)


    #main driver fucntion for scanning all tokens in source
    def find_tokens(self):

        while self.current < len(self.source):
            self.start = self.current
            self.find_token()

        #Adds EOF token to the end of the tokens list after loop ends
        self.tokens.append(Token("EOF", "", None, self.line))

        return self.tokens


identifier_pattern = r"[A-Za-z_][A-Za-z0-9_]*"
string_pattern = r'"[^"]*"'
number_pattern = r"\d+(\.\d+)?"



def run(source):
    #make scanner with source input
    scanner = Scanner(source)
    #find all tokens in source input using scanner
    #tokens = list of tokens
    tokens = scanner.find_tokens()

    #loop through/print all tokens
    for token in tokens:
        print(token)


def run_file(filename):
    with open(filename, 'r') as f:
        source = f.read()

    run(source)

def run_the_repl():
    print("----CHUD Interactive Shell----")
    try:
        while True:
            source = input("> ")
            run(source)
    except KeyboardInterrupt:
        print()

def main():
    if len(sys.argv) > 2:
        print("Correct Usage: python src/chud.py [script]")
    elif len(sys.argv) == 2:
        run_file(sys.argv[1])
    else:
        run_the_repl()

main()