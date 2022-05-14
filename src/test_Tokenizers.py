import unittest
import sys

sys.path.insert(0,'src')
from Tokenizer import run
from Tokenizer import *

default = '<stdin>'
# # CURRENTLY WORKING ON IMPORTING FROM ANOTHER FILE
# #
# #  /../JAVPIE folder
# #  |    |src folder
# #  |         |-----. py - target
# #  |
# #  |----|Test folder
# #  |         |-----./test_Tokenizer.py
# #
# #  Method works in Visual Studio Code, as this code was written using VSCode
# #  SOLVED, run test file with Coding Environemnt First
# #  Then, you can type: python .\test_Tokenizer.py
# #  Into the terminal

class TestTokens(unittest.TestCase):
    def test_additions(self):
        test_input = '1+1'
        testing, error = run(default, test_input)
        expected_text = '2'
        self.assertEqual(str(testing), expected_text)
        
class TestTokens2(unittest.TestCase):
    def test_NumParan(self):
        test_input = '(3)'
        testing, error = run(default, test_input)
        expected_text = '3'
        self.assertEqual(str(testing), expected_text)


class TestTokens3(unittest.TestCase):
    def test_NumCBrace(self):
        test_input = '\{5\}'
        testing, error = run(default, test_input)
        expected_text = "Illegal Character: '\\'"
        self.assertEqual(error.as_string(), expected_text)

class TestTokens4(unittest.TestCase):
    def test_Division(self):
        test_input = '10/2'
        testing, error = run(default, test_input)
        expected_text = '5'
        self.assertEqual(str(testing), expected_text)

class TestTokens5(unittest.TestCase):
    def test_Multiply(self):
        test_input = '10 * 2'
        testing = run(default, test_input)
        expected_text = '20'
        self.assertEqual(str(testing), expected_text)

class TestTokens6(unittest.TestCase):
    def test_Operands(self):
        test_input = '+-'
        testing = run(default, test_input)
        expected_text = '((PLUS, MINUS) None)'
        self.assertEqual(str(testing), expected_text)
        
class TestTokens7(unittest.TestCase):
    def test_Decimal(self):
        test_input = '2.5'
        testing = run(default, test_input)
        expected_text = '2.5'
        self.assertEqual(str(testing), expected_text)

class TestTokens_Error(unittest.TestCase):
    def test_String(self):
        test_input = 'string'
        testing = run(default, test_input)
        expected_text = '(None), <IllegalCharError object at 0x000002405638BFA0>)'
        self.assertEqual(str(testing), expected_text)
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
if __name__  == '__main__':
    unittest.main()



    