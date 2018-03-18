'''
@author：KongWeiKun
@file: sin-cos.py
@time: 18-3-18 下午8:05
@contact: 836242657@qq.com
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi,np.pi,256,endpoint=True)
y = np.cos(x)
y1 = np.sin(x)
plt.plot(x,y)
plt.plot(x,y1)

plt.show()