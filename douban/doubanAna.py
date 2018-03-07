'''
@author：KongWeiKun
@file: doubanAna.py
@time: 18-3-6 下午8:03
@contact: 836242657@qq.com
'''
import pandas as pd
import numpy as np
import pyecharts
import csv
import re



def plot_line(data,name,title):
    """
    折线图
    :param data: 
    :param name: 
    :param title: 
    :return: 
    """
    label = []
    sizes = []
    for row in data:
        label.append(row[0])
        sizes.append(row[1])
    line = pyecharts.Line(title=title)
    line.add('',label,sizes,mark_line=['max'])
    line.render('templates/{}.html'.format(name))

def plot_bar(data,name,title,x_roate=0,y_roate=0):
    """
    柱状图
    :param data: 
    :param name: 
    :param title: 
    :return: 
    """
    bar = pyecharts.Bar(title)
    label = []
    sizes = []
    for row in data:
        label.append(row[0])
        sizes.append(row[1])

    bar.add('',label,sizes,xaxis_interval=0,xaxis_rotate=x_roate, yaxis_rotate=y_roate)
    bar.render('templates/{}.html'.format(name))


def yearNum(data):
    """
    每年出版书籍数量
    :param data: 
    :return: 
    """
    reader = csv.reader(open(data))
    next(reader)
    arr = []
    yearcont = dict()
    for row in reader:
        if row[3]:
            year = re.findall('.*?(\d{4})/\d',row[3])
            if len(year) == 1:
                arr.append("".join(year))
    sortArr = sorted(arr,reverse=False)
    for num in sortArr:
        yearcont[num] = yearcont.get(num,0)+1
    for k in list(yearcont.keys()):
        if int(k) > 2018 or int(k) <1000:
            del yearcont[k]
    sortYear = sorted(yearcont.items(),reverse=False)
    return sortYear

def yearStar(data):
    """
    每年出版书籍的星级
    :param data: 数据路径
    :return: 
    """
    reader = csv.reader(open(data))
    next(reader)
    arr = []
    yearGrade = {}
    for row in reader:
        if row[3]:
            year = re.findall('.*?(\d{4})/\d',row[3])
            if len(year) == 1:
                yearGrade.setdefault(year,[])

def priceNum(data):
    """
    书籍的价格统计
    :param data: 
    :return: 
    """
    reader = csv.reader(open(data))
    next(reader)
    countprice = {}
    for row in reader:
        if re.match('[\u4E00-\u9FA5]+',row[0]):#匹配出中文
            if re.match('\d+\.',row[5]): #匹配出正常间隔
                price = re.sub(',','',row[5]) #过千的价格转化
                countprice[float(row[5])] = countprice.get(float(row[5]),0)+1
    arrcountprice = sorted(countprice.items(),reverse=False)
    # print(arrcountprice)
    return arrcountprice

def publishNum(data):
    """
    出版商统计
    :return: publishSort 列表形式
    """
    reader = csv.reader(open(data))
    next(reader)
    publish = {}
    for row in reader:
        if row[2] != 'None':
            publish[row[2]] = publish.get(row[2],0)+1
    publishSort = sorted(publish.items(),key=lambda x:x[1],reverse=True)[:30]
    # print(publishSort)
    return publishSort

def authorNum(data):
    reader = csv.reader(open(data))
    next(reader)
    author = {}
    for row in reader:
        if row[1] != 'None':
            author[row[1]] = author.get(row[1],0)+1
    authorSort = sorted(author.items(),key=lambda x:x[1],reverse=True)[:30]
    return authorSort

if __name__ == '__main__':
    data_path = 'data/douban_book.csv'
    # yearcou = yearNum(data_path)
    # plot_line(yearcou,'yearLine','每年出版书籍数量')
    # yearStar(data_path)
    # pricecou = priceNum(data_path)
    # plot_bar(pricecou,'priceBar','各种价格范围的书籍统计')
    # publish = publishNum(data_path)
    # plot_bar(publish,'publish','出版社书籍数量',x_roate=30)
    author = authorNum(data_path)
    plot_bar(author,'author','作者书籍数量',x_roate=90)
