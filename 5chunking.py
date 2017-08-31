# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 19:37:44 2017

@author: jagan reddy
"""

import nltk

with open('3afterstemming.txt', 'r') as rf:
    with open('5chunk.txt', 'w') as wf:
        for w in rf:
            text = nltk.word_tokenize(w)
            tagged = nltk.pos_tag(text)
            
            chunkGram = r"""Chunk: {<.*>+}
                                   }<VB|IN|DT|TO>+{"""
            
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            #string = ''.join(chunked)
            wf.write(str(chunked))