'''
@author：KongWeiKun
@file: superstar.py
@time: 18-2-12 下午1:12
@contact: 836242657@qq.com
'''
import pandas as pd
import os

import time
from pyecharts import Bar,Grid,Pie,Line
data = 'superstar.csv'
superstart = pd.read_csv(data)
index = superstart['time']
# print(superstart.isnull().sum())  #缺省检测
#把时间数据分割成年 月 日新特征
superstart['year'] = pd.DatetimeIndex(superstart['time']).year
superstart['month'] = pd.DatetimeIndex(superstart['time']).month
superstart['day'] = pd.DatetimeIndex(superstart['time']).day
superstart['hour'] = pd.DatetimeIndex(superstart['time']).hour
superstart = superstart.drop('time',axis=1)#去除原有的特征值

def bar_plot(row,title,name):
    index = [str(i) for i in superstart.groupby(row).count().index]
    values = [int(i) for i in superstart.groupby(row).count().username]
    bar = Bar(title=title, title_pos='center', width=1050, height=500)
    bar.add('', index, values, is_datazoom_show=True, xaxis_rotate=60, xaxis_interval=5,
                 label_emphasis_textcolor='black')
    bar.render('templates/{}.html'.format(name))

def pie_plot(row,name,title):
    index = [str(i) for i in superstart.groupby(row).count().index]
    values = [int(i) for i in superstart.groupby(row).count().username]
    pie = Pie(title=title, title_pos="55%")
    pie.add('',index,values,radius=[40,65],center=[71,50],legend_pos="92%",legend_orient='vertical',is_label_show=True)
    pie.render('templates/{}.html'.format(name))

def line_plot(row,name,title):
    index = [str(i) for i in superstart.groupby(row).count().index]
    values = [int(i) for i in superstart.groupby(row).count().username]
    line = Line(title)
    line.add('',index,values,is_smooth=True,mark_point=['average'],mark_line=['max','average'])
    line.render('templates/{}.html'.format(name))


pie_plot('year','year-pie',title='17-18年每年各有多少短评')
# line_plot('hour','hour-line',title='每小时发布短评量')


# bar_plot(row='year',title='年',name='test')
# pie_plot(row='year',title='年',name='pie')

#
# index2 = [str(i) for i in superstart.groupby('day').count().index]
# day_values = [int(i) for i in superstart.groupby('day').count().username]
#
#
# index3 = [str(i) for i in superstart.groupby('hour').count().index]
# hour_values3 = [int(i) for i in superstart.groupby('hour').count().username]

# index = [str(i) for i in superstart.groupby('star').count().index]
# print(index)
# values = [int(i) for i in superstart.groupby('star').count().username]
#
# bar = Bar(title='神秘巨星',title_pos='center',width=1050,height=500)
# bar.add('',index,values,legend_pos="90%",is_label_show=True,mark_line=['min','max'])
#
# pie = Pie("",title_pos="55%")
# pie.add('',index,values,radius=[40,65],center=[71,50],legend_pos="92%",legend_orient='vertical',is_label_show=True)
#
# grid = Grid()
# grid.add(bar,grid_right="55%")
# grid.add(pie,grid_left="60%")
# grid.render('templates/star.html')





# bar_plot('神秘巨星',superstart)

