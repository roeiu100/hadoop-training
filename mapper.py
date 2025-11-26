#!/usr/bin/env python
"""mapper.py"""

import sys

def read_input(file):
    for line in file:
        yield line.split()

def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            # Remove trailing commas and periods, convert to lowercase
            word_clean = word.rstrip('.,').lower()
            print('%s%s%d' % (word_clean, separator, 1))

if __name__ == "__main__":
    main()

