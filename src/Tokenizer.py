#CONSTANTS#
DIGITS = '0123456789'

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

TT_DEF      = 'FUNCTION'
TT_WHILE    = 'WHILE'
TT_IF       = 'IF'

#TOKEN CLASS#
class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

#LEXER CLASS#
class Lexer:
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
            else:
                char = self.current_char
                self.advance()
                return [], IllegalCharError(char)

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

#ERROR CLASSES#
class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result

class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illegal Character', details)

#PARSER CLASS#
class NumberNode:
    def __init__(self, tok):
        self.tok = tok
    
    def __repr__(self):
        return f'{self.tok}'

class BinOpNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node

    def __repr__(self):
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()

    def advance(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok

    def parse(self):
        res = self.expr()
        return res

    def factor(self):
        tok = self.current_tok

        if tok.type in (TT_INT, TT_FLOAT):
            self.advance()
            return NumberNode(tok)

    def term(self):
        return self.bin_op(self.factor, (TT_MULTIPLY, TT_DIVIDE))

    def expr(self):
        return self.bin_op(self.term, (TT_PLUS, TT_MINUS))

    def bin_op(self, func, ops):
        left = func()

        while self.current_tok.type in ops:
            op_tok = self.current_tok
            self.advance()
            right = func()
            left = BinOpNode(left, op_tok, right)

        return left

#RUN CLASS#
def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()
    if error: return None, error

    parser = Parser(tokens)
    ast = parser.parse()
    return ast, None
