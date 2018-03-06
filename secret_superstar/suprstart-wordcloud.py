'''
@author：KongWeiKun
@file: suprstart-wordcloud.py
@time: 18-2-12 下午11:25
@contact: 836242657@qq.com
'''
import os
import jieba
import PIL.Image as Image
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt

def content(name):
    with open('{}.txt'.format(name),'rb') as f:
        text = f.read()
        return text

text = content(name='10')
wordlist = jieba.cut(text,cut_all=False)
#cut_all True 为全局模式 False为精准模式
wordlist_space_split = ' '.join(wordlist)
d=os.path.dirname(__file__)

font='font/simsun.ttc'
backgroundImage = plt.imread('a.jpg')
print('加载图片成功！')
#设置词云样式
stopwords = STOPWORDS.copy()
stopwords.add("哈哈")
stopwords.add("印度")
stopwords.add("电影")
stopwords.add("阿米尔")
stopwords.add("还是")
stopwords.add("就是")#可以加多个屏蔽词
wordcloud = WordCloud(
    width=1024,
    height=768,
    background_color='white',  # 设置背景颜色
    mask=backgroundImage,  # 设置背景图片
    font_path=font,  # 设置中文字体，若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
    max_words=300,  # 设置最大现实的字数
    stopwords=stopwords,  # 设置停用词
    max_font_size=400,  # 设置字体最大值
    random_state=50,  # 设置有多少种随机生成状态，即有多少种配色方案
).generate(wordlist_space_split)
plt.imshow(wordcloud)            # 以图片的形式显示词云
plt.axis('off')                     # 关闭坐标轴
plt.show()

wordcloud.to_file(os.path.join(d,'1.png'))