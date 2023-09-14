from shlex import join
from imageio import imread
from collections import Counter
import requests
import re
import json
import csv
import jieba
import wordcloud
f =open('danmu.csv', encoding='utf-8-sig')
line =f.read().splitlines()

counter = Counter(line)
pai = counter.most_common(20)
for value,count in pai:
    print(value,count)



