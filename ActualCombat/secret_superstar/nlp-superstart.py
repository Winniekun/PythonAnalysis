'''
@author：KongWeiKun
@file: nlp-superstart.py
@time: 18-2-13 下午1:56
@contact: 836242657@qq.com
'''

import numpy as np
from snownlp import SnowNLP
import matplotlib.pyplot as plt

comment = []
with open('commment.txt','r',encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        if row not in comment:
            comment.append(row.strip('\n'))

def snowanalysis(self):
    sentimentslist = []
    for li in self:
        print(li)
        s = SnowNLP(li)
        print(s.sentiments)
        sentimentslist.append(s.sentiments)
    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01))
    plt.show()
snowanalysis(comment)