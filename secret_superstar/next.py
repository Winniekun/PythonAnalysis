'''
@author：KongWeiKun
@file: next.py
@time: 18-2-12 下午9:23
@contact: 836242657@qq.com
'''
import json
import csv

data = 'superstar.csv'
res = {}

def write_file(content,name):
    with open(name+'.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)  + '\n')#写入文件,并且确定为汉字
        f.close()

with open(data) as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row[3] == '10':
            print(row[5])
            write_file(row[5],'10')
        elif row[3] == '20':
            write_file(row[5],'20')
        elif row[3] == '30':
            write_file(row[5], '30')
        elif row[3] == '40':
            write_file(row[5], '40')
        else :
            write_file(row[5], '50')
