#!/usr/bin/env python3
"""
Created on 2023-05-18 (Thu) 23:57:36

WordCloud test

@author: I.Azuma
"""
#%%
import itertools
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#%%
text = WordCloud.__doc__
wordcloud = WordCloud().generate(text)
#wordcloud.to_file("word_cloud_result.png")

plt.imshow(wordcloud)

#%%
txt = open("C:/github/tabelog_handling/review_analysis/dev/result/review.txt",encoding='utf-8').read().splitlines()[5:-10]
review = ""
for r in txt:
    review = review + " " + str(r)
print(review)

#%%
import MeCab
from wordcloud import WordCloud
import matplotlib.pyplot as plt
tagger = MeCab.Tagger()
tagger.parse('')
node = tagger.parseToNode(review)
# 名詞のみ取り出す
word_list = []
while node:
    word_type = node.feature.split(',')
    if word_type[0] in ["名詞"]:
        # さらに絞り込み
        if word_type[1] in ["一般", "固有名詞"]:
            word_list.append(node.surface)
    node = node.next
# word_listを文字列に変換する
word_chain = ' '.join(word_list)

#%%
# Display WordCloud
font_path_gothic = 'C:/github/tabelog_handling/_utils/ipaexg.ttf'
result = WordCloud(width=800, height=600, background_color='white', font_path=font_path_gothic).generate(word_chain)
plt.figure(figsize=(12,10))
plt.imshow(result)
plt.axis('off')
plt.show()
