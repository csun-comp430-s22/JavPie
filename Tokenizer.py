#Tokens#

TT_INT      = 'INTEGER'
TT_STRING   = 'STRING'
TT_VARIABLE = 'VARIABLE'
TT_PLUS     = 'PLUS'
TT_MINUS    = 'MINUS'
TT_MULTIPLY = 'MULTIPLY'
TT_DIVIDE   = 'DIVIDE'
TT_LPARAN   = 'LPARAN'
TT_RPARAN   = 'RPARAN'
TT_LCURLY   = 'LCURLY'
TT_RCURLY   = 'RCURLY'
TT_WHILE    = 'WHILE'
TT_IF       = 'IF'
TT_EOF      = 'EOF'

#Token Class#
class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value}'.format(
            type = self.type,
            value = repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception('Error Parsing input')
    
    def get_next_token(self):
        text = self.text

        if self.pos > len(text) - 1:
            return Token(TT_EOF, None)

        current_char = text[self.pos]

        if current_char.isdigit():
            token = Token(TT_INT, int(current_char))
            self.pos += 1
            return token
        
        if current_char == '+':
            token = Token(TT_PLUS, current_char)
            self.pos += 1
            return token

        self.error()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()
        left = self.current_token
        self.eat(TT_INT)

        op = self.current_token
        self.eat(TT_PLUS)

        right = self.current_token
        self.eat(TT_INT)

        result = left.value + right.value
        return result

def main():
    while True:
        try:
            text = input('JavPie > ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()