<<<<<<< HEAD
####################################################################################
####################################################################################
############ Using test file in the src folder. Igonore for now ####################
####################################################################################
####################################################################################


# from importlib import import_module
# import unittest
# import sys
=======
import unittest
import Tokenizer
 
class TestTokens(unittest.TestCase):
    def test_run(self):
        test_input = '9+9'
        expected_text = '[INT:9,PLUS,INT:9]'
        self.assertEqual(Tokenizer.run(test_input), expected_text)
>>>>>>> 9d51997d7107a3aab74ca9df43054feed17bd60c

# sys.path.append(1, '../')
# from source.Tokenizer import Tokenizer as module



# # NOT 100% SURE THIS TEST CASE WILL WORK TRYING TO GET IMPORT TO WORK FOR NOW
# class TestTokens(unittest.TestCase):
#     def test_additions(self):
#         test_input = '9+9'
#         expected_text = '[INT:9,PLUS,INT:9]'
#         self.assertEqual(module.run(test_input), expected_text)

# if __name__  == '__main__':
#     unittest.main()


    