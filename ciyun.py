from shlex import join
from imageio import imread
from collections import Counter
import jieba
import wordcloud
import imageio
mk =imageio.imread("jing.png")


f =open('danmu.csv', encoding='utf-8-sig')
txt =f.read()
string =' '.join(jieba.lcut(txt))

w = wordcloud.WordCloud(
    width=800,
    height=600,
    background_color='white',
    font_path='STLITI.TTF',
    scale= 5,
    mask =mk,
    contour_width=5,
    contour_color='red'
)
w.generate(string)
w.to_file('ciyuntu.png')
