import unittest
import Tokenizer

from Tokenizer import *
default = '<stdin>'

class TestTokens(unittest.TestCase):
    def test_additions(self):
        test_input = '1+1'
        testing = Tokenizer.run(default,test_input)
        expected_text = '((INT:1, PLUS, INT:1), None)'
        self.assertEqual(str(testing), expected_text)
        
class TestTokenNum(unittest.TestCase):
    def test_Num(self):
        test_input = '9'
        testing = Tokenizer.run(default,test_input)
        expected_text = '(INT:9, None)'
        self.assertEqual(str(testing), expected_text)        
        
class TestTokens2(unittest.TestCase):
    def test_NumParan(self):
        test_input = '(3)'
        testing = Tokenizer.run(default,test_input)
        expected_text = '((LPARAN, INT:3, RPARAN), None)'
        self.assertEqual(str(testing), expected_text)


class TestTokens3(unittest.TestCase):
    def test_NumCBrace(self):
        test_input = '{5}'
        testing = Tokenizer.run(default,test_input)
        expected_text = '((LCURLY, INT:5, RCURLY), None)'
        self.assertEqual(str(testing), expected_text)

class TestTokens4(unittest.TestCase):
    def test_Division(self):
        test_input = '10/2'
        testing = Tokenizer.run(default,test_input)
        expected_text = '((INT:10, DIVIDE, INT:2), None)'
        self.assertEqual(str(testing), expected_text)

class TestTokens5(unittest.TestCase):
    def test_Multiply(self):
        test_input = '10 * 2'
        testing = Tokenizer.run(default,test_input)
        expected_text = '((INT:10, MULTIPLY, INT:2), None)'
        self.assertEqual(str(testing), expected_text)

class TestTokens6(unittest.TestCase):
    def test_Operands(self):
        test_input = '+-'
        testing = Tokenizer.run(default,test_input)
        expected_text = '((PLUS, MINUS), None)'
        self.assertEqual(str(testing), expected_text)
        
class TestTokens7(unittest.TestCase):
    def test_Decimal(self):
        test_input = '2.5'
        testing = Tokenizer.run(default,test_input)
        expected_text = '(FLOAT:2.5, None)'
        self.assertEqual(str(testing), expected_text)

class TestTokens_Error(unittest.TestCase):
    def test_String(self):
        test_input = 'string'
        testing = Tokenizer.run(default,test_input)
        expected_text = '(None, <Tokenizer.IllegalCharError object at 0x000002405638BFA0>)'
        self.assertEqual(str(testing), expected_text)

class TestToken8(unittest.TestCase):
    def test_SingleSpecial(self):
        test_input = '('
        testing = Tokenizer.run(default, test_input)
        expected_Text = '(LParen, None)'
        self.assertEqual(str(testing), expected_Text)

class TestTokens(unittest.TestCase):
    def test_additions(self):
        test_input = '1+1'
        testing = Tokenizer.run(default,test_input)
        expected_text = '(2, None)'
        self.assertEqual(str(testing), expected_text)
        
class TestTokenNum(unittest.TestCase):
    def test_Num(self):
        test_input = '9'
        testing = Tokenizer.run(default,test_input)
        expected_text = '(9, None)'
        self.assertEqual(str(testing), expected_text)        
        
class TestTokens2(unittest.TestCase):
    def test_NumParan(self):
        test_input = '(3)'
        testing = Tokenizer.run(default,test_input)
        expected_text = '(3, None)'
        self.assertEqual(str(testing), expected_text)


class TestTokens3(unittest.TestCase):
    def test_NumCBrace(self):
        test_input = '{5}'
        testing = Tokenizer.run(default,test_input)
        expected_text = '((LCURLY, INT:5, RCURLY), None)'
        self.assertEqual(str(testing), expected_text)

class TestTokens4(unittest.TestCase):
    def test_Division(self):
        test_input = '10/2'
        testing = Tokenizer.run(default,test_input)
        expected_text = '(5.0, None)'
        self.assertEqual(str(testing), expected_text)

