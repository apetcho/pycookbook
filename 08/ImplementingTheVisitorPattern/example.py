#!/usr/bin/env python3
# Example of the visitor pattern

# -*-------------------------------------------------------------*-
# -*- The following class represent nodes in an expression tree -*-
# -*-------------------------------------------------------------*-


class Node:
    pass


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand

class BinaryOperator(Node):
    def __init__(self, left, right):
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


# -*---------------------------*-
# -*- The visitore base class -*-
# -*---------------------------*-

class NodeVisitor:
    def visit(self, node):
        methname = f"visit_{(type(node).__name__).lower()}"
        method = getattr(self, methname, None)
        if method is None:
            method = self.generic_visit
        return method(node)
    
    def generic_visit(self, node):
        raise RuntimeError(f"No visit_{type(node).__name__} method")
    

# -*--------------------------------------*-
# -*- Example 1: An expression evaluator -*-
# -*--------------------------------------*-

class Evaluator(NodeVisitor):
    def visit_number(self, node:Number):
        return node.value
    
    def visit_add(self, node:Add):
        return self.visit(node.left) + self.visit(node.right)
    
    def visit_sub(self, node:Sub):
        return self.visit(node.left) - self.visit(node.right)
    
    def visit_mul(self, node:Mul):
        return self.visit(node.left) * self.visit(node.right)
    
    def visit_div(self, node:Div):
        return self.visit(node.left) / self.visit(node.right)
    
    def visit_negate(self, node:Negate):
        return -node.operand


# -*------------------------------------------*-
# -*- Example 2: Generate stack instructions -*-
# -*------------------------------------------*-


class StackCode(NodeVisitor):
    def generate_code(self, node):
        self.instructions = []
        self.visit(node)
        return self.instructions
    
    def visit_number(self, node:Number):
        self.instructions.append(("PUSH", node.value))

    def binop(self, node:BinaryOperator, instruction):
        self.visit(node.left)
        self.visit(node.right)
        self.instructions.append((instruction, ))

    def visit_add(self, node:Add):
        self.binop(node, "ADD")

    def visit_sub(self, node:Sub):
        self.binop(node, "SUB")

    def visit_mul(self, node:Mul):
        self.binop(node, "MUL")

    def visit_div(self, node:Div):
        self.binop(node, "DIV")

    def unaryop(self, node:UnaryOperator, instruction:str):
        self.visit(node.operand)
        self.instructions.append((instruction,))

    def visit_negate(self, node:Negate):
        self.unaryop(node, "NEG")


# -*------------------------------------------*-
# -*- Example of the above classes in action -*-
# -*------------------------------------------*-

def main():
    """Main entry."""
    t1 = Sub(Number(3), Number(4))
    t2 = Mul(Number(2), t1)
    t3 = Div(t2, Number(5))
    t4 = Add(Number(1), t3)

    evaluator = Evaluator()
    print(f"Should get 0.6: {evaluator.visit(t4)}")

    stackc = StackCode()
    code = stackc.generate_code(t4)
    for c in code:
        print(c)


if __name__ == "__main__":
    main()
