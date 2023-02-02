#!/usr/bin/env python3
"""Example of a priority queue."""
import heapq
from typing import Any

class Item:
    """Item class representing priority queue items."""

    def __init__(self, name:str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Item({self.name!r})"
    

class PriorityQueue:
    """PriorityQueue class."""

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item:Item, priority) -> None:
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self) -> Item:
        return heapq.heappop(self._queue)[-1]


def main():
    """Main entry."""
    pqueue = PriorityQueue()
    pqueue.push(Item("foo"), 1)
    pqueue.push(Item("bar"), 5)
    pqueue.push(Item("spam"), 4)
    pqueue.push(Item("grok"), 1)

    print(f"Should be bar: {pqueue.pop()}")
    print(f"Should be spam: {pqueue.pop()}")
    print(f"Should be foo: {pqueue.pop()}")
    print(f"Should be grok: {pqueue.pop()}")


if __name__ == "__main__":
    main()
