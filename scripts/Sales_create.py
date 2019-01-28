"用于创建规定格式的查询表json文件"

import sys,os,multiprocessing,json
currentpath = sys.path[0]
basic_path = currentpath + "\\basic"
sys.path.append(basic_path)

import config, search
import  requests 

url = 'https://raw.githubusercontent.com/Richasy/WFA_Lexicon/master/WF_Sale.json'
r = requests.get(url) #获取最新Sales词库

full_dic = {}
for item in r.json():
    va = item['search']
    ke = item['zh']
    full_dic[ke]=va

relic_dic = {}
for key in full_dic:
    if ('PRIME' in key) and not ('一套' in key) and not ('primed' in full_dic[key]):
        relic_dic[key] = full_dic[key]

sales = {}
count = 0
length = len(relic_dic)

def valid_print(name,query): #有效情况下
    global sales,count
    item_dict = search.search_in_wm(query)
    item_dict['ducats'] = str(item_dict['ducats'])
    item_dict['advicePrice'] = str(item_dict['advicePrice'])
    return (name,item_dict)

def add_to_sales(tulp):
    sales[tulp[0]]=tulp[1]
    global count 
    count += 1
    print(str(count) + ' of ' + str(length))

if __name__ == '__main__':
    print(str(count) + ' of ' + str(length))
    p = multiprocessing.Pool(processes=4)
    for key in relic_dic:
        p.apply_async(valid_print, args=(key,relic_dic[key]),callback=add_to_sales)
    print('waiting')
    p.close()
    p.join()
    print('DONE')

with open(config.json_path + '\\local_sales.json','w+',encoding='utf-8') as local_sales_file:
    local_sales_file.write(json.dumps(sales,indent=4,ensure_ascii=False))

