import Token

class TT_False(Token):
    def isequal(self, other):
        return isinstance(other, TT_False)

    def __hash__(self):
        return 1

    def __str__(self):
        return "False Token"


        #isinstance built in python method that allows
        #you to verfiy a value's data type, check if value is string or list etc