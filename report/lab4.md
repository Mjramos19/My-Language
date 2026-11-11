#Lab 4: Statements

##Overview

In this lab, I extended my Python interpreter to support expression statements, print statements, and panic-mode syntax error recovery.

I also completed the expression evaluator from the previous project so that the interpreter could evaluate expressions instead of only printing their AST representations.


##Implementation


##Statements

I added two new AST node classes, ExpressionStmt and PrintStmt, to represent statements and print them.

I modified the parser to process multiple statements separated by semicolons. The interpreter evaluates expression statements without displaying their results, while print statements evaluate expressions and display the results.

I also added support for the nil keyword.


##Error Recovery

I implemented a synchronize() method in the parser to handle/recover from syntax errors.

When the parser finds an invalid statement, it reports the error and skips tokens until it syncs up at a certain point. An example would be a semicolon or the beginning of another print statement.

This allows the parser to continue processing valid statements after an error.


##Testing

Test Case 1: Syntax Error Recovery

Input:
"one"
true;
print 2 +

Output:
Syntax Error: Expected ';' after expression on line 2
Syntax Error: Unexpected token '' on line 3

Test Case 2: Statements

Input:
4 + 2;
print "one";
print true;
print 1 + 2;
print nil;

Output:
one
true
3
nil

The expression statement 4 + 2; evaluates without printing a result. Each print statement displays its evaluated value.


##Setup and Execution

The interpreter is implemented in Python and does not require any libraries.

From the repos root directory, run:
python src/chud.py test/lab4/test1.txt
python src/chud.py test/lab4/test2.txt

The interpreter can also be started in interactive mode using:
python src/chud.py


##Conclusion

This lab expanded the interpreter to support multiple statements, evaluate and print expressions, and handling syntax errors without stopping the entire parsing process.