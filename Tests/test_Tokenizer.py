import unittest
import src.Tokenizer as Tokenizer
 


class TestTokens(unittest.TestCase):
    def test_run(self):
        test_input = '9+9'
        expected_text = '[INT:9,PLUS,INT:9]'
        self.assertEqual(Tokenizer.run(test_input), expected_text)

if __name__  == '__main__':
    unittest.main()



    