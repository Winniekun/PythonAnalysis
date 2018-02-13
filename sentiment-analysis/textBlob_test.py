'''
@author：KongWeiKun
@file: textBlob_text.py
@time: 18-2-12 上午9:20
@contact: 836242657@qq.com
'''
from textblob import TextBlob

text = '''
I am happy today. I feel sad today.
'''

blob = TextBlob(text)
print(blob.tags)
# print(blob.noun_phrases)
print(blob.sentences)
print(blob.sentences[0].sentiment)
print(blob.sentences[1].sentiment)
print(blob.sentiment)