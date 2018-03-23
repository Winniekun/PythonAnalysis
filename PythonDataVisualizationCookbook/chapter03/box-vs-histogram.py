'''
@author：KongWeiKun
@file: box-vs-histogram.py
@time: 18-3-18 下午5:20
@contact: 836242657@qq.com
'''
from pylab import *
import matplotlib.pyplot as plt
#箱线图讲解
# 箱体延伸出来的箱须来展示数据集合的整个范围
# 箱体和箱须主要用于表现一个或多个数据集合中数据的变化
# 箱线图可呈现5中数据
# 最小值 ： 数据集合中的最小值
# 第二四分位数 ： 其以下为数据集合中较低的25%数据
# 中值 ： 数据集合的中值
# 第三四分位数 ： 其以上为数据集合中较高的25%数据
# 最大值 ： 给定数据集合的最大值
dataset = [113,115,119,121,124,
           124,125,126,126,126,
           127,127,128,129,130,
           130,131,132,133,136]
# subplot(121)
# boxplot(dataset,vert=False)#倒置
#
# subplot(122)
# hist(dataset)
plt.boxplot(dataset)
plt.show()
plt.savefig('box.jpg')