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
from wordcloud import WordCloud
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
picture=np.array(Image.open(os.path.join(d,'a.jpg')))
wordcloud=WordCloud(background_color='#F0F8FF',max_words=1000,max_font_size=300,font_path=font,
                    mask=picture,random_state=42).generate(wordlist_space_split)
plt.imshow(wordcloud)            # 以图片的形式显示词云
plt.axis('off')                     # 关闭坐标轴
plt.show()

wordcloud.to_file(os.path.join(d,'1.png'))