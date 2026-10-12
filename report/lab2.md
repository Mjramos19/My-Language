#Lab 2 Report - CHUD language - Michael Ramos

##Expression Grammar

##AI Generated clear representation of my expression grammar
##----------------------------------------------------------
expression → equality ;
equality → comparison ( ( "==" | "!=" ) comparison )* ;
comparison → term ( ( ">" | ">=" | "<" | "<=" ) term )* ;
term → factor ( ( "+" | "-" ) factor )* ;
factor → unary ( ( "*" | "/" ) unary )* ;
unary → ( "!" | "-" ) unary | primary ;
primary → NUMBER | STRING | "true" | "false" | "(" expression ")" ;
#------------------------------------------------------------


##Design choices

My languages expression grammar is heavily based on Lox's.

CHUD uses the operators  (+, -, *, /), comparison operators (>, <, >=, <=), and equality operators (==, !=).

It also uses - and ! as unary operators

My literal types include numbers, strings, and boolean values (true and false)

Grouping is done using parentheses.

My languages grammar also prioritises multiplication and division before addition and subtraction in an expression.

My set of expressions currently is not as in-depth as Lox's. For example, I'm still missing logical operators like "and" and "or".


##Implementation

The AST is implemented using four classes in ast_nodes.py:

Literal: stores a literal vlaue
Unary: stores an operator and an expression
Binary: stores an operator and two expressions surrounding it
Grouping: stores an expression grouped inside of parentheses

The AST printer is implemented in ast_printer.py and uses recursion to print the nested expressions and parentheses to show the structure of every AST.


##Test setup

To run the tests, enter:

python test/lab2/test_ast.py

The tests make AST's directly rather than using the scanner.


##Testing

test1: Nested expressions, unary minus, multiplication, grouping - Expected: (* (- 123) (group 45.67))'
test2: Addition - Expected: '(+ 10 20)'
test3: String equality - Expected: '(== "hello" "world")'
test4: Boolean and unary NOT - Expected: '(! true)'
test5: Subtraction and division - Expected: '(/ (- 20 5) 3)'
test6: Greater than - Expected: '(> 10 5)'
test7: Greater than or equal - Expected: '(>= 10 10)'
test8: Less than - Expected: '(< 3 8)'
test9: Less than or equal - Expected: '(<= 3 3)'
test10: Not equal - Expected: '(!= 5 10)'

###results

All 10 tests matched expected outputs.

The tests use all AST classes, all of my languages literal types, every operator in my grammar, and even nested expressions.

###actual terminal output:
###-------------------------------
Test 1: (* (- 123) (group 45.67))
Test 2: (+ 10 20)
Test 3: (== "hello" "world")
Test 4: (! true)
Test 5: (/ (- 20 5) 3)
Test 6: (> 10 5)
Test 7: (>= 10 10)
Test 8: (< 3 8)
Test 9: (<= 3 3)
Test 10: (!= 5 10)
###-------------------------------