'''
@author：KongWeiKun
@file: wechat-ana.py
@time: 18-4-2 下午4:53
@contact: kongwiki@163.com
'''
import json
import re
filename = 'WechatLog.json'
wechatData = {'content':[]}
with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        wechatSinData = json.loads(line)
        wechatData['content'].append(wechatSinData)
f.close()
i = 0
presentCount = dict()
for v in wechatData['content']:
    redPresent = re.compile('://(.*?)/')
    redPresents = redPresent.findall(v['content'])
    if redPresents:
        i += 1
        # print(i,redPresents[0])
        presentCount[(redPresents[0])] = presentCount.get((redPresents[0]),0)+1
print(presentCount.keys())



