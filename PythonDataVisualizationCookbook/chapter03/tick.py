'''
@author：KongWeiKun
@file: tick.py
@time: 18-3-18 下午8:16
@contact: 836242657@qq.com
'''
import pylab
import numpy as np

ax = pylab.gca()
ax.locator_params(tight=True,nbins=10)
ax.plot(np.random.normal(10,.1,100))
pylab.show()