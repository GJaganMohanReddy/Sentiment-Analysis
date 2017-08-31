# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 11:31:53 2017

@author: jagan reddy
"""
import nltk

with open('3afterstemming.txt', 'r') as rf:
    with open('4postagged.txt', 'w') as wf:
        for line in rf:
            text = nltk.word_tokenize(line)
        #print(nltk.pos_tag(text))
        wf.write(str(nltk.pos_tag(text)))