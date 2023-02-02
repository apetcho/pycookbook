#!/usr/bin/env python3
"""An example of writing a simple recursive descent parser."""
import re
import collections
from typing import Tuple, Union

# -*- Token specification -*-
NUM = r"(?P<NUM>\d+)"
PLUS = r"(?P<PLUS>\+)"
MINUS = r"(?P<MINUS>-)"
TIMES = r"(?P<TIMES>\*)"
DIVIDE = r"(?P<DIVIDE>/)"
LPAREN = r"(?P<LPAREN>\()"
RPAREN = r"(?P<RPAREN>\))"
WS = r"(?P<WS>\s+)"

master_pat = re.compile(
    '|'.join([NUM, PLUS, MINUS, TIMES, DIVIDE, LPAREN, RPAREN, WS])
)

# -*- Tokenizer -*-
Token = collections.namedtuple("Token", ["type", "value"])

def generate_tokens(text):
    # scanner = master_pat.scanner(text)
    for m in re.finditer(master_pat, text):
        token = Token(m.lastgroup, m.group())
        if token.type != "WS":
            yield token


# -*----------*-
# -*- Parser -*-
# -*----------*-

class ExpressionEvaluator:
    """Implementation of a recursive descent parser.
    
    Each method implement a single grammar rule. Use the ._accept() method
    to test and accept the current lookahead token. Use the ._expect() method
    to exactly match and discard the next token on the input (or raise a
    SyntaxError if it doesn't match).
    """

    def parse(self, text:str):
        self.tokens = generate_tokens(text)
        # -*- Last symbol consumed
        self.tok = None
        # -*- Next symbol tokenized
        self.nexttok = None
        # -*- Load first lookahead token
        self._advance()
        return self.expr()
    
    def _advance(self) -> None:
        """Advance one token ahead."""
        self.tok = self.nexttok
        self.nexttok = next(self.tokens, None)

    def _accept(self, tokentype) -> bool:
        """Test and consume the next token if it matches toktype."""
        if self.nexttok and self.nexttok.type == tokentype:
            self._advance()
            return True
        else:
            return False

    def _expect(self, toktype):
        """Consume next token if it matches toktype or raise SyntaxError."""
        if not self._accept(toktype):
            raise SyntaxError(f"Expected {toktype}")

    def expr(self):
        """expression ::= term { ('+' | '-') term }*"""
        exprval = self.term()
        while self._accept("PLUS") or self._accept("MINUS"):
            op = self.tok.type
            right = self.term()
            if op == "PLUS":
                exprval += right
            elif op == "MINUS":
                exprval -= right
        return exprval

    def term(self) -> Union[int, float]:
        """term ::= factor {('*'|'/') factor }*"""
        termval = self.factor()
        while self._accept("TIMES") or self._accept("DIVIDE"):
            op = self.tok.type
            right = self.factor()
            if op == "TIMES":
                termval *= right
            elif op == "DIVIDE":
                termval /= right
        return termval

    def factor(self) -> Union[int, float]:
        """factor ::= NUM | ( expr )"""
        if self._accept("NUM"):
            return int(self.tok.value)
        elif self._accept("LPAREN"):
            exprval = self.expr()
            self._expect("RPAREN")
            return exprval
        else:
            raise SyntaxError("Expected NUMBER or LPAREN")


# -*-----------------------------*-
# -*- Example of building trees -*-
# -*-----------------------------*-

class ExpressionTreeBuilder(ExpressionEvaluator):
    def expr(self) -> Tuple[str, str, str]:
        """expression ::= term { ('+' | '-') term }"""
        exprval = self.term()
        while self._accept("PLUS") or self._accept("MINUS"):
            op = self.tok.type
            right = self.term()
            if op == "PLUS":
                exprval = ("+", exprval, right)
            elif op == "MINUS":
                exprval = ('-', exprval, right)
        return exprval

    def term(self) -> Tuple[str, str, str]:
        """term ::= factor { ('*' | '/' ) factor }"""
        termval = self.factor()
        while self._accept("TIMES") or self._accept("DIVIDE"):
            op = self.tok.type
            right = self.factor()
            if op == "TIMES":
                termval = ("*", termval, right)
            elif op == "DIVIDE":
                termval = ("/", termval, right)
        return termval

    def factor(self) -> int:
        """factor ::= NUM | ( expr )"""
        if self._accept("NUM"):
            return int(self.tok.value)
        elif self._accept("LPAREN"):
            exprval = self.expr()
            self._expect("RPAREN")
            return exprval
        else:
            raise SyntaxError("Expected NUMBER or LPAREN")


def main():
    """Main entry."""
    parser = ExpressionEvaluator()
    print(parser.parse("2"))
    print(parser.parse("2 + 3"))
    print(parser.parse("2 + 3 * 4"))
    print(parser.parse("2 + (3 + 4) * 5"))

    parser = ExpressionTreeBuilder()
    print(parser.parse("2"))
    print(parser.parse("2 + 3"))
    print(parser.parse("2 + 3 * 4"))
    print(parser.parse("2 + (3 + 4) * 5"))
    print(parser.parse("2 + 3 + 4"))



if __name__ == "__main__":
    main()
