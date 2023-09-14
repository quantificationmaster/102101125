from shlex import join
from imageio import imread
from collections import Counter
import jieba
import wordcloud
f =open('danmu.csv', encoding='utf-8-sig')
line =f.read().splitlines()
print(Counter(line).most_common(20))
