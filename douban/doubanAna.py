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

data_path = 'data/douban_book.csv'


def yearNum(data):
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
    reader = csv.reader(open(data))
    next(reader)
    arr = []
    yearGrade = {}
    for row in reader:
        if row[3]:
            year = re.findall('.*?(\d{4})/\d',row[3])
            if len(year) == 1:
                yearGrade.setdefault(year,[])


def plot_line(data,name,title):
    label = []
    sizes = []
    for row in data:
        label.append(row[0])
        sizes.append(row[1])
    line = pyecharts.Line(title=title)
    line.add('',label,sizes,mark_line=['max'])
    line.render('templates/{}.html'.format(name))

if __name__ == '__main__':
    # yearcou = yearNum(data_path)
    # plot_line(yearcou,'yearBar','每年出版书籍数量')
    yearStar(data_path)