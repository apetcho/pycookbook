#!/usr/bin/env python3
"""Determine the most common words in a list."""
from collections import Counter


def main():
    """Main entry point."""
    words = [
        "look", "into", "my", "eyes", "look", "into", "my", "eyes",
        "the", "eyes", "the", "eyes", "the", "eyes", "not", "around",
        "the", "eyes", "look", "around", "the", "eyes", "look", "into",
        "my", "eyes", "you're", "under"
    ]
    word_counts = Counter(words)
    top_three = word_counts.most_common(3)
    print(top_three)

    # -*- Example of merging in more words -*-
    morewords = ["why", "are", "you", "not", "looking", "in", "my", "eyes"]
    word_counts.update(morewords)
    print(word_counts.most_common(3))


if __name__ == "__main__":
    main()
