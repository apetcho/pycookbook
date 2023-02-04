#!/usr/bin/env python3
# Base class and non-recursive visitor implementation.
#
import types

class Node:
    pass


class NodeVisitor:
    def visit(self, node:Node):
        stack = [node]
        lastResult = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(lastResult))
                    lastResult = None
                elif isinstance(last, Node):
                    stack.append(self._visit(stack.pop()))
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
    
    def generic_visit(self, node):
        raise RuntimeError(f"No visit_{(type(node).__name__).lower()} method")
    
