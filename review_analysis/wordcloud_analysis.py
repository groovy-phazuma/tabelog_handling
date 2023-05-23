#!/usr/bin/env python3
"""
Created on 2023-05-24 (Wed) 00:11:07

WordCloud analysis

@author: I.Azuma
"""
#%%
import MeCab
import itertools
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#%%
class WordCloudAnalysis():
    def __init__(self):
        self.review = None
    
    def load_review(self,path="C:/github/tabelog_handling/review_analysis/dev/result/review.txt"):
        txt = open(path,encoding='utf-8').read().splitlines()
        review = ""
        for r in txt:
            review = review + " " + str(r)
        self.review = review
    
    def morphological_analysis(self):
        tagger = MeCab.Tagger()
        tagger.parse('')
        node = tagger.parseToNode(self.review)
        # extract nouns only
        word_list = []
        while node:
            word_type = node.feature.split(',')
            if word_type[0] in ["名詞"]:
                # further filtering
                if word_type[1] in ["一般", "固有名詞"]:
                    word_list.append(node.surface)
            node = node.next
        self.word_chain = ' '.join(word_list)
    
    def display(self):
        # Display WordCloud
        font_path_gothic = 'C:/github/tabelog_handling/_utils/ipaexg.ttf'
        result = WordCloud(width=800, height=600, background_color='white', font_path=font_path_gothic).generate(self.word_chain)
        plt.figure(figsize=(12,10))
        plt.imshow(result)
        plt.axis('off')
        plt.show()

