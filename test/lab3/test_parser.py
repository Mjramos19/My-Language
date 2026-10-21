#AI Generated parser testing:
#--------------------------------------
import sys
import os
from contextlib import redirect_stdout
from io import StringIO

# Allow importing files from src/
sys.path.insert(0, os.path.abspath("src"))

from chud import run

# Test an expression and compare its output
def test_expression(source, expected):
    output = StringIO()

    with redirect_stdout(output):
        run(source)

    actual = output.getvalue().strip()

    if actual == expected:
        print(f"PASS: {source}")
    else:
        print(f"FAIL: {source}")
        print(f"Expected: {expected}")
        print(f"Actual:   {actual}")


# Test basic arithmetic
test_expression("3 + 4 * 2", "(+ 3.0 (* 4.0 2.0))")
test_expression("(3 + 4) * 2", "(* (group (+ 3.0 4.0)) 2.0)")
test_expression("10 - 3 + 2", "(+ (- 10.0 3.0) 2.0)")
test_expression("10 / 2", "(/ 10.0 2.0)")

# Equality operators
test_expression("5 == 5", "(== 5.0 5.0)")
test_expression("10 != 3", "(!= 10.0 3.0)")

# Comparison operators
test_expression("5 > 3", "(> 5.0 3.0)")
test_expression("3 < 5", "(< 3.0 5.0)")
test_expression("5 >= 5", "(>= 5.0 5.0)")
test_expression("3 <= 5", "(<= 3.0 5.0)")

# Unary operators
test_expression("-5", "(- 5.0)")
test_expression("!true", "(! true)")
test_expression("--5", "(- (- 5.0))")

# Literal types
test_expression("42", "42.0")
test_expression("3.14", "3.14")
test_expression('"hello"', '"hello"')
test_expression("true", "true")
test_expression("false", "false")

# Nested grouping and precedence
test_expression("((3 + 2) * 4)", "(group (* (group (+ 3.0 2.0)) 4.0))")
test_expression("5 > 3 + 1", "(> 5.0 (+ 3.0 1.0))")
test_expression("1 + 2 * 3 == 7", "(== (+ 1.0 (* 2.0 3.0)) 7.0)")

# Syntax error tests
test_expression(
    "3 + * 4",
    "Syntax Error: Unexpected token '*' on line 1"
)

test_expression(
    "(3 + 4",
    "Syntax Error: Expected ')' on line 1"
)

test_expression(
    "5 6",
    "Syntax Error: Unexpected token '6' on line 1"
)

test_expression(
    "3 @ + 4",
    "Syntax Error: Unexpected character '@' on line 1"
)

test_expression(
    '"hello',
    "Syntax Error: Unterminated string on line 1"
)

test_expression(
    "3 +",
    "Syntax Error: Unexpected token '' on line 1"
)

# Verify valid input still works after errors
test_expression("5 + 2", "(+ 5.0 2.0)")
#----------------------------------------------