#!/usr/bin/env python
"""reducer.py"""

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    word_counts = []

    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            word_counts.append((current_word, total_count))
        except ValueError:
            pass

    # Sort by count descending
    word_counts.sort(key=lambda x: x[1], reverse=True)

    # Print only top 3
    for word, count in word_counts[:3]:
        print(f"{word}{separator}{count}")

if __name__ == "__main__":
    main()
