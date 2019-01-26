'用于生成本地的价格字典'
import sys,os,json,threading
currentpath = sys.path[0]
basic_path = currentpath + "\\basic"
sys.path.append(basic_path)

import config,search

with open(config.json_path + '\\relic_dic.json','r',encoding='utf-8') as relic_dic_file:
    relic_dic = json.loads(relic_dic_file.read())

sales = {}
count = 0
length = len(relic_dic)

def valid_print(name,query): #有效情况下
    global sales,count
    item_dict = search.search_in_wm(query)
    item_dict['ducats'] = str(item_dict['ducats'])
    item_dict['advicePrice'] = str(item_dict['advicePrice'])
    sales[name]=item_dict
    count += 1
    print(str(count) + ' of ' + str(length))
'''
threadlist = []
for key in relic_dic:
    t = threading.Thread(target=valid_print, args=(key,relic_dic[key],))
    threadlist.append(t)
for t in threadlist:
    t.start()
for t in threadlist:
    t.join()
'''

for key in relic_dic:
    valid_print(key,relic_dic[key])

with open(config.json_path + '\\local_sales.json','w+',encoding='utf-8') as local_sales_file:
    local_sales_file.write(json.dumps(sales,indent=4,ensure_ascii=False))