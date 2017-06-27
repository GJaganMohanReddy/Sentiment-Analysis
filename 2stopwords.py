# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 11:11:16 2017

@author: jagan reddy
"""

from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))
filtered_sentence = []
with open('1tokenized.txt', 'r') as rf:
    with open('2filteredstopwords.txt', 'w') as wf:
        for word in rf:
                if word not in stop_words:
                    filtered_sentence.append(word)
        
        string = ''.join(filtered_sentence)
        wf.write(string)