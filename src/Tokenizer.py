#CONSTANTS#
DIGITS = '01234567890'

#TOKENS#
TT_INT      = 'INT'
TT_FLOAT    = 'FLOAT'
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

#TOKEN CLASS#
class Token(object):
    def __init__(self, type, value = None):
        self.type = type
        self.value = value

    def __repr__(self) -> str:
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

#LEXER CLASS#
class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
                self.advance()
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MULTIPLY))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIVIDE))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPARAN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPARAN))
                self.advance()
            elif self.current_char == '{':
                tokens.append(Token(TT_LCURLY))
                self.advance()
            elif self.current_char == '}':
                tokens.append(Token(TT_RCURLY))
                self.advance()
            elif self.current_char == 'if':
                tokens.append(Token(TT_IF))
                self.advance()
            elif self.current_char == 'while':
                tokens.append(Token(TT_WHILE))
                self.advance()
            else:
                char = self.current_char
                self.advance()
                return [], IllegalCharError("'" + char + "'")

        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

            if dot_count == 0:
                return Token(TT_INT, int(num_str))
            else:
                return Token(TT_FLOAT, float(num_str))

#ERROR CLASS#
class Error:
    def __int__(self, error_name, details):
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result

class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illegal Character', details)

#RUN CLASS#
def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()

    return tokens, error
