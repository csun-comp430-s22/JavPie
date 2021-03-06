import unittest
import sys

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
sys.path.insert(0,'src')
from JavPie import *

default = '<stdin>'

class testIntType(unittest.TestCase):
    def test_Int(self):
        test_input = '1'
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        expected_res = 'INT:1'
        self.assertEqual(str(parsetest.node), expected_res)
        
class testFloatType(unittest.TestCase):
    def test_Int(self):
        test_input = '1.1'
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        expected_res = 'FLOAT:1.1'
        self.assertEqual(str(parsetest.node), expected_res)
        
class testAddition(unittest.TestCase):
    def test_Int(self):
        test_input = '1+2'
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        expected_res = '(INT:1, PLUS, INT:2)'
        self.assertEqual(str(parsetest.node), expected_res)

class testMult(unittest.TestCase):
    def test_Int(self):
        test_input = '10*22'
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        expected_res = '(INT:10, MUL, INT:22)'
        self.assertEqual(str(parsetest.node), expected_res)
        
class testMinus(unittest.TestCase):
    def test_Int(self):
        test_input = '30 - 20'
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        expected_res = '(INT:30, MINUS, INT:20)'
        self.assertEqual(str(parsetest.node), expected_res)
        
class testDivide(unittest.TestCase):
    def test_Int(self):
        test_input = '10/5'
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        expected_res = '(INT:10, DIV, INT:5)'
        self.assertEqual(str(parsetest.node), expected_res)
        
class testMultParen(unittest.TestCase):
    def test_Int(self):
        test_input = '2*(3*2)'
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        expected_res = '(INT:2, MUL, (INT:3, MUL, INT:2))'
        self.assertEqual(str(parsetest.node), expected_res)
        
class testAdditionParen(unittest.TestCase):
    def test_Int(self):
        test_input = '(2-1)+2'
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        expected_res = '((INT:2, MINUS, INT:1), PLUS, INT:2)'
        self.assertEqual(str(parsetest.node), expected_res)
        
class testPower(unittest.TestCase):
    def test_Int(self):
        test_input = '2^2'
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        expected_res = '(INT:2, POW, INT:2)'
        self.assertEqual(str(parsetest.node), expected_res)
        
class testComplexMath(unittest.TestCase):
    def test_Int(self):
        test_input = '9*(2-1)+2'
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        expected_res = '((INT:9, MUL, (INT:2, MINUS, INT:1)), PLUS, INT:2)'
        self.assertEqual(str(parsetest.node), expected_res)
        
class testComplexMath2(unittest.TestCase):
    def test_Int(self):
        test_input = '(2-1)+2'
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        expected_res = '((INT:2, MINUS, INT:1), PLUS, INT:2)'
        self.assertEqual(str(parsetest.node), expected_res)
        
class testComplexMath3(unittest.TestCase):
    def test_Int(self):
        test_input = '((2-1)+2)^2'
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        expected_res = '(((INT:2, MINUS, INT:1), PLUS, INT:2), POW, INT:2)'
        self.assertEqual(str(parsetest.node), expected_res)
        
class testComplexMath4(unittest.TestCase):
    def test_Int(self):
        test_input = '10/2*2-1'
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        expected_res = '(((INT:10, DIV, INT:2), MUL, INT:2), MINUS, INT:1)'
        self.assertEqual(str(parsetest.node), expected_res)


class testComplexMath3(unittest.TestCase):
    def test_Int(self):
        test_input = '2^2+1-1*3/1'
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        expected_res = '(((INT:2, POW, INT:2), PLUS, INT:1), MINUS, ((INT:1, MUL, INT:3), DIV, INT:1))'
        self.assertEqual(str(parsetest.node), expected_res)

class testSTRType(unittest.TestCase):
    def test_Int(self):
        test_input = '"hello"'
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        expected_res = 'STRING:hello'
        self.assertEqual(str(parsetest.node), expected_res)
        
class testSTRMult(unittest.TestCase):
    def test_Int(self):
        test_input = '"hello" * 2'
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        expected_res = '(STRING:hello, MUL, INT:2)'
        self.assertEqual(str(parsetest.node), expected_res)
        
class testSTRAdd(unittest.TestCase):
    def test_Int(self):
        test_input = '"hello" + " Comp430"'
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        expected_res = '(STRING:hello, PLUS, STRING: Comp430)'
        self.assertEqual(str(parsetest.node), expected_res)
        
class testSTRCombo(unittest.TestCase):
    def test_Int(self):
        test_input = '"hello" * 2 + " Comp430"'
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        expected_res = '((STRING:hello, MUL, INT:2), PLUS, STRING: Comp430)'
        self.assertEqual(str(parsetest.node), expected_res)
        
class testParseError(unittest.TestCase):      
    def test_ParseError(self):
        test_input = '"hello" + 2'
        test=False
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        if error != None: test = True
        message = 'Test: Should Count as Illegal Operation'
        self.assertTrue(test, message)
        
class testParseError1(unittest.TestCase):      
    def test_ParseError(self):
        test_input = '"hello" - 2'
        test=False
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        if error != None: test = True
        message = 'Test: Should Count as Illegal Operation'
        self.assertTrue(test, message)
        
class testParseError3(unittest.TestCase):      
    def test_ParseError(self):
        test_input = '"hello" / 2'
        test=False
        tokens, error = Lexer(default, test_input).make_tokens()
        parsetest = Parser(tokens).parse()
        if error != None: test = True
        message = 'Test: Should Count as Illegal Operation'
        self.assertTrue(test, message)
        

if __name__  == '__main__':
    unittest.main()
