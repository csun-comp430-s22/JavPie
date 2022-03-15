import unittest
import Tokenizer

# NOT 100% SURE THIS TEST CASE WILL WORK TRYING TO GET IMPORT TO WORK FOR NOW
class TestTokens(unittest.TestCase):
    def test_additions(self):
        test_input = '1+1'
        expected_text = '[INT:1, PLUS, INT:1]'
        self.assertEqual(Tokenizer.run(test_input), expected_text)
class TestTokens2(unittest.TestCase):
    def test_additions(self):
        test_input = '(3)'
        expected_text = '[LPAREN, INT:3, RPAREN]'
        self.assertEqual(Tokenizer.run(test_input), expected_text)


class TestTokens3(unittest.TestCase):
    def test_additions(self):
        test_input = '{5}'
        expected_text = '[LCURLY, INT:3, RCURLY]'
        self.assertEqual(Tokenizer.run(test_input), expected_text)

class TestTokens4(unittest.TestCase):
    def test_additions(self):
        test_input = '10/2'
        expected_text = '[INT: 10, DIVIDE, INT: 2]'
        self.assertEqual(Tokenizer.run(test_input), expected_text)

class TestTokens5(unittest.TestCase):
    def test_additions(self):
        test_input = '10 * 2'
        expected_text = '[INT:10, MULTIPLY, INT:2]'
        self.assertEqual(Tokenizer.run(test_input), expected_text)

class TestTokens6(unittest.TestCase):
    def test_additions(self):
        test_input = '+-'
        expected_text = '[PLUS, MINUS]'
        self.assertEqual(Tokenizer.run(test_input), expected_text)
class TestTokens7(unittest.TestCase):
    def test_additions(self):
        test_input = '2.5'
        expected_text = '[FLOAT]'
        self.assertEqual(Tokenizer.run(test_input), expected_text)

class TestTokens_Error(unittest.TestCase):
    def test_additions(self):
        test_input = 'string'
        expected_text = '[ERROR]'
        self.assertEqual(Tokenizer.run(test_input), expected_text)

if __name__  == '__main__':
    unittest.main()



    