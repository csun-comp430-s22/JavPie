import Token


class TT_Variable(Token):


    def __init__(self, name):
        self.name = None

        self.name = name

    def __hash__(self): #if two objects are equal to each other, there hashcodes have to be the same
        #hash is a built in method to python
        return hash(self.name)

    def __str__(self):
        return self.name

    def ifequals(self, other):
        if isinstance(other, TT_Variable):
            newVar = other
            return self.name == newVar.name
        else:
            return False
