#!/usr/bin/env python
"""mapper.py"""

import sys
import string
import unicodedata

def clean_word(word):
    # normalize to NFKD form and encode to ASCII bytes, ignore non-ASCII
    word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('ascii')
    # remove punctuation and convert to lowercase
    word = word.strip(string.punctuation).lower()
    return word

def read_input(file):
    for line in file:
        yield line.split()

def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            word = clean_word(word)
            if word:
                print('%s%s%d' % (word, separator, 1))

if __name__ == "__main__":
    main()
