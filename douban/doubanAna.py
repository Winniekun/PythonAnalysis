'''
@author：KongWeiKun
@file: doubanAna.py
@time: 18-3-6 下午8:03
@contact: 836242657@qq.com
'''
from collections import Counter
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

def plot_more_line(data,name,title,x_roate = 0,y_roate = 0):
    """
    绘制多条折现
    :param data: 
    :param name: 
    :param title: 
    :param x_roate: 
    :param y_roate: 
    :return: 
    """
    stackBar = pyecharts.Line(title)
    label = []
    legend = ['max','min','ave','most']
    maxSizes = []
    minSizes = []
    aveSizes = []
    mostSizes = []
    for row in data:
        label.append(row[0])
        maxSizes.append(row[1]['max'])
        minSizes.append(row[1]['min'])
        aveSizes.append(row[1]['ave'])
        mostSizes.append(row[1]['most'])

    stackBar.add(legend[1],label,minSizes,)
    stackBar.add(legend[2],label,aveSizes,)
    stackBar.add(legend[3],label,mostSizes,mark_line=["average"])
    stackBar.add(legend[0],label,maxSizes,is_datazoom_show=True,is_smooth=True,xaxis_interval=0,xaxis_rotate=x_roate, yaxis_rotate=y_roate)
    stackBar.render('templates/{}.html'.format(name))

def plot_fill_line(data,name,title):
    label = [i[0] for i in data]
    lengend = ['0-10','10-20','20-30','30-40','40-50',
               '50-60','60-70','70-80','80-90','90-100','>100']
    size_0 = [i[1]['0-10'] for i in data]
    size_1 = [i[1]['10-20'] for i in data]
    size_2 = [i[1]['20-30'] for i in data]
    size_3 = [i[1]['30-40'] for i in data]
    size_4 = [i[1]['40-50'] for i in data]
    size_5 = [i[1]['50-60'] for i in data]
    size_6 = [i[1]['60-70'] for i in data]
    size_7 = [i[1]['70-80'] for i in data]
    size_8 = [i[1]['80-90'] for i in data]
    size_9 = [i[1]['90-100'] for i in data]
    size_10 = [i[1]['>100'] for i in data]
    fillLine = pyecharts.Line(title)
    fillLine.add(lengend[0],label,size_0,is_smooth=True,is_fill=True)
    fillLine.add(lengend[1],label,size_1,is_smooth=True,is_fill=True)
    fillLine.add(lengend[2],label,size_2,is_smooth=True,is_fill=True)
    fillLine.add(lengend[3],label,size_3,is_smooth=True,is_fill=True)
    fillLine.add(lengend[4],label,size_4,is_smooth=True,is_fill=True)
    fillLine.add(lengend[5],label,size_5,is_smooth=True,is_fill=True)
    fillLine.add(lengend[6],label,size_6,is_smooth=True,is_fill=True)
    fillLine.add(lengend[7],label,size_7,is_smooth=True,is_fill=True)
    fillLine.add(lengend[8],label,size_8,is_smooth=True,is_fill=True)
    fillLine.add(lengend[9],label,size_9,is_smooth=True,is_fill=True)
    fillLine.add(lengend[10],label,size_10,is_smooth=True,is_fill=True)
    fillLine.render('templates/{}.html'.format(name))

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
    yearGrade = dict()
    yearGradeInfo = dict()
    for row in reader:
        if row[7] != '0': #去除无评价的评分项
            year = "".join(re.findall('.*?(\d{4})/\d', row[3])) #去除格式不正确的年份
            if year and 1000 < int(year) < 2018 :
                # print("{}年某个评分为{}".format("".join(year),row[7]))
                year = int(year)
                yearGrade.setdefault(year,[])
                yearGrade[year].append(float(row[7]))
    # print(yearGrade.keys())

    for k,v in yearGrade.items():
        info = {
            'max':max(v),
            'min':min(v),
            'ave':(sum(v)/len(v)),
            'most': Counter(v).most_common(1)[0][0]
        }
        # print("{}年最高分{}最低分{}平均分{}".format(k,max(v),min(v),(sum(v)/len(v))))
        yearGradeInfo.setdefault(k,info)
    sortInfo = sorted(yearGradeInfo.items(),key=lambda x:x[0],reverse=False)
    return sortInfo

