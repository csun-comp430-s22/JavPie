import unittest
import Tokenizer

# NOT 100% SURE THIS TEST CASE WILL WORK TRYING TO GET IMPORT TO WORK FOR NOW
class TestTokens(unittest.TestCase):
    def test_additions(self):
        test_input = '1+1'
        expected_text = '[INT:1, PLUS, INT:1]'
        self.assertEqual(Tokenizer.run(test_input), expected_text)

if __name__  == '__main__':
    unittest.main()



    