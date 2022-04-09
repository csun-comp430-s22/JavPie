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
    
class VarAccessNode:
    def __init__(self, var_name_tok):
        self.var_name_tok = var_name_tok
        
        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.var_name_tok.pos_end
        
class VarAssignNode:
    def __init__(self, var_name_tok, value_node):
        self.var_name_tok = var_name_tok
        self.value_node = value_node
        
        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.var_name_tok.pos_end

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
        self.advance_count = 0

    def register_advancement(self):
        self.advance_count += 1

    def register(self, res):
        self.advance_count += res.advance_count
        if res.error: self.error = res.error
        return res.node

    
    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        if not self.error or self.advance_count == 0:# havent advanced since
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

    def atom(self):
        res = ParseResult()
        tok = self.current_tok
        
        if tok.type in (Tokenizer.TT_INT, Tokenizer.TT_FLOAT):
            res.register_advancement()
            self.advance()
            return res.success(NumberNode(tok))
        
        elif tok.type == Tokenizer.TT_IDENTIFIER:
            res.register_advancement()
            self.advance()
            return res.success(VarAccessNode(tok))

        elif tok.type == Tokenizer.TT_LPAREN:
            res.register_advancement()
            self.advance()
            expr= res.register(self.expr())
            if res.error: return res
            if self.current_tok.type == Tokenizer.TT_RPAREN:
                res.register_advancement()
                self.advance()
                return res.success(expr)
            else:
                return res.failure(Error.InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected ')'"
                ))
                
        return res.failure(Error.InvalidSyntaxError(
            tok.pos_start, tok.pos_end,
            "Expected int, float, identifier, '+', '_', or '('"
        ))
    
    def power(self):
        return self.bin_op(self.atom, (Tokenizer.TT_POW, ), self.factor)
        
    def factor(self):
        res = ParseResult()
        tok = self.current_tok

        if tok.type in (Tokenizer.TT_PLUS, Tokenizer.TT_MINUS):
            res.register_advancement()
            self.advance()
            factor = res.register(self.factor())
            if res.error: return res
            return res.success(UnaryOpNode(tok, factor))
        
        return self.power()
        # return res.failure(Error.InvalidSyntaxError(
        #     tok.pos_start, tok.pos_end,
        #     "Expected int or float \n"
        # ))

    def term(self):
        return self.bin_op(self.factor, (Tokenizer.TT_MULTIPLY, Tokenizer.TT_DIVIDE))

    def expr(self):
        res = ParseResult()
        
        if self.current_tok.matches(Tokenizer.TT_KEYWORD, 'VAR'):
            res.register_advancement()
            self.advance()
            if self.current_tok.type != Tokenizer.TT_IDENTIFIER:
                return res.failure(Error.InvalidSyntaxError(
                   self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected Identifier"
                ))
            
            var_name = self.current_tok
            res.register_advancement()
            self.advance()
            
            if self.current_tok.type != Tokenizer.TT_EQ:
                return res.failure(Error.InvalidSyntaxError(
                   self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected '='"
                ))

            res.register_advancement()
            self.advance()
            expr = res.register(self.expr())
            if res.error: return res
            return res.success(VarAssignNode(var_name, expr))
            
        node = res.register(self.bin_op(self.term, (Tokenizer.TT_PLUS, Tokenizer.TT_MINUS)))

        if res.error: 
            return res.failure(Error.InvalidSyntaxError(
            self.current_tok.pos_start, self.current_tok.pos_end,
            "Expected 'VAR', int, float, identifier, '+', '-', or '('"
        ))
        
        return res.success(node)
 
    def bin_op(self, func_a, ops, func_b=None):
        if func_b == None:
            func_b = func_a
            
        res = ParseResult()
        left = res.register(func_a())
        if res.error: return res

        while self.current_tok.type in ops:
            op_tok = self.current_tok
            res.register_advancement()
            self.advance()
            right = res.register(func_b())
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

#CONTEXT FILE# originally in parser.py, moved from Tokenizer.py uwu
class Context: 
    def __init__(self, display_name, parent = None, parent_entry_pos = None):
        self.display_name = display_name
        self.parent = parent
        self.parent_entry_pos = parent_entry_pos
        self.symbol_table = None
      