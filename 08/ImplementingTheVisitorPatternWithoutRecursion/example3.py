#!/usr/bin/env python3
# Example: Modified non-recursive implementation using a special Visit() class
# to signal should be visited next
import types


class Node:
    pass


class Visit:
    def __init__(self, node:Node):
        self.node = node


class NodeVisitor:
    def visit(self, node:Node):
        stack = [Visit(node)]
        lastResult = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(lastResult))
                    lastResult = None
                elif isinstance(last, Visit):
                    stack.append(self._visit(stack.pop().node))
                else:
                    lastResult = stack.pop()
            except StopIteration:
                stack.pop()
        return lastResult
    
    def _visit(self, node:Node):
        methodname = f"visit_{(type(node).__name__).lower()}"
        method = getattr(self, methodname, None)
        if method is None:
            method = self.generic_visit
        return method(node)
    
    def generic_visit(self, node:Node):
        raise RuntimeError(f"No visit_{(type(node).__name__).lower()} method")
    

class UnaryOperator(Node):
    def __init__(self, operand) -> None:
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
        yield (yield Visit(node.left)) + (yield Visit(node.right))

    def visit_sub(self, node:Sub):
        yield (yield Visit(node.left)) - (yield Visit(node.right))

    def visit_mul(self, node:Mul):
        yield (yield Visit(node.left)) * (yield Visit(node.right))

    def visit_div(self, node:Div):
        yield (yield Visit(node.left)) / (yield Visit(node.right))

    def visit_negate(self, node:Negate):
        yield -(yield Visit(node.operand))


def main():
    """Main entry."""
    # 1 + 2*(3-4)/5
    t1 = Sub(Number(3), Number(4))
    t2 = Mul(Number(2), t1)
    t3 = Div(t2, Number(5))
    t4 = Add(Number(1), t3)
    # -* Evaluate it
    evaluator = Evaluator()
    print(evaluator.visit(t4))
    # -*- Blow it up
    num = Number(0)
    for n in range(1, 10000):
        num = Add(num, Number(n))

    try:
        print(evaluator.visit(num))
    except RuntimeError as err:
        print(err)


if __name__ == "__main__":
    main()
