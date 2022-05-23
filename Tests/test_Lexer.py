import unittest
import sys

sys.path.insert(0,'src')
##from Tokenizer import run
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
# #  SOLVED, run test file with Coding Environemnt
# #  

class TestTokens(unittest.TestCase):
    def test_additions(self):
        test_input = '1+1'
        testing = Lexer(default, test_input).make_tokens()
        expected_text = '([INT:1, PLUS, INT:1, EOF], None)'
        self.assertEqual(str(testing), expected_text)
        
class TestTokens2(unittest.TestCase):
    def test_NumParan(self):
        test_input = '(3)'
        testing= Lexer(default, test_input).make_tokens()
        expected_text = '([LPAREN, INT:3, RPAREN, EOF], None)'
        self.assertEqual(str(testing), expected_text)


class TestTokens4(unittest.TestCase):
    def test_Division(self):
        test_input = '10/2'
        testing= Lexer(default, test_input).make_tokens()
        expected_text = '([INT:10, DIV, INT:2, EOF], None)'
        self.assertEqual(str(testing), expected_text)

class TestTokens5(unittest.TestCase):
    def test_Multiply(self):
        test_input = '10 * 2'
        testing = Lexer(default, test_input).make_tokens()
        expected_text = '([INT:10, MUL, INT:2, EOF], None)'
        self.assertEqual(str(testing), expected_text)

class TestTokens6(unittest.TestCase):
    def test_Operands(self):
        test_input = '+-'
        testing = Lexer(default, test_input).make_tokens()
        expected_text = '([PLUS, MINUS, EOF], None)'
        self.assertEqual(str(testing), expected_text)
        
class TestTokens7(unittest.TestCase):
    def test_Decimal(self):
        test_input = '2.5'
        testing = Lexer(default, test_input).make_tokens()
        expected_text = '([FLOAT:2.5, EOF], None)'
        self.assertEqual(str(testing), expected_text)

class TestTokens_String(unittest.TestCase):
    def test_String(self):
        test_input = '"string"'
        testing = Lexer(default, test_input).make_tokens()
        expected_text = '([STRING:string, EOF], None)'
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
        
class testFUN(unittest.TestCase):
    def test_Int(self):
        test_input = 'FUN'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([KEYWORD:FUN, EOF], None)'
        self.assertEqual(str(testing), expected_res)       
        
class TestTokensError(unittest.TestCase):
    def test_NumCBrace(self):
        test_input = '\{5\}'
        test=False
        testing, error = Lexer(default, test_input).make_tokens()
        if error != None: test = True
        message = 'Test: Illegal Character: \ '
        self.assertTrue(test, message)
        
class TestTokensError2(unittest.TestCase):
    def test_NumCBrace(self):
        test_input = '`'
        test=False
        testing, error = Lexer(default, test_input).make_tokens()
        if error != None: test = True
        message = 'Test: Illegal Character: ` '
        self.assertTrue(test, message)
        
class TestTokensError3(unittest.TestCase):
    def test_NumCBrace(self):
        test_input = ' '
        test=False
        testing, error = Lexer(default, test_input).make_tokens()
        if error != None: test = True
        message = 'Test: Illegal Character: space_key'
        self.assertTrue(test, message)
        
class TestTokensError4(unittest.TestCase):
    def test_NumCBrace(self):
        test_input = '@'
        test=False
        testing, error = Lexer(default, test_input).make_tokens()
        if error != None: test = True
        message = 'Test: Illegal Character: @ '
        self.assertTrue(test, message)
        
class TestTokensError5(unittest.TestCase):
    def test_NumCBrace(self):
        test_input = '#'
        test=False
        testing, error = Lexer(default, test_input).make_tokens()
        if error != None: test = True
        message = 'Test: Illegal Character: # '
        self.assertTrue(test, message)
        
class TestTokensError6(unittest.TestCase):
    def test_NumCBrace(self):
        test_input = '$'
        test=False
        testing, error = Lexer(default, test_input).make_tokens()
        if error != None: test = True
        message = 'Test: Illegal Character: $ '
        self.assertTrue(test, message)
        
class TestTokensError7(unittest.TestCase):
    def test_NumCBrace(self):
        test_input = '%'
        test=False
        testing, error = Lexer(default, test_input).make_tokens()
        if error != None: test = True
        message = 'Test: Illegal Character: % '
        self.assertTrue(test, message)
        
class TestTokensError8(unittest.TestCase):
    def test_NumCBrace(self):
        test_input = '~'
        test=False
        testing, error = Lexer(default, test_input).make_tokens()
        if error != None: test = True
        message = 'Test: Illegal Character: ~ '
        self.assertTrue(test, message)
        
class TestTokensError9(unittest.TestCase):
    def test_NumCBrace(self):
        test_input = ';'
        test=False
        testing, error = Lexer(default, test_input).make_tokens()
        if error != None: test = True
        message = 'Test: Illegal Character: ; '
        self.assertTrue(test, message)        
        
        
class TestTokensError4(unittest.TestCase):
    def test_NumCBrace(self):
        test_input = ':'
        test=False
        testing, error = Lexer(default, test_input).make_tokens()
        if error != None: test = True
        message = 'Test: Illegal Character: : '
        self.assertTrue(test, message)
        
class TestTokensError4(unittest.TestCase):
    def test_NumCBrace(self):
        test_input = ','
        test=False
        testing, error = Lexer(default, test_input).make_tokens()
        if error != None: test = True
        message = 'Test: Illegal Character: , '
        self.assertTrue(test, message)
        
class TestTokensError4(unittest.TestCase):
    def test_NumCBrace(self):
        test_input = '.'
        test=False
        testing, error = Lexer(default, test_input).make_tokens()
        if error != None: test = True
        message = 'Test: Illegal Character: . '
        self.assertTrue(test, message)
        
if __name__  == '__main__':
    unittest.main()



    