class TestTokens5(unittest.TestCase):
    def test_Multiply(self):
        test_input = '10 * 2'
        testing = Tokenizer.run(default,test_input)
        expected_text = '(20, None)'
        self.assertEqual(str(testing), expected_text)

class TestTokens6(unittest.TestCase):
    def test_Operands(self):
        test_input = '+-'
        testing = Tokenizer.run(default,test_input)
        expected_text = '((PLUS, MINUS), None)'
        self.assertEqual(str(testing), expected_text)
        
class TestTokens7(unittest.TestCase):
    def test_Decimal(self):
        test_input = '2.5'
        testing = Tokenizer.run(default,test_input)
        expected_text = '(2.5, None)'
        self.assertEqual(str(testing), expected_text)

class TestTokens_Error(unittest.TestCase):
    def test_String(self):
        test_input = 'string'
        testing = Tokenizer.run(default,test_input)
        expected_text = '(None, <Tokenizer.IllegalCharError object at 0x000002405638BFA0>)'
        self.assertEqual(str(testing), expected_text)

class TestToken8(unittest.TestCase):
    def test_SingleSpecial(self):
        test_input = '('
        testing = Tokenizer.run(default, test_input)
        expected_Text = '(LParen, None)'
        self.assertEqual(str(testing), expected_Text)

class TestToken9(unittest.TestCase):
    def test_9(self):
        test_input = '5==5'
        testing = Tokenizer.run(default, test_input)
        expected_Text = '(1, None)'
        self.assertEqual(str(testing), expected_Text)

class TestToken10(unittest.TestCase):
    def test_SingleSpecial(self):
        test_input = '5!=5'
        testing = Tokenizer.run(default, test_input)
        expected_Text = '(0, None)'
        self.assertEqual(str(testing), expected_Text)

class TestToken11(unittest.TestCase):
    def test_SingleSpecial(self):
        test_input = 'IF 5==5 THEN 123'
        testing = Tokenizer.run(default, test_input)
        expected_Text = '(123, None)'
        self.assertEqual(str(testing), expected_Text)

class TestToken12(unittest.TestCase):
    def test_SingleSpecial(self):
        test_input = 'FUN hello(a,b,c)->a+b+c'
        testing = Tokenizer.run(default, test_input)
        expected_Text = '(<function hello>, None)'
        self.assertEqual(str(testing), expected_Text)

class TestToken13(unittest.TestCase):
    def test_SingleSpecial(self):
        test_input = '"this is a string"'
        testing = Tokenizer.run(default, test_input)
        expected_Text = '("this is a string", None)'
        self.assertEqual(str(testing), expected_Text)


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

class TestToken14(unittest.TestCase):
    def test_SingleSpecial(self):
        test_input = '5<6'
        testing = Tokenizer.run(default, test_input)
        expected_Text = '(1, None)'
        self.assertEqual(str(testing), expected_Text)

class TestToken15(unittest.TestCase):
    def test_SingleSpecial(self):
        test_input = '1==1 AND 2==2'
        testing = Tokenizer.run(default, test_input)
        expected_Text = '(1, None)'
        self.assertEqual(str(testing), expected_Text)

class TestToken16(unittest.TestCase):
    def test_SingleSpecial(self):
        test_input = 'VAR i=0'
        testing = Tokenizer.run(default, test_input)
        expected_Text = '(0, None)'
        self.assertEqual(str(testing), expected_Text)

class TestToken17(unittest.TestCase):
    def test_SingleSpecial(self):
        test_input = 'WHILE i<10 THEN VAR i = i+1'
        testing = Tokenizer.run(default, test_input)
        expected_Text = '(None, None)'
        self.assertEqual(str(testing), expected_Text)

class TestToken18(unittest.TestCase):
    def test_SingleSpecial(self):
        test_input = '5+2 == 3+4'
        testing = Tokenizer.run(default, test_input)
        expected_Text = '(1, None)' #typechecker for boolean
        self.assertEqual(str(testing), expected_Text)
class TestToken19(unittest.TestCase):
    def test_SingleSpecial(self):
        test_input = '7^2'
        testing = Tokenizer.run(default, test_input)
        expected_Text = '(49, None)'
        self.assertEqual(str(testing), expected_Text)

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



    