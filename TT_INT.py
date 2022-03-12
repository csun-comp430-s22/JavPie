import Token

class TT_INT(Token): 
    def TT_INT(self, value): #or def __init__
        self.value =0

        self.value = value

    def isequal(self, other):
        if isinstance(other, TT_INT):

            asInt = other
            return self.value == asInt.value
        else:
            return False

    def __hash__(self):
        return self.value
    
    def __str__(self):
        return str(self.value)