def yearPrice(data):
    reader = csv.reader(open(data))
    next(reader)
    unitprice = dict()
    finaprice = dict()
    for row in reader:
        if re.match('[\u4E00-\u9FA5]+',row[0]):#匹配出中文 其他国家的书籍价钱需要汇率转化 直接去掉
            if re.match('\d+\.',row[5]): #匹配出正常间隔
                price = re.sub(',','',row[5]) #过千的价格转化
                year = "".join(re.findall('.*?(\d{4})/\d', row[3]))  # 去除格式不正确的年份
                if year and 1000 < int(year) < 2018:
                    unitprice.setdefault(int(year),[])
                    unitprice[int(year)].append(float(price))
    # print(unitprice)

    for k,v in unitprice.items():
        zero = [num for num in v if 0<num<10]
        ten = [num for num in v if 10<num<20]
        twenty = [num for num in v if 20 < num < 30]
        thirty = [num for num in v if 30 < num < 40]
        forty = [num for num in v if 40 < num < 50]
        fifty = [num for num in v if 50 < num < 60]
        sixty = [num for num in v if 60 < num < 70]
        seventy = [num for num in v if 70 < num < 80]
        eighty = [num for num in v if 80 < num < 90]
        ninety = [num for num in v if 90 < num < 100]
        hundred = [num for num in v if 100 < num ]
        info = {
            '0-10': len(zero),
            '10-20': len(ten),
            '20-30': len(twenty),
            '30-40': len(thirty),
            '40-50': len(forty),
            '50-60': len(fifty),
            '60-70': len(sixty),
            '70-80': len(seventy),
            '80-90': len(eighty),
            '90-100': len(ninety),
            '>100': len(hundred)
        }
        finaprice.setdefault(k,info)
    # print(finaprice)
    sortArray = sorted(finaprice.items(),key=lambda x:(x[0]),reverse=False)

    # print(sortArray)
    return sortArray

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

def publishStar(data):
    reader = csv.reader(open(data))
    next(reader)
    publishGrade = dict()
    publisGradeInfo = dict()
    for row in reader:
        if row[7] != '0':  # 去除无评价的评分项
            if row[2] != 'None':
                publishGrade.setdefault(row[2],[])
                publishGrade[row[2]].append(float(row[7]))
    for k,v in publishGrade.items():
        info = {
            'max':max(v),
            'min':min(v),
            'ave':(sum(v)/len(v)),
            'most':Counter(v).most_common(1)[0][0]
        }
        # print("{}出版社最高分{}最低分{}平均分{}".format(k,max(v),min(v),(sum(v)/len(v))))
        publisGradeInfo.setdefault(k,info)
    sortInfo = sorted(publisGradeInfo.items(),key=lambda x:x[0],reverse=True)[:100]
    # print(sortInfo)
    return sortInfo

def authorNum(data):
    """
    作者统计
    :param data: 
    :return: 
    """
    reader = csv.reader(open(data))
    next(reader)
    author = {}
    for row in reader:
        if row[1] != 'None':
            author[row[1]] = author.get(row[1],0)+1
    authorSort = sorted(author.items(),key=lambda x:x[1],reverse=True)[:30]
    return authorSort

def authorStar(data):
    reader = csv.reader(open(data))
    next(reader)
    publishGrade = dict()
    publisGradeInfo = dict()
    for row in reader:
        if row[7] != '0':  # 去除无评价的评分项
            if row[1] != 'None':
                publishGrade.setdefault(row[1], [])
                publishGrade[row[1]].append(float(row[7]))
    for k, v in publishGrade.items():
        info = {
            'max': max(v),
            'min': min(v),
            'ave': (sum(v) / len(v)),
            'most': Counter(v).most_common(1)[0][0]
        }
        # print("{}年最高分{}最低分{}平均分{}".format(k,max(v),min(v),(sum(v)/len(v))))
        publisGradeInfo.setdefault(k, info)
    sortInfo = sorted(publisGradeInfo.items(), key=lambda x: x[1]['most'], reverse=True)[:50]
    # print(sortInfo)
    return sortInfo

if __name__ == '__main__':
    data_path = 'data/douban_book.csv'
    # yearcou = yearNum(data_path)
    # plot_line(yearcou,'yearLine','每年出版书籍数量')
    # yearStar(data_path)
    # pricecou = priceNum(data_path)
    # plot_bar(pricecou,'priceBar','各种价格范围的书籍统计')
    # publish = publishNum(data_path)
    # plot_bar(publish,'publish','出版社书籍数量',x_roate=30)
    # author = authorNum(data_path)
    # plot_bar(author,'author','作者书籍数量',x_roate=90)
    s = yearStar(data_path)
    plot_more_line(s,'yearstar','书籍评分与年份',x_roate=90)
    # s = yearPrice(data_path)
    # plot_fill_line(s,'yearprice','')
    # publishGrade = publishStar(data_path)
    # plot_more_line(publishGrade,'publishgrade','出版社出版的书籍的质量',x_roate=60)
    # authorStar(data_path)