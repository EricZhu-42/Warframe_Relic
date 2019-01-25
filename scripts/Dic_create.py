"用于创建规定格式的查询表json文件"

import sys,os
currentpath = sys.path[0]
basic_path = currentpath + "\\basic"
sys.path.append(basic_path)

import config
import json,requests

url = 'https://raw.githubusercontent.com/Richasy/WFA_Lexicon/master/WF_Sale.json'
r = requests.get(url) #获取最新Sales词库

dic = {}
for item in r.json():
    va = item['search']
    ke = item['zh']
    dic[ke]=va

with open(config.json_path + '\\Dic.json','w+',encoding='utf-8') as f:
    f.write(json.dumps(dic,ensure_ascii=False,indent=4))

#创建并保存字典