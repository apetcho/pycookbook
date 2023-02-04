#!/usr/bin/env python3
# Example: Non-recursive implementation using yield

from node import Node, NodeVisitor


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class BinaryOperator(Node):
    def __init__(self, left:Node, right:Node):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass

class Mul(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class Negate(UnaryOperator):
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


class Evaluator(NodeVisitor):
    def visit_number(self, node:Number):
        return node.value
    
    def visit_add(self, node:Add):
        yield (yield node.left) + (yield node.right)

    def visit_sub(self, node:Sub):
        yield (yield node.left) - (yield node.right)

    def visit_mul(self, node:Mul):
        yield (yield node.left) * (yield node.right)

    def visit_div(self, node:Div):
        yield (yield node.left) / (yield node.right)

    def visit_negate(self, node:Negate):
        yield -(yield node.operand)


def main():
    """Main entry."""
    # 1 + 2*(3 - 4)/5
    t1 = Sub(Number(3), Number(4))
    t2 = Mul(Number(2), t1)
    t3 = Div(t2, Number(5))
    t4 = Add(Number(1), t3)
    # Evaluate it
    evaluator = Evaluator()
    print(evaluator.visit(t4))
    # Blow it up
    num = Number(0)
    for n in range(1, 1000000):
        num = Add(num, Number(n))

    try:
        print(evaluator.visit(num))
    except RuntimeError as err:
        print(err)


if __name__ == "__main__":
    main()
