#lab 1: Scanning

#Design

My language is called CHUD, which is primarily based on Lox and its design process. For lab 1, I implemented the scanning portion of my language. The scanner basically takes source code from either a file or terminal input and stores it as a list of tokens.

My language currently supports identifiers, keywords, numbers, strings, operators, punctuation, comments, and can handle whitescape.

Current keywords:
    'var'
    'print'
    'if'
    'else'
    'while'
    'true'
    'false'

'//' for single line commenting

The design was heavily based on lox. The scanner reads the source code one character at a time and builds tokens based on what it finds. The set of keywords and token types are pretty small currently relative to Lox because the scanner is the only portion of my language currently implemented, but I am planning to add more.


#Regex

#identifiers

Regex:
'[A-Za-z_][A-Za-z0-9_]*'

#Number literals

Regex:
'\d+(\.\d+)?'

A number can hold one or more digits. It can also have a decimal point followed by more digits or none.

#String literals

Regex:
'"[^"]*"'

A string has to begin and end with double quotes. The scanner then stores the characters in between the quotation marks.


#Setup

CHUD is implemented in python and requires no external dependencies.

#Source file mode

From the directory of the repo, run 'python src/chud.py {filename}

Example: 'python src/chud.py test/lab1/firstprogram.chud

The scanner then reads the file and prints the tokens and their info

#interactive mode

run 'python src/chud.py'

This opens up the CHUD interactive shell where source code can be typed directly into the terminal. The shell also can keep taking inputs even after errors are made.


#Error handling

The scanner can currently produce error messages for unexpected characters and unterminated strings. The messages include error types and the lines that they were made on. Error messages also do not stop the scanner.


#Testing

#Token Types
Tests punctuation, operators. keywords, and identifiers (all current token types)

Expected:
each of those token types should have the correct token type and info. There should also be a end of file token at the end.

Actual:
The scanner correctly recognized all token types and ended with an EOF token.

#literals
Tests integers, decimals, strings, string with numbers, and empty strings.

expected:
Numbers should have NUMBER tokens stored with their literal values. Strings should have a STRING token stored with their literal values.

Actual:
Each literal was stored with its proper corresponding token type.

#comments
Tests comments and comments placed after the source code.

Expected:
All text after '//' should be ignored until the next line.

Actual:
All text got ignored until next line of valid source code was reached.

#Unexpected Characters
Tests lexical errors caused by using unknown characters in the source code. 

Expected: The scanner should report the error, where it was found, what ws found, and should continue scanning the rest of the code.

Actual: It works as expected. However, the order of output is a little out of whack and the error messages print before the token information of the actual working source code. So, the formatting of output is a little confusing but the functionality is all there.

#unterminated Strings
Tests the detection of a string that reaches the end of the source code without finding a closing quote.

Expected:
The scanner should produce an unterminated string error message with the line number that it started on.

Actual:
It produces an error message and all proper info. But again, the order is off in the terminal as it prints error messages before all valid tokens.


#Test program
Tests multiple scanner features together in the form of a simple program

#expected:
The entire program should be converted into the correct tokens with no errors, and ending with a EOF token.

Actual:
The program was converted correctly and ended with an EOF token.


#Known limitations

CHUD really only has a working scanner currently. Meaning that it can't actually execute the source code, it simply reports on it. The scanner also only currently supports single line comments and not block comments.

All required tests passed but again, the order of output is thrown off slightly by the error messages. All information is correct and the tests are still passed. But, it is a visual error that I need to correct.
