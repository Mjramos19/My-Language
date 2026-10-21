#Lab 3 Report - Michael Ramos

##expression Grammer

expression → equality
equality   → comparison ( ( "==" | "!=" ) comparison )*
comparison → term ( ( ">" | ">=" | "<" | "<=" ) term )*
term       → factor ( ( "+" | "-" ) factor )*
factor     → unary ( ( "*" | "/" ) unary )*
unary      → ( "!" | "-" ) unary | primary
primary    → NUMBER | STRING | "true" | "false"
           | "(" expression ")"

This is a representation of my operator precedence. It goes from unary operations with the highest precedence to equality operations having the lowest precedence. Parentheses (grouping) basically overrides the normal rules.


##design choices

I used recurssion with separate methods for each level of operator. Operators on the same level are just handled from left to right. Unary operators use recursion, and parentheses dp as well to parse the expression inside them.

The parser also raises syntax errprs for invalid expressions, which are then caught by the main program so the interactive shell can keep running.


##Setup and Testing Instructions

To start the interactive interpreter:

python src/chud.py

To run an expression from a file:

python src/chud.py test.chud

To run the automated Lab 3 tests:

python test/lab3/test_parser.py

The automated tests compare the interpreters actual output to the expected AST output or syntax error message and display PASS or FAIL for each test.


##Test Results

All 28 automated tests passed successfully. The tests covered arithmetic, comparison and equality operators, unary operations, literals, operator precedence, nested parentheses, and syntax errors.

Examples of expected and actual outputs:

Input           Expected Output                 Actual Output

3 + 4 * 2       (+ 3.0 (* 4.0 2.0))             (+ 3.0 (* 4.0 2.0))

(3 + 4) * 2     (* (group (+ 3.0 4.0)) 2.0)     (* (group (+ 3.0 4.0)) 2.0)

5 == 5          (== 5.0 5.0)                    (== 5.0 5.0)

My own interactive testing also confirmed that the interpreter continues accepting expressions after encountering syntax errors.


##Syntax Tree

Expression: 3 + 4 * 2

    +
   / \
  3   *
     / \
    4   2

AST: (+ 3.0 (* 4.0 2.0))

In the tree you can see that multiplication takes precedence over addtion. The multiplication operation gets in own subtree that becomes the right side of the addition operation in the AST.


##Limitations

The interpreter can parse expressions but does not actually evaluate them or execute any statements. Also, the interpreter can only process one expression at a time and not multiple in a single input. It also can't support variables or asisignments yet.