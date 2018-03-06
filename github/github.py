'''
@author：KongWeiKun
@file: github.py
@time: 18-2-19 下午12:09
@contact: 836242657@qq.com
'''
'''
爬取github 分析
'''
import re
import os
import json
import math
import jieba
import pandas as pd
from pyecharts import Bar
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from pypinyin import lazy_pinyin


data_path = 'data/result.csv'

def plot_bar(data,name):
    """
    graph
    :return: 
    """
    # print(df[:1])
    data_list = list(data[name]) #转化为列表方便分析
    # print(data_list[:10])
    print(len(data_list))
    print('max {} = {}'.format(name,max(data_list)))
    labels = ['00~00','01-10','11-50','51-100','101-500','501-1000','>1000']
    sizes = []
    sizes.append(len([count for count in data_list if count == 0]))
    sizes.append(len([count for count in data_list if 10>= count> 0]))
    sizes.append(len([count for count in data_list if 50>= count > 10]))
    sizes.append(len([count for count in data_list if 100>= count > 50]))
    sizes.append(len([count for count in data_list if 500>= count > 100]))
    sizes.append(len([count for count in data_list if 1000>= count > 500]))
    sizes.append(len([count for count in data_list if count > 1000]))
    bar = Bar(name,'by KongWiKi')
    bar.add('',labels,sizes,is_lable_show=True,mark_line=['max','min'])
    bar.render('templates/{}.html'.format(name))

def plot_positon():
    """
    graph position
    :return: 
    """
    df = pd.read_csv(data_path)
    data_list = list(df['position'])
    data_pos = [pos for pos in data_list if str(pos) != 'nan']
    #中文转拼音
    places = []
    for row in data_pos:
        place = ''.join(lazy_pinyin(row))
        places.append(place)

    wordcloud = WordCloud(background_color='white',
                          width=1024,
                          height=768,
                          margin=2,
                          max_font_size=300).generate(str(places)) #转为str防止报错
    wordcloud.to_file('templates/github-places.jpg')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


def main():
    df = pd.read_csv(data_path)
    features = ['stars','followers','following','repositories','contributions']
    for i in features:
        print(i)
        plot_bar(df,i)

    plot_positon()

if __name__ == '__main__':
    main()