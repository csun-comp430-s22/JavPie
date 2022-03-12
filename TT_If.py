import Token


class TT_If(Token):

    def isequal(self, other):
        return isinstance(other, TT_If)

    def __hash__(self):
        return 3
    
    def __str__(self):
        return "If Token"

