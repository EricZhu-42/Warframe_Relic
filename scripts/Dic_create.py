"用于创建规定格式的查询表json文件"

import json,requests

url = 'https://raw.githubusercontent.com/Richasy/WFA_Lexicon/master/WF_Sale.json'
r = requests.get(url)

dic = {}
for item in r.json():
    va = item['search']
    ke = item['zh']
    dic[ke]=va

with open('D:\\Desk\\Coding\\Py\\Warframe_Relic\\json\\Dic.json','w+',encoding='utf-8') as f:
    f.write(json.dumps(dic,ensure_ascii=False))
