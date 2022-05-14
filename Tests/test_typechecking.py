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
    def test_Int(self):
        test_input = '1'
        testing = Lexer(default, test_input).make_tokens()
        expected_res = '([INT:1, EOF], None)'
        self.assertEqual(str(testing), expected_res)


if __name__  == '__main__':
    unittest.main()
