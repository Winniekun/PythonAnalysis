'''
@author：KongWeiKun
@file: snownlp_test.py
@time: 18-2-12 上午9:31
@contact: 836242657@qq.com
'''
from snownlp import SnowNLP

text = '''
I am happy today. I feel sad today.
'''
s= SnowNLP(text)
print(s.sentences)