'''
@author：KongWeiKun
@file: chapter02.py
@time: 18-2-6 下午5:30
@contact: 836242657@qq.com
'''
'''
来自bit.ly的1.usa.gov的数据
'''
import json
import time
import pylab

path = './data/usagov_bitly_data2012-03-16-1331923249.txt'
# with open(path) as f:
#     reader = f.readlines()
#     print(reader)
records = [json.loads(line) for line in open(path)]
# # print(records)
# time_zones = [rec['tz'] for rec in records if 'tz' in rec] #部分记录没有tz字段
# print(time_zones[:10])
# #对时区进行计数
# def get_counts(sequence):
#     """
#     标准Python库
#     :param squence:
#     :return: counts
#     """
#     counts = {}
#     for x in sequence:
#         if x in counts:
#             counts[x] += 1
#         else:
#             counts[x] = 1
#
#     return counts
#
# from collections import defaultdict
# def get_counts2(sequence):
#     """
#     纯Python精简版
#     :param sequence:
#     :return:
#     """
#     counts = defaultdict(int) # 所有的均值均会被初始化为0
#     for x in sequence:
#         counts[x] += 1
#     return counts
#
# def top_counts(count_dict, n):
#     """
#     获取前n位的时区及其计数值
#     :param count_dict:
#     :param n:
#     :return:
#     """
#     start = time.time()
#     values_key_pairs = [(count,tz) for tz,count in count_dict.items()]
#     values_key_pairs.sort()
#     end = time.time()
#     total = end - start
#     return values_key_pairs[-n:],total
#
# def top_counts2(count_dict, n):
#     """
#     获取前n位的时区及其计数值
#     :param count_dict:
#     :param n:
#     :return:
#     """
#     start = time.time()
#     values_key_pairs = sorted(count_dict.items(),key=lambda x:x[1], reverse=True)
#     end =  time.time()
#     total = end - start
#     return values_key_pairs[:n] ,total
#
# counts = get_counts(time_zones)
# print(counts['America/New_York'])
# print(len(time_zones))
# print(top_counts(counts,10))
# print(top_counts2(counts,10))
# #python标准库中collection.counter类 可使该任务更加轻松
# from collections import Counter
# counts = Counter(time_zones)
# print(counts.most_common(10))

#利用pandas对时区进行时区行计数
from pandas import DataFrame,Series
import pandas as pd ; import numpy as np
frame = DataFrame(records)
# print(frame)
# print(frame['tz'][:10])
tz_counts = frame['tz'].value_counts()
# print(tz_counts[:10])
clean_tz = frame['tz'].fillna('Missing')#缺失的时区填写为ＮＡ　
clean_tz[clean_tz == ''] = 'Unknow'#未知的空字符
tz_counts = clean_tz.value_counts()
# print(tz_counts[:10])
# tz_counts[:10].plot(kind='barh',rot=0)
# results = Series([x.split()[0] for x in frame.a.dropna()])
# print(results.value_counts()[:8])
cframe = frame[frame.a.notnull()] #移除缺失项
operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
print(operating_system[:5])
#根据时区和得到的操作系统列表对数据进行分组
by_tz_os = cframe.groupby(['tz',operating_system])
#通过size对分组结果进行计数并用unstack 进行重塑
agg_counts = by_tz_os.size().unstack().fillna(0)
print(agg_counts[:10])
indexer = agg_counts.sum(1).argsort()
print(indexer[:10])
print(agg_counts.take(indexer)[-10:])