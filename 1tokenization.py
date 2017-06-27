# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from nltk.tokenize import word_tokenize

with open('train.txt', 'r') as rf:
    with open('1tokenized.txt', 'w') as wf:
        for line in rf:
            string = ' '.join(word_tokenize(line))
            wf.write(string)

        