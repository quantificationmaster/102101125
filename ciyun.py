from shlex import join
from imageio import imread
from collections import Counter
import jieba
import wordcloud


f =open('danmu.csv', encoding='utf-8-sig')
txt =f.read()
string =' '.join(jieba.lcut(txt))

w = wordcloud.WordCloud(
    width=600,
    height=400,
    background_color='white',
    font_path='STLITI.TTF',
    scale= 5
)
w.generate(string)
w.to_file('ciyuntu.png')
