'''
@author：KongWeiKun
@file: base.py
@time: 18-3-18 下午5:08
@contact: 836242657@qq.com
'''
import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [5,4,3,2]

plt.figure()
#直线
plt.subplot(231)
plt.plot(x,y)
#柱状
plt.subplot(232)
plt.bar(x,y)
#x y 倒置
plt.subplot(233)
plt.barh(x,y)
# 堆叠 设置红色
plt.subplot(234)
plt.bar(x,y)
y1 = [7,8,5,3]
plt.bar(x,y1,bottom=y,color='r')
# 箱图
plt.subplot(235)
plt.boxplot(x,y)
#散点图
plt.subplot(236)
plt.scatter(x,y)

plt.show()
