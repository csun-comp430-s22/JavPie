import Error
import Tokenizer


#Erro Runtime

class RTResult:
    def __init__(self):
        self.value = None
        self.error = None

    def register(self, res):
        if res.error: self.error = res.error
        return res.value

    def success(self, value):
        self.value = value
        return self
    def failure(self, error):
        self.error = error
        return self

#NODE CLASS#
class NumberNode:
    def __init__(self, tok):
        self.tok = tok
        self.pos_start = self.tok.pos_start
        self.pos_end =self.tok.pos_end
    
    def __repr__(self):
        return f'{self.tok}'

class BinOpNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node

        self.pos_start = self.left_node.pos_start
        self.pos_end = self.right_node.pos_end

    def __repr__(self):
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'


class UnaryOpNode:
    def __init__(self, op_tok, node):
        self.op_tok = op_tok
        self.node = node

        self.pos_start = self.op_tok.pos_start
        self.pos_end = node.pos_end

    def __repr__(self):
        return f'({self.op_tok}, {self.node})'
#PARSE RESULT#
class ParseResult:
    def __init__(self):
        self.error = None
        self.node = None

    def register(self, res):
        if isinstance(res, ParseResult):
            if res.error: self.error = res.error
            return res.node

        return res
    
    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        self.error = error
        return self

#PARSER CLASS#
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
        if not res.error and self.current_tok.type != Tokenizer.TT_EOF:
            return res.failure(Error.InvalidSyntaxError( 
                self.current_tok.pos_start, self.current_tok.pos_end,
                "Expected '+', '-', '*', or '/' \n"
            ))
        return res

    def factor(self):
        res = ParseResult()
        tok = self.current_tok

        if tok.type in (Tokenizer.TT_PLUS, Tokenizer.TT_MINUS):
            res.register(self.advance())
            factor = res.register(self.factor())
            if res.error: return res
            return res.success(UnaryOpNode(tok, factor))

        if tok.type in (Tokenizer.TT_INT, Tokenizer.TT_FLOAT):
            res.register(self.advance())
            return res.success(NumberNode(tok))

        elif tok.type == Tokenizer.TT_LPAREN:
            res.register(self.advance())
            expr= res.register(self.expr())
            if res.error: return res
            if self.current_tok.type == Tokenizer.TT_RPAREN:
                res.register(self.advance())
                return res.success(expr)
            else:
                return res.failure(Error.InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected ')'"
                ))


        return res.failure(Error.InvalidSyntaxError(
            tok.pos_start, tok.pos_end,
            "Expected int or float \n"
        ))

    def term(self):
        return self.bin_op(self.factor, (Tokenizer.TT_MULTIPLY, Tokenizer.TT_DIVIDE))

    def expr(self):
        return self.bin_op(self.term, (Tokenizer.TT_PLUS, Tokenizer.TT_MINUS))

    def bin_op(self, func, ops):
        res = ParseResult()
        left = res.register(func())
        if res.error: return res

        while self.current_tok.type in ops:
            op_tok = self.current_tok
            res.register(self.advance())
            right = res.register(func())
            if res.error: return res
            left = BinOpNode(left, op_tok, right)

        return res.success(left)

    #def atom(self):
      #  res = ParseResult()
       # tok = self.current_tok

        #if tok.type == Tokenizer.TT_STRING:
         #   res.register_advancement()
          #  self.advance()
           # return res.success(Tokenizer.StringNode(tok))

class Context: 
    def __init__(self, display_name, parent = None, parent_entry_pos = None):
        self.display_name = display_name
        self.parent = parent
        self.parent_entry_pos = parent_entry_pos
