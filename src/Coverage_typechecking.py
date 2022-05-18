# 
#
#  THIS FILE IS FOR CODE COVERAGE, THIS IS
#  NOT THE TEST FILE
# 
#
import unittest
import sys

sys.path.insert(0,'src')
from Tokenizer import *

default = '<stdin>'

class testIntType(unittest.TestCase):
    def test_Int(self):
        test_input = '1'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([INT:1, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testAddNoSpaces(unittest.TestCase):
    def test_add(self):
        test_input = '1+9'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([INT:1, PLUS, INT:9, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testIntType(unittest.TestCase):
    def test_String(self):
        test_input = ''
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([INT:1, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testIntType(unittest.TestCase):
    def test_Int(self):
        test_input = '1'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([INT:1, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testIntType(unittest.TestCase):
    def test_Int(self):
        test_input = '1'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([INT:1, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testEmptyInput(unittest.TestCase):
    def test_String(self):
        test_input = ''
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testIdentifierType(unittest.TestCase):
    def test_Identifier(self):
        test_input = 'VAR hi = 1'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([KEYWORD:VAR, IDENTIFIER:hi, EQ, INT:1, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testLetterStringType(unittest.TestCase):
    def test_Int(self):
        test_input = "h"
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([IDENTIFIER:h, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testFUNType(unittest.TestCase):
    def test_Int(self):
        test_input = 'FUN a (a,b) -> a + b'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([KEYWORD:FUN, IDENTIFIER:a, LPAREN, IDENTIFIER:a, COMMA, IDENTIFIER:b, RPAREN, ARROW, IDENTIFIER:a, PLUS, IDENTIFIER:b, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testPlusSymbol(unittest.TestCase):
    def test_Int(self):
        test_input = '+'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([PLUS, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testMinusSymbol(unittest.TestCase):
    def test_Int(self):
        test_input = '-'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([MINUS, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testMultSymbol(unittest.TestCase):
    def test_Int(self):
        test_input = '*'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([MUL, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testDivideSymbol(unittest.TestCase):
    def test_Int(self):
        test_input = '/'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([DIV, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testLParen(unittest.TestCase):
    def test_Int(self):
        test_input = '('
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([LPAREN, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testRParen(unittest.TestCase):
    def test_Int(self):
        test_input = ')'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([RPAREN, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testPowSymbol(unittest.TestCase):
    def test_Int(self):
        test_input = '^'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([POW, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testAND(unittest.TestCase):
    def test_Int(self):
        test_input = 'AND'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([KEYWORD:AND, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testVAR(unittest.TestCase):
    def test_Int(self):
        test_input = 'VAR'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([KEYWORD:VAR, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testOR(unittest.TestCase):
    def test_Int(self):
        test_input = 'OR'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([KEYWORD:OR, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testIF(unittest.TestCase):
    def test_Int(self):
        test_input = 'IF'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([KEYWORD:IF, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testELSE(unittest.TestCase):
    def test_Int(self):
        test_input = 'ELSE'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([KEYWORD:ELSE, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testFOR(unittest.TestCase):
    def test_Int(self):
        test_input = 'FOR'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([KEYWORD:FOR, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testTO(unittest.TestCase):
    def test_Int(self):
        test_input = 'TO'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([KEYWORD:TO, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testSTEP(unittest.TestCase):
    def test_Int(self):
        test_input = 'STEP'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([KEYWORD:STEP, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testWHILE(unittest.TestCase):
    def test_Int(self):
        test_input = 'WHILE'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([KEYWORD:WHILE, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testTHEN(unittest.TestCase):
    def test_Int(self):
        test_input = 'THEN'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([KEYWORD:THEN, EOF], None)'
        self.assertEqual(str(testing), expected_res)

class testFUN(unittest.TestCase):
    def test_Int(self):
        test_input = 'FUN'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([KEYWORD:FUN, EOF], None)'
        self.assertEqual(str(testing), expected_res)


if __name__  == '__main__':
    unittest.main()
