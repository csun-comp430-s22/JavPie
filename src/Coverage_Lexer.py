import unittest
import Tokenizer


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

if __name__  == '__main__':
    unittest.main()



    