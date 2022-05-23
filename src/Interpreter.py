from Error import RTError
import JavPie

#RUNTIME RESULT#
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

#Number Class#
class Number:
    def __init__(self, value):
        self.value = value
        self.set_pos()

    def set_pos(self, pos_start=None, pos_end=None):
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def added_to(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value), None
    
    def subbed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value), None
    
    def multed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value), None

    def dived_by(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, RTError(
                    other.pos_start, other.pos_end,
                    'Division by zero'
                )
            return Number(self.value / other.value), None

    def __repr__(self):
        return str(self.value)

#INTERPRETER CLASS#
class Interpreter:
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        raise Exception(f'No visit_{type(node).__name__} method defined')

    def visit_NumberNode(self, node):
        return RTResult().success(
            Number(node.tok.value).set_pos(node.pos_start, node.pos_end)
        )

    def visit_BinOpNode(self, node):
        res = RTResult()

        left = res.register(self.visit(node.left_node))
        if res.error: return res
        right = res.register(self.visit(node.right_node))
        if res.error: return res

        if node.op_tok.type == JavPie.TT_PLUS:
            result, error = left.added_to(right)
        elif node.op_tok.type == JavPie.TT_MINUS:
            result, error = left.subbed_by(right)
        elif node.op_tok.type == JavPie.TT_MULTIPLY:
            result, error = left.multed_by(right)
        elif node.op_tok.type == JavPie.TT_DIVIDE:
            result, error = left.dived_by(right)

        if error:
            return res.failure(error)
        else:
            return res.success(result.set_pos(node.pos_start, node.pos_end))

    def visit_UnaryOpNode(self, node):
        res = RTResult()
        number = self.visit(node.node)
        if res.error: return res

        error = None

        if node.op_tok.type == JavPie.TT_MINUS:
            number, error = number.multed_by(Number(-1))

        if error:
            return res.failure(error)
        else:
            return res.success(number.set_pos(node.pos_start, node.pos_end))