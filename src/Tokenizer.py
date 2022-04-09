import Error
import Parser
from strings_with_arrows import *
import string

#CONSTANTS#
DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTER_DIGITS = LETTERS + DIGITS

#TOKENS#
TT_INT          = 'INT'
TT_FLOAT        = 'FLOAT'
TT_STRING       = 'STRING'
TT_IDENTIFIER   = 'IDENTIFIER'
TT_KEYWORD      = 'KEYWORD'

TT_VARIABLE = 'VARIABLE'

TT_PLUS      = 'PLUS'
TT_MINUS     = 'MINUS'
TT_MULTIPLY  = 'MULTIPLY'
TT_DIVIDE    = 'DIVIDE'
TT_EQ        = 'EQ'

TT_LPAREN   = 'LPARAN'
TT_RPAREN   = 'RPARAN'
TT_LCURLY   = 'LCURLY'
TT_RCURLY   = 'RCURLY'

TT_DEF      = 'FUNCTION'
TT_WHILE    = 'WHILE'
TT_IF       = 'IF'

TT_EOF      = 'EOF'
TT_POW      = 'POW'

KEYWORDS = {
    'VAR'
}

#SYMBOL TABLE#

class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.parent = None
        
    def get(self, name):
        value = self.symbols.get(name, None)
        if value == None and self.parent:
            return self.parent.get(name)
        
        return value
    
    def set(self, name, value):
        self.symbols[name] = value
        
    def remove(self, name):
        del self.symbols[name]

#INTERPRETER#

class Interpreter:
    def visit(self, node, context):
       method_name = f'visit_{type(node).__name__}'
       method = getattr(self, method_name, self.no_visit_method)
       return method(node, context)
    
    def no_visit_method(self, node, context):
        raise Exception(f'No vistit_{type(node).__name__} method defined')

    def visit_NumberNode(self,node, context):
        return Parser.RTResult().success(Number(node.tok.value).set_context(context).set_pos(node.pos_start, node.pos_end))

    def Visit_VarAccessNode(self, node, context):
        res = Parser.RTResult()
        var_name = node.var_name_tok.value
        value = context.symbol_table.get(var_name)
        
        if not value:
            res.failure(Error.RTError(
                node.pos_start, node.pos_end,
                f"'{var_name}' is not defined",
                  context
            ))
        value = value.copy().set_pos(node.pos_start, node.pos_end)
        return res.success(value)
    
    def visit_VarAssignNode(self, node, context):
        res = Parser.RTResult()
        var_name = node.var_name_tok.value
        value = res.register(self.visit(node.value_node, context))
        if res.error: return res
        
        context.symbol_table.set(var_name, value)
        return res.success(value)

        
    def visit_BinOpNode(self, node, context):
        res = Parser.RTResult()
        left = res.register(self.visit(node.left_node, context))
        if res.error: return res
        right = res.register(self.visit(node.right_node, context))

        if node.op_tok.value == TT_PLUS:
            result, error = left.added_to(right)
        elif node.op_tok.value == TT_MINUS:
            result, error = left.subbed_by(right)
        elif node.op_tok.value == TT_MULTIPLY:
            result, error = left.multed_by(right)
        elif node.op_tok.value == TT_DIVIDE:
            result,error = left.divided_by(right)
        elif node.op_tok.value == TT_POW:
            result,error = left.powed_by(right)
        
        if error: 
            return res.failure(error)
        else:
            return res.success(result.set_pos(node.pos_start, node.pos_end))

    
            
    def visit_UnaryOpNode(self, node, context):
        res = Parser.RTResult()
        number = res.register(self.visit(node.node), context)
        if res.error: return res

        errpr = None
        if node.op_tok.type == TT_MINUS:
            number, error = number.multed_by(Number(-1))
        if error:
            return res.failure(error)
        else: 
            return res.success(number.set_pos(node.pos_start, node.pos_end))


###
class Number:
    def __init__(self, value):
        self.value = value
        self.set_pos()
        self.set_context()
        
    def set_pos(self, pos_start= None, pos_end = None):
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def set_context(self, context = None):
        self.context = context
        return self
        
    def added_to(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value).set_context(self.context), None

    def subbed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value).set_context(self.context), None

    def multed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value).set_context(self.context), None

    def divided_by(self, other):
        if isinstance(other, Number):
            if other.value ==0:
                return None, Error.RTError(
                    other.pos_start, other.pos_end,
                    'Division by Zero >:(', self.context
                )
            return Number(self.value / other.value).set_context(self.context), None

    def powed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value ** other.value).set_context(self.context), None
    
    def copy(self):
        copy = Number(self.value)
        copy.set_pos(self.set_pos, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __repr__(self):
        return str(self.value)


    

#STRING#

class StringNode:
    def __init__(self, tok):
        self.tok = tok
        self.pos_start = self.tok.pos_start
        self.pos_end = self.tok.pos_end

    def __repr__(self):
        return f'{self.tok}'
        

#POSITION#
class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char=None):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)


#TOKEN CLASS#
class Token:
    def __init__(self, type_, value=None, pos_start=None, pos_end=None):
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()

        if pos_end:
            self.pos_end = pos_end
            
    def matches(self, type_, value):
        return self.type == type_ and self.value == value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

#LEXER CLASS#
class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char in LETTERS:
                tokens.append(self.make_identifier)
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS, pos_start=self.pos))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS, pos_start=self.pos))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MULTIPLY, pos_start=self.pos))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIVIDE, pos_start=self.pos))
                self.advance()
            elif self.current_char == '^':
                tokens.append(Token(TT_POW, pos_start=self.pos))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN, pos_start=self.pos))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN, pos_start=self.pos))
                self.advance()
            elif self.current_char == '{':
                tokens.append(Token(TT_LCURLY, pos_start=self.pos))
                self.advance()
            elif self.current_char == '}':
                tokens.append(Token(TT_RCURLY, pos_start=self.pos))
                self.advance()
            elif self.current_char == '=':
                tokens.append(Token(TT_EQ, pos_start=self.pos))
                self.advance()                                              
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], Error.IllegalCharError(pos_start, self.pos, "'" + char + "'")

        tokens.append(Token(TT_EOF, pos_start=self.pos))
        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0
        pos_start = self.pos.copy()

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str), pos_start, self.pos)
        else:
            return Token(TT_FLOAT, float(num_str))
      
    def make_identifier(self):
        id_str = ''
        pos_start = self.pos.copy()
        
        while self.current_char != None and self.current_char in LETTER_DIGITS + '_':
            id_str += self.current_char
            self.advance()
            
        tok_type = TT_KEYWORD if id_str in KEYWORDS else TT_IDENTIFIER
        return Token(tok_type, id_str, pos_start, self.pos)

#RUN CLASS#

global_symbol_table = SymbolTable()
global_symbol_table.set("null", Number(0))

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error: return None, error
    
    parser = Parser.Parser(tokens)
    ast = parser.parse()
    if ast.error: return None, ast.error

    interpreter = Interpreter()
    context = Parser.Context('<program>')
    context.symbol_table = global_symbol_table
    result = interpreter.visit(ast.node, context)

    return result.value, result.error
  #  return ast.node, ast.error
